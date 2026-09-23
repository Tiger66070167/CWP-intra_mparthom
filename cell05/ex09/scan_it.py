import sys
import re

if len(sys.argv) != 3:
    print("none")

else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    count = len(re.findall(keyword, string))

    if count == 0:
        print("none")
        
    else:
        print(count)
