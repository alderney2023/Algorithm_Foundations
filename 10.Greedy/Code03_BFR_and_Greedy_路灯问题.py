
import random


#暴力递归
def minLights(lst):
    if not list or len(lst)==0:
        return 0
    lights = set()
    return process(lst, 0, lights)

def process(lst, i, lights):
    if i == len(lst):
        for j in range(len(lst)):
            if lst[j] == '.' and (j-1 not in lights) and (j not in lights) and (j+1 not in lights):
                return float('inf')
        return len(lights)
    yes = float("inf")
    if lst[i] == '.':    
        lights.add(i)
        yes = process(lst, i+1, lights)
        lights.remove(i)
    no = process(lst, i+1, lights)
    return min(yes, no)


#---------------------------------------------------------------------------------
#贪心算法

def minLights2(lst):
    light = 0
    i=0;
    while i < len(lst) :
        if lst[i] == 'X':
            i+=1
        else:
            light += 1
            if i+1 == len(lst):
                break
            elif lst[i] == '.' and lst[i+1] == '.':
                i += 3
            else:
                i += 2
    return light






#---------------------------------------------------------------------------------

def generateRandomString(cnt):
    lst = []
    for i in range(cnt):
        x = "X" if random.choice([0,1,2]) == 0 else "."
        lst.append(x)
    return lst


def main():
    cnt = 20
    lst = generateRandomString(20)
    print(lst)
    print(minLights(lst))
    print(minLights2(lst))


if __name__ == "__main__":
    main()