
from locale import currency


class TriesNode:
    def __init__(self):
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TriesNode()
    def insert(self, word):
        currentNode = self.root 
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TriesNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children["*"] = None
    def collectAllWord(self, node=None, word="", words=[]):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWord(childNode, word+key, words)
        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWord(currentNode)

    def traverses(self, node=Node):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.traverses(childNode)

    def autoCorrect(self, word):
        currentNode = self.root
        wordFoundSoFar = ""
        for char in word:
            if currentNode.children.get(char):
                wordFoundSoFar += char
                currentNode = currentNode.children.get(char)
            else:
                return wordFoundSoFar + self.collectAllWord(currentNode)[0]
        return word

    
        
