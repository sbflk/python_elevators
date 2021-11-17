import sys
import json
import csv
import pandas
import numpy
import pandas as pd


def AllocateElevator(building, calls, out):
    numberofelevators = len(building["_elevators"])
    with open(out, 'w') as f:
        pass

    df = calls
    if numberofelevators > 1:


    else:
        #return cvs file with zeros at column 6
        df[5] = 0
        df.to_csv(out, header=False, index=False)










if __name__ == '__main__':
    args = sys.argv
    json_file = args[1]
    calls = args[2]
    out = args[3]

    f = open(json_file, "r")
    building = json.load(f)

    df_calls = pd.read_csv(calls, header=None)


    AllocateElevator(building, df_calls, out)
