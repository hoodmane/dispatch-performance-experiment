from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text()
array = [x.split() for x in text.splitlines()]
compilers = ["gcc", "clang", "emcc"]
d = {k: {} for k in compilers}

for [cc, a, _, time, _] in array:
    d[cc][a] = float(time)

denom = d["gcc"]["goto"]
# denom = d["emcc"]["switch"]
denom = d["emcc"]["tcall"]

for col in d.values():
    for method in col.keys():
        col[method] /= denom


print((" " * 6) + "".join(["%7s" % cc for cc in compilers]))
for method in ["switch", "goto", "tcall"]:
    print((f"{method:<6}") + "".join(["%7.3f" % d[cc][method] for cc in compilers]))
