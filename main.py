import sys
import json
import csv
import pandas
import numpy
import pandas as pd


def AllocateElevator(building, calls, df,out):
    numberofelevators = len(building["_elevators"])
    if numberofelevators > 1:
        pass
    else:
        #return cvs file with zeros at column 6
        df[5] = 0
        df.to_csv(out, header=False)










if __name__ == '__main__':
    args = sys.argv
    json_file = args[1]
    calls = args[2]
    out = args[3]

    f = open(json_file, "r")
    building = json.load(f)

    f1 = open(calls, "r")
    calls = f1.read()

    df = pd.read_csv(out, header=None)

    AllocateElevator(building, calls, df, out)
