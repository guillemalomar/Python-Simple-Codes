import unittest

class TestStringMethods(unittest.TestCase):
	
    def test_types_wrongsize(self):
	    #Here I would make a generator of lists with every size between 1 and 10 and check all work (not enough time)
        self.assertEqual(triangle_analyzer([1,2]), 'A triangle should have 3 sides')
        self.assertEqual(triangle_analyzer([1]), 'A triangle should have 3 sides')
        self.assertEqual(triangle_analyzer([1,2,4,5]), 'A triangle should have 3 sides')

    def test_types_scalene(self):
        self.assertEqual(triangle_analyzer([1,2,3]), 'Scalene Triangle')
        self.assertEqual(triangle_analyzer([4,2,3]), 'Scalene Triangle')
        self.assertEqual(triangle_analyzer([9,2,3]), 'Scalene Triangle')
		
    def test_types_equilateral(self):
        self.assertEqual(triangle_analyzer([1,2,2]), 'Equilateral Triangle')
        self.assertEqual(triangle_analyzer([2,2,1]), 'Equilateral Triangle')
        self.assertEqual(triangle_analyzer([2,1,1]), 'Equilateral Triangle')

    def test_types_isosceles(self):
	    #Here I would make a generator of lists with every number repeated between 1 and 10 and check all work (not enough time)
        self.assertEqual(triangle_analyzer([3,3,3]), 'Isosceles Triangle')
        self.assertEqual(triangle_analyzer([9999,9999,9999]), 'Isosceles Triangle')
        self.assertEqual(triangle_analyzer([30,30,30]), 'Isosceles Triangle')

def triangle_analyzer(sizes):
    if len(sizes) != 3:
        return 'A triangle should have 3 sides'
    equalSides = {}
    for ind1, side1 in enumerate(sizes):
        for ind2, side2 in enumerate(sizes):
            if ind1 != ind2:
                if side1 == side2:
                    if ind1 >= ind2:
	                    equalSides[(ind1,ind2)] = 1
                    else:
		                equalSides[(ind2,ind1)] = 1
    if len(equalSides) == 0:
        return 'Scalene Triangle'
    elif len(equalSides) == 1:
        return 'Equilateral Triangle'
    else:
        return 'Isosceles Triangle'
		
if __name__ == '__main__':
	unittest.main()

