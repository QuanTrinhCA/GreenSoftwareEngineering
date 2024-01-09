# [Problem 4: Green software engineering](https://www.unb.ca/saintjohn/sase/_assets/documents/problems2019.pdf)

Software quality is not only about returning the correct answer or running fast: it can also be 
about the amount of energy required by the computer or device to run that software. For 
example, our choice of how to store and access data in the program has an impact on the 
energy consumption. This is an important aspect to consider when developing software. For 
example, reducing the energy used by mobile devices leads to longer battery lives. The domain 
related to this problem is called green software engineering.

A first step in identifying where we can focus our attention for reducing energy consumption is 
to measure the energy required for each function in the software. Your program should help 
with this. In particular, assuming that you have the number of watts at every second while 
running the program (as input), we want to calculate how many joules (unit of energy 
consumption) were necessary overall. We also want such information for each sub-function 
(“function”, “module”, “method”, etc.) used throughout the execution of the program.

The input starts with a positive integer N, indicating the number of seconds that the application 
was running. Then you have N lines (one per second), each having a real number indicating the 
number of watts at that time. An empty line separates this part from the second part, which is 
for indicating when each sub-function was running. This part starts with a positive integer 
indicating the number of sub-functions. Then there is one line of input for each sub-function: 
first there is an index indicating when this sub-function started running (with index 0 being the 
first second that the program was running), and then you have the name of that sub-function 
(no space in the name). It is assumed that the sub-functions were executed in sequence, from 
the index they began (inclusively) up to the index of the next sub-function (exclusive). The list of 
sub-functions is always sorted over time in the input, from earliest to latest. So for the example 
input below, the “Init” function ran from second 0 to 2 (inclusively), the “Main” function ran 
from second 3 to 7, and finally the “Closing” function ran from second 8 to 9 (i.e., until the end).

Your program should calculate, for each sub-function, the average watts over the 
corresponding period (e.g., for “Init”, take the average of 0.7, 1.0 and 1.5). Then you should 
multiply this number by the number of seconds the sub-function took, in order to get the 
number of joules used. Round up this number of joules (i.e., take the ceiling of that number)
and print it in the format shown in the example output below. Finally, add the number of joules 
used by each sub-function and print this. Also indicate which of the sub-functions used the 
highest number of joules.

## Sample Input 1
```
10
0.7
1.0
1.5
1.3
1.7
1.8
2.0
1.9
1.1
1.5
3
0 Init
3 Main
8 Closing
```

## Sample Output 1
```
Init used 4 joules
Main used 9 joules
Closing used 3 joules
total joules: 16
worst: Main
```
