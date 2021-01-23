import math
import random 

global count
count = 0
RndLog = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
RndLtr = ["", "K", "M", "G", "T"]



def Log(): 
    global count 
    rndChoiceLog = random.choice(RndLog)
    rndChoiceLtr = random.choice(RndLtr)
    longLog = 0

    if rndChoiceLtr == "K":
        longLog = rndChoiceLog * 1000
    elif rndChoiceLtr == "M":
       longLog = rndChoiceLog * 1000000
    elif rndChoiceLtr == "G":
       longLog = rndChoiceLog * 1000000000
    elif rndChoiceLtr == "T":
       longLog = rndChoiceLog * 1000000000000
    else:
        longLog = rndChoiceLog

    ans = round(math.log2(longLog))

    resp = input("LOG " + str(rndChoiceLog) + str(rndChoiceLtr) + " = ")

    if resp == "exit":
        exit()
    
    try:
        val = int(resp)
    except ValueError:
        print("That's not an number! try again!")
        Log()

    if int(resp) == ans:
        count +=1 
        print(str(count) + " in a row CORRECT")
        if count == 3:
            print("Congratulations! You are super awesome. When it comes time to pick a team, I'll pick YOU.")
        else:
            Log()
    else:
        print("The correct answer is " + str(ans))
        print("0 in a row CORRECT")
        count = 0
        Log()

def main():
    Log()

if __name__ == "__main__":
    main()