class Tile:
	def __init__(self, pos, is_mine=False):
		# Tile Attr
		self.pos = pos
		self.is_mine = is_mine
		self.surrounding = None
		# Graphic Attr
		self.size = None
		self.color = None
	
	def draw(self):
		pass