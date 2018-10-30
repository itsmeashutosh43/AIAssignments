import math

class State:
	def __init__(self,miLeft,caLeft,pos,miRight,caRight):
		self.miLeft=miLeft
		self.caLeft=caLeft
		self.pos=pos
		self.miRight=miRight
		self.caRight=caRight
		self.parent=None

	def goal(self):
		if self.miLeft==0 and self.caLeft==0:
			return True

		else:
			return False

	def valid(self):
		if self.miLeft >= 0 and self.miRight >= 0 and self.caLeft >= 0 and self.caRight >= 0 and (self.miLeft == 0 or self.miLeft >= self.caLeft) and (self.miRight == 0 or self.miRight >= self.caRight):
			return True
		else:
			return False



def successors(state):
	children=[]


	if state.pos=='left':
		newState=State(state.miLeft,state.caLeft-2,'right',state.miRight,state.caRight+2)
		if newState.valid():
			children.append(newState)
			newState.parent=state

			

		# 1 completed

		newState=State(state.miLeft-1,state.caLeft-1,'right',state.miRight+1,state.caRight+1)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		# 2 completed

		newState=State(state.miLeft-2,state.caLeft,'right',state.miRight+2,state.caRight)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		# 3 completed

		newState=State(state.miLeft-1,state.caLeft,'right',state.miRight+1,state.caRight)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		#4 completed

		newState=State(state.miLeft,state.caLeft-1,'right',state.miRight,state.caRight+1)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		#5 completed

	else:

		newState=State(state.miLeft+1,state.caLeft+1,'left',state.miRight-1,state.caRight-1)
		if newState.valid():
			children.append(newState)
			newState.parent=state
		#1 completed

		newState=State(state.miLeft+2,state.caLeft,'left',state.miRight-2,state.caRight)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		newState=State(state.miLeft+1,state.caLeft,'left',state.miRight-1,state.caRight)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		newState=State(state.miLeft,state.caLeft+1,'left',state.miRight,state.caRight-1)
		if newState.valid():
			children.append(newState)
			newState.parent=state

		newState=State(state.miLeft,state.caLeft+2,'left',state.miRight,state.caRight-2)
		if newState.valid():
			children.append(newState)
			newState.parent=state



	return children


def bfs():
	init=State(3,3,'left',0,0)

	if init.goal():
		return init

	allList=list()
	exploredNodes=set()

	allList.append(init)
	while allList:
		state=allList.pop(0)
		if state.goal():
			return state
		exploredNodes.add(state)
		children=successors(state)
		
		for child in children:
			if (child not in exploredNodes) or (child not in allList):
				allList.append(child)




	return None




def printSolutions(solution):
	path=[]
	path.append(solution)

	parentOfNode=solution.parent


	while parentOfNode:
		path.append(parentOfNode)
		parentOfNode=parentOfNode.parent

	for t in range(len(path)):
		state=path[len(path)-t-1]

		print ("(" + str(state.caLeft) + "," + str(state.miLeft) \
                              + "," + state.pos + "," + str(state.caRight) + "," + \
str(state.miRight) + ")")




def main():
	solution=bfs()

	print ("The solution is:")

	print ("missionaryleft,cannibalLeft,position,missionaryRight,cannibalRight")

	printSolutions(solution)




if __name__=="__main__":
	main()


