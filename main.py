import pygame
import json


class Game:
	def __init__(self):
		# Game Settings
		with open("./fixtures/settings.json") as file:
			self.settings = json.load(file)
		self.screen = pygame.display.set_mode((self.settings["display"]["x"], 
										 	   self.settings["display"]["y"]))

	def run(self):
		while True:
			self.screen.fill(self.settings["display"]["color"])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
			pygame.display.update()


if __name__ == "__main__":
	minesweeper = Game()
	minesweeper.run()