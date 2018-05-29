class Circle:
	'''a simple class for creating Circle objects '''
	def __str__(self):
		return "object from Circle class"

	def __init__(self,x,y,radius):
		self.x = x
		self.y = y
		self.radius = radius

	def add_x(self,n):
		self.x += n
		return self.x

	def add_y(self,n):
		self.y += n
		return self.y

	def add_radius(self,n):
		self.radius += n
		return self.radius


circ = Circle(0,0,1)
circ2 = Circle(1,1,5)

circ2.add_x(25)
print(circ2.x)

print(circ)
circ.add_y(3)
circ.add_x(4)
circ.add_radius(5)

print(circ.x)
print(circ.y)
print(circ.radius)
