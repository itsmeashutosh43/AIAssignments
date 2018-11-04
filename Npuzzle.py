import numpy as np
class Board:
	def __init__(self,boardDimention):
		self.boardDimention=boardDimention
		self.goal=self.makeBoard()
	def makeBoard(self):
		size=self.boardDimention

		board=[int(i) for i in range(1,size**2+1) ]
		board[size**2-1]=0

		return np.array(board).reshape(size,size)

	def isGoal(self):
		return self.goal

	def findFourState(self,presentState):
		for i,j in enumerate(presentState):
			for k,l in enumerate(j):
				if l==0:
					x,y=i,k
					break


		presentState1=presentState.copy()
		presentState2=presentState.copy()
		presentState3=presentState.copy()
		presentState4=presentState.copy()


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
				allPossibleStates.append(presentState3)
				print(newX,newY)
		except IndexError:
			pass

		newX=x
		newY=y+1


		try:
			
			temp=presentState4[newX][newY]
			presentState4[newX][newY]=presentState4[x][y]
			presentState4[x][y]=temp
			allPossibleStates.append(presentState4)
			print(newX,newY)
		except IndexError:
			pass


		return np.array(allPossibleStates)


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

	array=np.array(ourInput).reshape(size,size)

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
	boardDimention=int(input(("Enter the board dimention you want :")))

	board=Board(boardDimention)

	print(board.isGoal())


	ourInput=[int(x) for x in input("Write your desired entry with a space (write 0 for blank)").split(' ')]
	boardInput=np.array(ourInput).reshape(boardDimention,-1)

	if solutionExists(ourInput,boardDimention):
		print ("The solution exists")

		print (boardInput)

		print ('\n')

		print ('**************************************************')

		presentState=boardInput.copy()
		states=[]
		states.append(presentState)
		i=0

		while states:
			i+=1
			explored=[]
			state=states.pop()
			explored.append(state)
			

			if board.findDistance(state,0)==0:
				print ("Answer found biyatchhh")
				return state


			children=board.findFourState(state)
			
			scores=[]

			for child in children:
					

				scores.append(board.findDistance(child,i))
			
			index=min(scores)

			states.append(children[scores.index(index)])
			

			

		return 0
				
		

	else:
		
		print ("Sorry the solution does not exist")


main()