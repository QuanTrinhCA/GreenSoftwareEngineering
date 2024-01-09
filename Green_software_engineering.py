import math

print("Input:")
wattsPerSec = list()
secTotal = int(input())
for x in (range(secTotal)):
    wattsPerSec.append(float(input()))

functions = list()
for x in (range(int(input()))):
    buffer = input().split()
    functions.append([buffer[0], buffer[1], 0])

for x in range(len(functions)):
    energyUsed = float()
    if x == len(functions) - 1: 
        secUsed = secTotal - 1 - int(functions[x][0])
        for y in range(secUsed + 1): energyUsed += wattsPerSec[int(functions[x][0]) + y]
    else: 
        secUsed = int(functions[x + 1][0]) - int(functions[x][0])
        for y in range(secUsed): energyUsed += wattsPerSec[int(functions[x][0]) + y]
    functions[x][2] = str(math.ceil(energyUsed))
    

energyTotal = int()
worstFunc = functions[0]
for function in functions:
    energyTotal += int(function[2])
    print(str(function[1]) + " used " + str(function[2]) + " joules")
    if function[2] > worstFunc[2]: worstFunc = function

print("Total joules: " + str(energyTotal))
print("Worst: " + str(worstFunc[1]))