###########################################################################
#   汉诺塔
###########################################################################


def Hanoi(n):
    process(n, "left","right","mid")

def process(n, source, target, other):
    if n == 1:
        print(n, "from", source,"to", target)
        return
    process(n-1, source, other, target)
    print(n, "from", source, "to", target)
    process(n-1, other, target, source)


#---------------------------------------------------------------------------------

def main():
    n = 3
    Hanoi(n)
    #hanoi_simulate_process(n)

if __name__ == "__main__":
    main()