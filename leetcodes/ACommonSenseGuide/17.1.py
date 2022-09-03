from lib2to3.pytree import Node


class TriesNode:
    def __init__(self):
        self.children = {}
    def collectAllWord(self, node=None, word="", words=[]):
        currentNode = node or self.root 
        for key, childNode in currentNode.children.items():
            if key=="*":
                words.append(word)
            else:
                self.collectAllWord(childNode, word+key, words)
        return words
    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return Node
        return self.collectAllWord(currentNode)
    def traverses(self, node = Node):
        currentNode = node or self.root 
        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.traverses(childNode)
        