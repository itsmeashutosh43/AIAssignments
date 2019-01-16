import numpy as np
import copy
class Parent:
	def __init__(self,parent,child1=None,child2=None,child3=None,child4=None):
		self.parent=parent
		self.child1=child1
		self.child2=child2
		self.child3=child3
		self.child4=child4

	def getAll(self):
		return((self.child1,self.child2,self.child3,self.child4))


class Board:
	def __init__(self,boardDimention):
		self.boardDimention=boardDimention
		self.goal=self.makeBoard()
	def makeBoard(self):
		size=self.boardDimention

		board=[int(i) for i in range(1,size**2+1) ]
		board[size**2-1]=0

		return np.array(board).reshape(size,size).tolist()

	def isGoal(self):
		return self.goal

	def findFourState(self,presentState):
		for i,j in enumerate(presentState):
			for k,l in enumerate(j):
				if l==0:
					x,y=i,k
					break


		presentState1=copy.deepcopy(presentState)
		presentState2=copy.deepcopy(presentState)
		presentState3=copy.deepcopy(presentState)
		presentState4=copy.deepcopy(presentState)


		allPossibleStates=[]

		newX=x-1
		newY=y

		try:
			if newX>=0:
			
				temp=presentState1[newX][newY]
				presentState1[newX][newY]=presentState1[x][y]
				presentState1[x][y]=temp
				
				allPossibleStates.append(presentState1)
		except IndexError:
			pass

		newX=x+1
		newY=y

		try:
			
			temp=presentState2[newX][newY]
			presentState2[newX][newY]=presentState2[x][y]
			presentState2[x][y]=temp
			#print(presentState2,2)
			allPossibleStates.append(presentState2)
			
		except IndexError:
			pass

		newX=x
		newY=y-1


		try:
			if newY>=0:
				temp=presentState3[newX][newY]
				presentState3[newX][newY]=presentState3[x][y]
				presentState3[x][y]=temp
				#print(presentState3,3)
				allPossibleStates.append(presentState3)
				
		except IndexError:
			pass

		newX=x
		newY=y+1


		try:
			
			temp=presentState4[newX][newY]
			presentState4[newX][newY]=presentState4[x][y]
			presentState4[x][y]=temp
			#print(presentState4,4)
			allPossibleStates.append(presentState4)
			
		except IndexError:
			pass


		return (allPossibleStates)


	def findDistance(self,child,i):
		size=self.boardDimention
		newArray=self.goal.copy()
		count=0

		for a in range(size):
			for b in range(size):
				if child[a][b]!=0:
					if child[a][b]!=newArray[a][b]:
					
						count+=1
				else:
					pass

		return count+i




def calculateInversions(ourInput):
	inputt=ourInput.copy()
	inputt.remove(0)
	#ourInput.remove(0)
	l=0
	for i,j in enumerate(inputt):
		for k in range(i,len(inputt)):
			if j>inputt[k]:
				l+=1

	return l

def calculateRow(ourInput):
	size=len(ourInput)
	
	size=int(size**0.5)

	array=np.array(ourInput).reshape(size,size).tolist()

	for i,j in enumerate(array):
		if 0 in j:
			return i




def solutionExists(ourInput,boardDimention):
	numberOfInversions=calculateInversions(ourInput)
	print(numberOfInversions)
	rowOfBlankSquare=calculateRow(ourInput)

	if boardDimention%2!=0:
		if numberOfInversions%2==0:
			return True
		else:
			return False
	else:
		if (numberOfInversions+rowOfBlankSquare)%2!=0:
			return True
		else:
			return False

			
def main():
	ll=0
	boardDimention=int(input(("Enter the board dimention you want :")))

	board=Board(boardDimention)

	print(board.isGoal())


	ourInput=[int(x) for x in input("Write your desired entry with a space (write 0 for blank)").split(' ')]
	boardInput=np.array(ourInput).reshape(boardDimention,-1).tolist()

	if solutionExists(ourInput,boardDimention):
		print ("The solution exists")

		print (boardInput)

		print ('\n')

		print ('**************************************************')

		presentState=copy.deepcopy(boardInput)
		states=[]
		states.append(presentState)
		i=0
		explored=[]
		listOfGraphs=[]

		while states:
			i+=1
			
			state=states.pop()
			#popping the current state

			explored.append(state)


			

			if board.findDistance(state,0)==0:
				return listOfGraphs
				#returning if we reach the goal state.


			children=board.findFourState(state)
			#finding atmost four states given a child c.

			scores=[]
			sons=[]
			for child in children:
				sons.append(child)
				
				if (child not in explored) and (child not in states):
					#checking if the state is already explored
					
					#scores.append(board.findDistance(child,i))
					states.append(child)
					#print (child,"accepted")

			drawGraphs=Parent(state,(*sons))
			listOfGraphs.append(drawGraphs)

			
			#index=min(scores)

			#states.append(children[scores.index(index)])

			

		
			

			

		return 0
				
		

	else:
		
		print ("Sorry the solution does not exist")

		return 0


listOfGraphs=main()

if listOfGraphs!=0:

	step=0
	for steps in listOfGraphs:
		step+=1

		print ("Step, ",step)


		print ('\t\t\t\t',steps.parent)

		print ('\n')

		a=steps.getAll()

		for i in a:
			try:
				if i!=None:
					
					print('\t',i,end='')
			except:
				pass

		print ('\n')
		print ('************************************************')