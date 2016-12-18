import re
import sys

ls = sys.stdin.readlines()
cols = ls[0].strip().split("|")
print r"\begin{table}[H]"
print r"\begin{tabular}{%s}" % ("l" * len(cols))
print r"\toprule"
print " & ".join(cols) + r" \\"
print r"\midrule"
for l in ls[1:]:
    print re.sub("\|", "&", l.strip()) + r" \\"
print r"\bottomrule"
print r"\end{tabular}"
print r"\end{table}"
