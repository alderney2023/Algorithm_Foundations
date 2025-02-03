###########################################################################
# 每个学生有三个属性， 任意一个属性相同就认为是一个人
# 输入： 给出一群人
# 输出： 实际有多少人
# ###########################################################################


from Code01_并查集_灵活字典版 import UnionSet

class User:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

def mergeUsers(users):

    attr1 = {}
    attr2 = {}
    attr3 = {}
    us = UnionSet(users)
    
    for user in users:
        if user.attr1 in attr1:
            us.union(user, attr1[user.attr1])
        else:
            attr1[user.attr1] = user
        if user.attr2 in attr2:
            us.union(user, attr2[user.attr2])
        else:
            attr2[user.attr2] = user
        if user.attr3 in attr3:
            us.union(user, attr3[user.attr3])
        else:
            attr3[user.attr3] = user
    return us.sets()



#---------------------------------------------------------------------------------

def main():
    user_lst = [User('abc1','mn2','xyz1'),
            User('abc1','mn3','xyz2'),
            User('abc2','mn4','xyz3'),
            User('abc3','mn1','xyz4'),
            User('abc4','mn5','xyz5'),
            User('abc5','mn5','xyz6'), ]
    user_number = mergeUsers(user_lst)
    print(user_number)


if __name__ == "__main__":
    main()