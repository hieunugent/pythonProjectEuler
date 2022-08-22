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