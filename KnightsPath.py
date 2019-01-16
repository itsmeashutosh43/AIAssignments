#Knight's Tour

'''
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.


'''











class Chess:
	def __init__(self,n):
		self.chessBoard=self.make()
		self.n=n

	def isPossible(self,i,j):
		if (i>=0 and i<=self.n-1) and (j>=0 and j<=self.n-1):
			return True
		return False

	def make(self):
		chessBoard=[[(i,j)for i in range(4)]for j in range(4)]

		return chessBoard

	def findNextMove(self,states):
		state=[]

		x1=states[0]
		x2=states[1]

		newx1=x1-1
		newy1=x2-2

		if self.isPossible(newx1,newy1):
			state.append((newx1,newy1))


		newx1=x1-2
		newy1=x2-1

		if self.isPossible(newx1,newy1):
			state.append((newx1,newy1))

		newx1=x1+2
		newy1=x2+1

		if self.isPossible(newx1,newy1):
			state.append((newx1,newy1))

		newx1=x1+1
		newy1=x2+2

		if self.isPossible(newx1,newy1):
			state.append((newx1,newy1))

		newx1=x1+2
		newy1=x2-1

		if self.isPossible(newx1,newy1):
			state.append((newx1,newy1))

		newx1=x1+1
		newy1=x2-2

		if self.isPossible(newx1,newy1):
			state.append((newx1,newy1))

		return state







def main():
	n=4
	chess=Chess(4)
	for i in chess.chessBoard:
		for j in i:
			explored=set()
			activeState=[]
			i=0
			activeState.append(j)
			while activeState:
				i+=1
				newState=activeState.pop()
				explored.add(newState)
				allChildern=chess.findNextMove(newState)
				allChildern=list(set(allChildern).difference(explored))
				if len(allChildern)==0:
					print("exhausted",i)
					break	
				scores=[]
				for child in allChildern:
					noOfPossibleSteps=chess.findNextMove(child)
					number=len(set(noOfPossibleSteps).difference(explored))
					scores.append(number)



				newState=allChildern[scores.index(max(scores))]
				print(newState)
				activeState.append(newState)

			

		








			# find possible moves



	




main()