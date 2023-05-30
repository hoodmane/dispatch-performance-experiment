#!/bin/python3
import subprocess
import itertools
import random
from pathlib import Path
import json
import statistics


OPTFLAGS = ["O2", "O3", "Os"]
COMPILERS = ["gcc", "clang", "emcc"]
METHODS = ["switch", "cgoto", "tcall"]


def out_gen(outfile):
    with open(outfile, "w+") as o:
        while True:
            [triple, time] = yield
            o.write(json.dumps([list(triple), time]) + "\n")
            o.flush()


def get_results(out, trials):
    combos = list(itertools.product(COMPILERS, OPTFLAGS, METHODS))

    out.send(None)
    for _ in range(trials):
        for triple in random.sample(combos, len(combos)):
            cmd = ["./interp_" + "-".join(triple)]
            if triple[0] == "emcc":
                cmd.insert(0, "node")
            result = subprocess.run(
                cmd, capture_output=True, encoding="utf8", check=True, cwd="./bin"
            )
            time_str = result.stdout.split()[-2]
            time = float(time_str)
            out.send([triple, time])
    out.close()


if not Path("results.data").exists():
    get_results(out_gen("results.data"), 100)


with open("results.data", "r") as f:
    raw_data = {}
    for line in f.readlines():
        [key, val] = json.loads(line)
        raw_data.setdefault(tuple(key), []).append(val)

results = {}
for key, val in raw_data.items():
    results[key] = statistics.geometric_mean(val)

denom = results[("gcc", "O2", "cgoto")]

for a in results.keys():
    results[a] /= denom


def format_row(method, entryfmt, entries):
    def gen():
        yield f"| {method:<6}"
        for entry in entries:
            yield entryfmt % entry
        yield ""

    return (" | ".join(gen())).strip()


def format_hline():
    def gen():
        yield 0
        yield 6 + 2
        for _ in COMPILERS:
            yield 5 + 2
        yield 0

    return "|".join("-" * n for n in gen())


for optflag in OPTFLAGS:
    print(f"#### {optflag}:")
    print()
    print(format_row("", "%5s", COMPILERS))
    print(format_hline())

    for method in METHODS:
        entries = (results[(cc, optflag, method)] for cc in COMPILERS)
        print(format_row(method, "%5.3f", entries))
    print("\n")
