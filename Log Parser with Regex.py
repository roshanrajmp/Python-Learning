import re
from collections import Counter

errors = []
with open("app.log") as f:
    for line in f:
        match = re.search(r"ERROR|WARN|INFO", line)
        if match:
            errors.append(match.group())

print(Counter(errors))
