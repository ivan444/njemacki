import re
import sys

ls = sys.stdin.readlines()
for l in ls:
    print re.sub(r"\-([a-z\\\"]+)", r"\\nastavak{\1}", l),

