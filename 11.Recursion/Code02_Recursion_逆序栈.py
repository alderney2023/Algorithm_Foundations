###########################################################################
#   不使用其他数据结构反转栈
###########################################################################

def reverse(stack):
    if not stack:
        return
    x = f(stack)
    reverse(stack)
    stack.append(x)
    
def f(stack):
    r = stack.pop() 
    if not stack:
        return r
    last = f(stack)
    stack.append(r)
    return last

#---------------------------------------------------------------------------------

def main():
    stack = [1,2,3]
    reverse(stack)
    print(stack)

if __name__ == "__main__":
    main()