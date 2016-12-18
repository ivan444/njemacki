import re
import sys

ls = sys.stdin.readlines()
for l in ls:
    print re.sub(r"\b(der|die|das|dem|den|ein.*)\b", r"\\clan{\1}", l),

