



def print_all_folders(n):
    process(1, n, 0)
    print()

def process(i, n, flag):
    if i>n:
        return 
    process(i+1, n, 0)
    print("凹" if flag == 0 else "凸", end=" ")
    process(i+1, n, 1)

def main():
    print_all_folders(3)

if __name__ == "__main__":
    main()