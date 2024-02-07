import pygame as pg

class Tile:
	def __init__(self, screen, pos:tuple, is_mine:bool=False):
		# Tile Attr
		self.pos = pos
		self.is_mine = is_mine
		self.surrounding = None
		# Graphic Attr
		self.screen = screen
		self.size = None
		self.color = None
	
	def draw(self):
		pg.draw.rect(self.screen, self.color, self.pos + self.size)