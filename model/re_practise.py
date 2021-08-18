import re

matcher = re.finditer("a?",'abaabaab')
for match in matcher:
    print(match.start(),"....",match.group())