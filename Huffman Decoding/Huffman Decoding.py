"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
#def decodeHuff(root, s):
	#Enter Your Code Here
    
"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    cur = root
    chararray = []
    #For each character, 
    #If at an internal node, move left if 0, right if 1
    #If at a leaf (no children), record data and jump back to root AFTER processing character
    for c in s:
        if c == '0' and cur.left:
            cur = cur.left
        elif cur.right:
            cur = cur.right
        
        if cur.left is None and cur.right is None:
            chararray.append(cur.data)
            cur = root
    
    #Print final array
    print("".join(chararray))
            
            