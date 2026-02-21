import re
from collections import Counter

with open('custom_components/bms_connector/bms/seplos/v2/sensors.py', 'r', encoding='utf-8') as f:
    content = f.read()

names = []
for match in re.finditer(r'SeplosBMSSensorBase\([^,]*, [^,]*, "[^"]*", "([^"]*)",', content):
    names.append(match.group(1))

for match in re.finditer(r'DerivedSeplosBMSSensor\([^,]*, [^,]*, [^,]*, "([^"]*)",', content):
    names.append(match.group(1))

c = Counter(names)
for name, count in c.items():
    if count > 1:
        print(f"Duplicate Name: {name} (Count: {count})")
