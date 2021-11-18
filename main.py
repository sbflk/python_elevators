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
    elevators = []#all elevators
    all_calls = []#all calls
    if numberofelevators > 1:
        for i in range(numberofelevators):
            current_elev = building["_elevators"][i]
            e = Elevator(i, current_elev["_speed"], current_elev["_closeTime"], current_elev["_openTime"],
                         current_elev["_startTime"], current_elev["_stopTime"], 0, None)
            elevators.append(e)

        for i in calls.iterrows():
            c = CallForElevator(i[1][1], i[1][2], i[1][3])
            all_calls.append(c)

        for i in range(numberofelevators):# give each elevator one call to start with
            df.at[i, 5] = i
            elevators[i].set_current_call(all_calls[i])

        for j in range(numberofelevators, len(all_calls)):
            when_will_finish = []  # did elevator finish previous call or how longer will it take
            current_call = all_calls[j]
            for i in range(numberofelevators):
                e = elevators[i]
                time_from_last_call = e.get_current_call().get_time() + e.get_closetime() + e.get_starttime() + \
                                      e.get_stoptime() + e.get_opentime() + \
                                      (abs(e.get_current_call().get_dest()-current_call.get_src()))/e.get_speed()
                if time_from_last_call-current_call.get_time() <= 0:
                    when_will_finish.append(0)
                else:
                    when_will_finish.append(time_from_last_call-current_call.get_time())


            min_t = all_calls[-1].get_time() + 120 #max time
            fastest_times = []# list because more than 1 elevator could have time 0 which means she has no calls
            for i in range(len(when_will_finish)):
                if when_will_finish[i] < min_t:
                    min_t = when_will_finish[i]
                    fastest_times = [i]
                elif when_will_finish[i] == min_t:
                    fastest_times.append(i)

            if len(fastest_times) == 1:
                df.at[j, 5] = fastest_times[0]
            else:
                fastest = fastest_times[0]
                for i in fastest_times:
                    if elevators[i].get_speed() > elevators[fastest].get_speed():
                        fastest = i

                df.at[j, 5] = fastest

        df.to_csv(out, header=False, index=False)



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
