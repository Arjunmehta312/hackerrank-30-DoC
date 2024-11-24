class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        # Finding the maximum and minimum elements in the array
        max_element = max(self.__elements)
        min_element = min(self.__elements)
        # Calculating the maximum absolute difference
        self.maximumDifference = max_element - min_element

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)