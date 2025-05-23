import pygame
from constants import *
from player import Player



def main():
	print(f"Starting Asteroids! \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")


	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x =  SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(BLACK)
		player.draw(screen)
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
	main()
