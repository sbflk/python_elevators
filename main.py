import sys
import json
import csv
import pandas
import numpy
import pandas as pd
from Elevator import Elevator
from CallForElevator import CallForElevator


def AllocateElevator(building, calls, out):
    numberofelevators = len(building["_elevators"])
    with open(out, 'w') as f:
        pass

    df = calls
    elevators = []
    all_calls = []
    if numberofelevators > 1:
        for i in range(numberofelevators):
            current_elev = building["_elevators"][i]
            e = Elevator(i, current_elev["_speed"], current_elev["_closeTime"], current_elev["openTime"],
                         current_elev["_startTime"], current_elev["_stopTime"], 0)
            elevators.append(e)

        for i in calls.iterrows():
            c = CallForElevator(i[1], i[2], i[3])
            all_calls.append(c)





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
