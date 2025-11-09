import heapq

# Huffman Tree Node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    # 👇 Comparison method for heapq
    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Function to print Huffman codes
def Printnode(node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        Printnode(node.left, newVal)
    if node.right:
        Printnode(node.right, newVal)

    # If leaf node
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


# Input data
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [50, 10, 30, 5, 3, 2]

# Create priority queue
nodes = []

for i in range(len(chars)):
    heapq.heappush(nodes, Node(freq[i], chars[i]))

# Build Huffman Tree
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newNode)

# Print Huffman Codes
print("Huffman Codes for given characters:\n")
Printnode(nodes[0])
