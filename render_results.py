from pathlib import Path
import subprocess
import os


OPTFLAGS = ["-O2", "-O3", "-Os"]
COMPILERS = ["gcc", "clang", "emcc"]

results = {}

env = os.environ.copy()
for optflag in OPTFLAGS:
    optflag_dict = {}
    results[optflag] = optflag_dict
    Path("main.c").touch()
    env["OPTFLAG"] = optflag
    subprocess.run(["make"], env=env, check=True)

    for compiler in COMPILERS:
        opt_cc_dict = {}
        optflag_dict[compiler] = opt_cc_dict
        cmd = [f"./interp_{compiler}"]
        if compiler == "emcc":
            cmd.insert(0, "node")
        result = subprocess.run(cmd, capture_output=True, encoding="utf8", check=True)
        for line in result.stdout.splitlines():
            [_, method, _, time, _] = line.split()
            opt_cc_dict[method] = float(time)


# denom = d["gcc"]["goto"]
# denom = d["emcc"]["switch"]
# denom = d["emcc"]["tcall"]
denom = results["-O2"]["gcc"]["goto"]

for a in results.values():
    for b in a.values():
        for method in b.keys():
            b[method] /= denom


for optflag in ["-O2", "-O3", "-Os"]:
    optflag_dict = results[optflag]
    print("OPTFLAG:", optflag)
    print((" " * 6) + "".join(["%7s" % cc for cc in COMPILERS]))
    for method in ["switch", "goto", "tcall"]:
        print(
            f"{method:<6}"
            + "".join(["%7.3f" % optflag_dict[cc][method] for cc in COMPILERS])
        )
    print("\n")
