"""Render the case's parts and check each one, and that the halves close.

usage: python3 case/tests/test_case.py [OPENSCAD]

- top, bot and knob each export as one solid, and demo renders, with
  --hardwarnings and no WARNING or ERROR line: a failed assert leaves the exit
  status at 0, so the output decides.
- The top and bottom halves, where they sit assembled, do not overlap
  (case/tests/fit.scad renders nothing).
"""

import os
import struct
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.join(os.path.dirname(HERE), "transistor_tester.scad")
results = []


def check(label, ok, got):
    results.append(bool(ok))
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {got}")


def render(openscad, src, out, *defines):
    cmd = [openscad, "--hardwarnings", "--export-format", "binstl", "-o", out]
    for d in defines:
        cmd += ["-D", d]
    r = subprocess.run(cmd + [src], capture_output=True, text=True)
    return r, [l for l in r.stderr.splitlines() if l.startswith(("WARNING", "ERROR"))]


def solids(path):
    data = open(path, "rb").read()
    (n,) = struct.unpack_from("<I", data, 80)
    parent = {}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for i in range(n):
        t = struct.unpack_from("<9f", data, 84 + i * 50 + 12)
        corners = [t[0:3], t[3:6], t[6:9]]
        for c in corners:
            parent.setdefault(c, c)
        root = find(corners[0])
        for c in corners[1:]:
            parent[find(c)] = root
    return len({find(v) for v in parent})


def main():
    openscad = sys.argv[1] if len(sys.argv) > 1 else "openscad"
    with tempfile.TemporaryDirectory() as tmp:
        stl = os.path.join(tmp, "out.stl")
        for part in ("top", "bot", "knob"):
            r, bad = render(openscad, CASE, stl, f'part="{part}"')
            n = solids(stl) if r.returncode == 0 and not bad else 0
            check(f"{part} is one clean solid", n == 1, bad[:1] or f"{n} solid(s)")
        r, bad = render(openscad, CASE, stl, 'part="demo"')
        check("demo renders", r.returncode == 0 and not bad, bad[:1] or "clean")
        r, _ = render(openscad, os.path.join(HERE, "fit.scad"), stl)
        empty = "top level object is empty" in r.stderr.lower()
        check("the halves close without overlapping", empty, "no overlap" if empty else "they overlap")
    print(f"{sum(results)} of {len(results)} checks passed")


if __name__ == "__main__":
    main()
    sys.exit(0 if results and all(results) else 1)
