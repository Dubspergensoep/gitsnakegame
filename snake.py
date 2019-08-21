import numpy as np
import random as rand
class Snake:
	def __init__(self, size):
		self.size = size
		#initializing board
		self.board = np.zeros((size,size))
		#adding snake array
		self.snakeArr= np.array([[self.size//4+1, self.size//2], [self.size//4, self.size//2], [self.size//4-1, self.size//2]])
		print(self.snakeArr)
		#intialize direction
		self.direction=[1, 0]
		#add apple
		self.apple=[rand.randint(0,self.size-1),rand.randint(0,self.size-1)]
		#intialize gamestate to true if game state false -> game over
		self.SnakeAlive=True 
		self.score=0		
	
	def PrintBoard(self):
		board = np.zeros((self.size,self.size))
		print(board)
		for coord in self.snakeArr:
			board[coord[0]][coord[1]]=1
		print(board)

	def Update(self):
		if(self.SnakeAlive):
			#Update snake position
			self.snakeArr=np.concatenate(([self.snakeArr[0]+self.direction], self.snakeArr), axis=0)
			#Check if snake died
			if self.snakeArr[0, 0]<0 or self.snakeArr[0, 0]>=self.size or self.snakeArr[0, 1]<0 or self.snakeArr[0, 1]>=self.size:
				self.SnakeAlive=False
				print("GAME OVER!!!")
			if (np.unique(self.snakeArr,axis=0)).shape!=(self.snakeArr).shape:
				self.SnakeAlive=False
				print("GAME OVER!!!")
			#Check if snake eats apple
			if self.snakeArr[0, 0]==self.apple[0] and self.snakeArr[0, 1]==self.apple[1]:
				self.score+=1
				print("Your Score is : ", self.score)
				self.NewApple()
			else:
				self.snakeArr=np.delete(self.snakeArr,-1,0)
			

			

	def GetGameState(self):
		return self.SnakeAlive

	def GetSnakeArray(self):
		return self.snakeArr

	def GetApple(self):
		return self.apple

	def ChangeDirection(self,Dir):
		if Dir=="u" and self.direction != [0, 1]:
			self.direction=[0, -1]
		elif Dir=="d" and self.direction != [0, -1]:
			self.direction=[0, 1]
		elif Dir=="r" and self.direction != [-1, 0]:
			self.direction=[1, 0]
		elif Dir=="l" and self.direction != [1, 0]:
			self.direction=[-1, 0]
	
	def NewApple(self):
		self.apple=[rand.randint(0,self.size-1),rand.randint(0,self.size-1)]
		for part in self.snakeArr:
			if part[0]==self.apple[0] and part[1]==self.apple[1]:
				self.NewApple()
				break
		
				

			
	
