import sys
import json









if __name__ == '__main__':
    args = sys.argv
    json_file = args[1]
    calls = args[2]
    out = args[3]


    f = open(json_file, "r")

    f = json.load(f)
    print(type(f))
