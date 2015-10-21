def main():
	tree=[]
	inputList=[]
	print 'Enter the number of nodes',
	limit=int(raw_input())
	print 'Enter ',limit,'elements'

	for k in range(limit):
		inputList.append(int(raw_input()))
	for i in inputList:
		tree=avlInsert(tree,i)
	print 'avlTree in list'
	print tree
	print 'avlTree:'
	printTree(tree)
	print '\nHeight of the tree is ',tree[1]
	
def printTree(tree):
	if len(tree)!=0:
		printTree(tree[2])
		print tree[0],
		printTree(tree[3])

def height(tree):
	if len(tree)==0:
		return 0
	else:
		lh=height(tree[2])
		rh=height(tree[3])
		if lh > rh:
			return lh+1
		else:
			return rh+1

def max(tree1,tree2):
	if height(tree1) > height(tree2):
		return height(tree1)
	else:
		return height(tree2)

def rightRotate(tree):
	newRoot=[]
	newRoot=tree[2]
	tree[2]=newRoot[3]
	newRoot[3]=tree
	tree[1]=1+max(tree[2],tree[3])
	newRoot[1]=1+max(newRoot[2],newRoot[3])
	return newRoot

def leftRotate(tree):
	newRoot=[]
	newRoot=tree[3]
	tree[3]=newRoot[2]
	newRoot[2]=tree
	tree[1]=1+max(tree[2],tree[3])
	newRoot[1]=1+max(newRoot[2],newRoot[3])
	return newRoot	

def avlInsert(tree,data):
	if len(tree)==0:
		return [data,0,[],[]]
	else:
		if  data <= tree[0]:
		    tree[2]=avlInsert(tree[2],data)
	        else:
		    tree[3]=avlInsert(tree[3],data)

	balance=height(tree[2])-height(tree[3])

	if balance > 1:
		if height(tree[2][2]) >= height(tree[2][3]):
			return rightRotate(tree)
		else:
			tree[2]=leftRotate(tree[2])
			return rightRotate(tree)

	if balance < -1:
		if height(tree[3][3]) >= height(tree[3][2]):
			return leftRotate(tree)
		else:
			tree[3]=rightRotate(tree[3])
			return leftRotate(tree)

	tree[1]=1+max(tree[2],tree[3])	
	return tree 

main()
