




class info:
    def __init__(self, yes, no):
        self.yes = yes
        self.no = no

def maxHappy(head):
    if not head:
        return 0
    info = process(head)
    return max(info.yes, info.no)

def process(head):
    if not head.nexts:
        return info(head.happy,0)
    yes = head.happy
    no = 0
    for e in head.nexts:
        yes += process(e).no
        no += max(process(e).yes, process(e).no)
    return info(yes, no)

class Employee:
    def __init__(self, happy=0, nexts=[]):
        self.happy = happy
        self.nexts = nexts

def main():
    node11 = Employee(40)
    node12 = Employee(10)
    node13 = Employee(20)
    node21 = Employee(10)
    node22 = Employee(50)
    node31 = Employee(5)
    node1 = Employee(20, [node11,node12,node13])
    node2 = Employee(30, [node21,node22])
    node3 = Employee(100, [node31])  
    node0 = Employee(10, [node1,node2,node3])
    print(maxHappy(node0))



if __name__ == "__main__":
    main()