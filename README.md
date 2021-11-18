Study of the subject:
1. https://www.geeksforgeeks.org/scan-elevator-disk-scheduling-algorithms/
shows the algorithm SCAN that works for one elevator. Shows the pros and cons of the algorithm, explains the algorithm in pseudo – code,
and talks about the complexity of the algorithm. This algorithm can be a good basis for starters.

2. https://elevation.fandom.com/wiki/Destination_dispatch#Overview
Talks about methods for optimization of buildings with several elevators.
Explains the pros and cons of such methods, and shows what methods are used in different countries.

3. https://www.youtube.com/watch?v=xOayymoIl8U
A video that explains the basis of an algorithm for an optimization of one or several elevators.
This video showcases several ways to improve the basic algorithms.

Difference between offline and online algorithms:

Offline algorithms work with the basis that we have all the information we will work with beforehand.
In this elevator algorithm, it means that we will know when and where each call for an elevator will be.

Online algorithms work with the basis that we will receive new input/s that we had no knowledge of beforehand while the algorithm is working. 
In this elevator algorithm, it means that we will receive calls without prior knowledge or specific preparations for them.


The algorithm:

If there is only one elevator in the building, the algorithm will set all the given calls to that elevator.
If there are more than one elevator, firstly, the algorithm gives each of the elevators a call to start with, the earliest ones. 
Then, for every call after that, the algorithm calculates the whole time it will take for each elevator to finish their current call if they have one,
get to the next call and finish it as well, the elevator with the lowest time will be assigned for that call. 
If more than one elevator has the lowest time(very unlikely), the elevator with the higher speed will be assigned for the call.

Class diagram:


![uml_diagram1](https://user-images.githubusercontent.com/76430228/142437880-287d4f60-d926-4290-8972-d07795dd75bb.png)


Report Table:
This is the report table of the calls in each building.

In each square there are two rows.

The first row is the average time.

The second is the amount of uncompleted calls. 

<img width="465" alt="table of reports" src="https://user-images.githubusercontent.com/76430228/142435321-1f620100-4806-4050-bcf1-7c5f2917efe9.PNG">








