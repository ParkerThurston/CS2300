#Code written by Parker Thurston
import math
lyst = [math.pi, math.e,-(math.e),-(math.pi)]
for i in lyst:
    s = ''
    if i < 0:
        s = "-"
    if i == math.pi or i == -(math.pi):
        s += 'pi'
    elif i == math.e or i == -(math.e):
        s += 'e'
    print("Ceiling of "+ s + " is: " + str(math.ceil(i)))
    print("Floor of "+ s + " is: " + str(math.floor(i)))
    print("Round of "+ s + " is: " + str(round(i)))
    print("Truncate of "+ s + " is: " + str(math.trunc(i)))