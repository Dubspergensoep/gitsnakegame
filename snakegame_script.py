import snake as sn
import numpy as np
import pygame, sys

#Game variables
GameSize=17 #same size as google snake game
TileSize=30
SnakeColor=(0, 255, 0) #green
AppleColor=(255,0,0)#red
BackgroundColor=(0, 0, 0) #black
WaitingTime=200 #in ms
ClearCountMax=10
ClearCount=0

#intializing Snake
SnakeGame=sn.Snake(GameSize)

# dataset variables
snakehistory = np.array([])
directionhistory = np.array([])

#initializing Pygame
pygame.init()
size=width, heigth=GameSize*TileSize, GameSize*TileSize
screen = pygame.display.set_mode(size)

#Run game
print("game starts running")
while SnakeGame.SnakeAlive:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN	and event.key==pygame.K_UP:
			SnakeGame.ChangeDirection("u")
		elif event.type==pygame.KEYDOWN	and event.key==pygame.K_DOWN:
			SnakeGame.ChangeDirection("d")
		elif event.type==pygame.KEYDOWN	and event.key==pygame.K_RIGHT:
			SnakeGame.ChangeDirection("r")
		elif event.type==pygame.KEYDOWN	and event.key==pygame.K_LEFT:
			SnakeGame.ChangeDirection("l")
            			
	#update snake game
	SnakeGame.Update()
	SnakeArr=SnakeGame.GetSnakeArray()

	# Save game data
	snakehistory = np.append(snakehistory,SnakeGame.snakeArr)
	directionhistory = np.append(directionhistory,SnakeGame.GetDir())
	print([SnakeGame.snakeArr,SnakeGame.GetDir()])


	#drawing snakeGame
	screen.fill(BackgroundColor)
	for snakepart in SnakeArr:
		pygame.draw.rect(screen,SnakeColor,(snakepart[0]*TileSize,snakepart[1]*TileSize,TileSize,TileSize))
	Apple=SnakeGame.GetApple()
	pygame.draw.rect(screen,AppleColor,(Apple[0]*TileSize,Apple[1]*TileSize,TileSize,TileSize))
	pygame.display.flip()
	
	#Waiting
	pygame.time.wait(WaitingTime)

print(snakehistory[-10:-1])
sys.exit()



