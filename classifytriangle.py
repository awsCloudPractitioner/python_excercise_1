
class ClassifyTriangle:

	def __init__(self, sidelist):
		self.side_a, self.side_b, self.side_c = sidelist

		# side is a float representing the side of a triangle.
		# Passes validation if it is > 0
		# Return error if it is negative

		if any(side_item <= 0.0 for side_item in sidelist):
			raise ValueError("It is an impossible Triangle!")

	@property
	def equilateral(self):
		return self.side_a == self.side_b == self.side_c

	@property
	def isosceles(self):
		return self.side_a == self.side_b or self.side_b == self.side_c or self.side_c == self.side_a

	@property
	def scalene(self):
		return self.side_a != self.side_b and self.side_b != self.side_c and self.side_c != self.side_a


if __name__ == '__main__':

	sides = []
	# Input for all three sides of the triangle
	# Throws exception for invalid number
	for number in range(3):
		try:
			side = float(input("How long is the {number} side of the triangle? ".format(number=number + 1)))
			sides.append(side)
		except ValueError:
			print("Invalid number...")
			raise

	triangle = ClassifyTriangle(sides)

	if triangle.equilateral:
		print("Equilateral and Isosceles triangle (every equilateral triangle is also an isosceles triangle)")

	elif triangle.isosceles:
		print("Isosceles triangle!")

	elif triangle.scalene:
		print("Scalene triangle!")
