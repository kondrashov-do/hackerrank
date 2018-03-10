class Node:
    def __init__(self):
        self.children = {}
        self.size = 0

    def putChild(self, ch):
        self.children[ch] = Node()

    def getChild(self, ch):
        return self.children[ch]

    def getSize(self):
        return self.size
    def incSize(self):
        self.size += 1

    def getChildren(self):
        return self.children

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr_node = self.root
        for ch in word:
            if ch in curr_node.getChildren():
                curr_node = curr_node.getChild(ch)
            else:
                curr_node.putChild(ch)
                curr_node = curr_node.getChild(ch)
            curr_node.incSize()
    def find(self, word):
        curr_node = self.root
        for ch in word:
            if ch in curr_node.getChildren():
                curr_node = curr_node.getChild(ch)
            else:
                return 0
        return curr_node.getSize()

trie = Trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    else:
        print(trie.find(contact))
