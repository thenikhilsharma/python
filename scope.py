class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        amax = int(max(self.__elements))
        amin = int(min(self.__elements))
        self.maximumDifference = amax - amin
        return self.maximumDifference
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)