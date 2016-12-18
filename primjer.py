import sys

ls = sys.stdin.read()
for l in ls:
    lr = l.split("->")
    left = lr[0].strip()
    right = lr[1].strip()
    print r"\primjer{%s \\rightarrow %s}"
