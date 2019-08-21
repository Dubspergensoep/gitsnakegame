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

#initializing Pygame
pygame.init()
size=width, heigth=GameSize*TileSize, GameSize*TileSize
screen = pygame.display.set_mode(size)



#Run game
print("game starts running")
while 1:
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

	#keys=pygame.key.get_pressed()
	#if keys[pygame.K_LEFT]:
	#	SnakeGame.ChangeDirection("l")
	#	keys=pygame.key.get_pressed()
	#elif keys[pygame.K_RIGHT]:
	#	SnakeGame.ChangeDirection("r")
	#	keys=pygame.key.get_pressed()
	#elif keys[pygame.K_UP]:
	#	SnakeGame.ChangeDirection("u")
	#	keys=pygame.key.get_pressed()
	#elif keys[pygame.K_DOWN]:
	#	SnakeGame.ChangeDirection("d")
	#	keys=pygame.key.get_pressed()

            			
	#update snake game
	SnakeGame.Update()
	SnakeArr=SnakeGame.GetSnakeArray()

	#drawing snakeGame
	screen.fill(BackgroundColor)
	for snakepart in SnakeArr:
		pygame.draw.rect(screen,SnakeColor,(snakepart[0]*TileSize,snakepart[1]*TileSize,TileSize,TileSize))
	Apple=SnakeGame.GetApple()
	pygame.draw.rect(screen,AppleColor,(Apple[0]*TileSize,Apple[1]*TileSize,TileSize,TileSize))
	pygame.display.flip()
	
	#Waiting
	pygame.time.wait(WaitingTime)
	
	



