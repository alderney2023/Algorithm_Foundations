


class Node:
    def __init__(self):
        self.through = 0
        self.end = 0
        self.nexts = {}

class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        if word == None or word == "":
            return
        cur = self.root
        cur.through += 1
        for x in word:
            if x not in cur.nexts:
                cur.nexts[x] = Node()   
            cur = cur.nexts[x]
            cur.through += 1
        cur.end += 1

    def erase(self, word):
        if self.countWordsEqualTo(word)==0:
            return 
        cur = self.root
        cur.through -= 1
        for x in word:
            cur.nexts[x].through -= 1
            if cur.nexts[x].through == 0:
                del cur.nexts[x]
            cur = cur.nexts[x]  
        cur.end -= 1
        
    def countWordsEqualTo(self, word):
        if word == None or word == "":
            return 0
        cur = self.root
        for x in word:
            if x not in cur.nexts:
                return 0
            cur = cur.nexts[x]
        return cur.end

    def countWordsStartingWith(self, word):
        cur = self.root
        for x in word:
            if x not in cur.nexts:
                return 0
            cur = cur.nexts[x]
        return cur.through


#---------------------------------------------------------------------------------

def main():
    
    lst = ['abc','abd','abcd','abcd','ab']

    trie = Trie()
    for x in lst:
        trie.insert(x)
    print(trie.countWordsEqualTo("ab"))
    print(trie.countWordsStartingWith("ab"))
    print(trie.root.nexts['a'].nexts['b'].nexts['c'].through)

    print(trie.countWordsEqualTo("abcd"))
    trie.erase('abcd')
    print(trie.countWordsEqualTo("abcd"))

if __name__ == "__main__":
    main()