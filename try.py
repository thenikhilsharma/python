class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):

        mx = int(max(a))
        diff_arr = []

        for i in range(len(a)):
            diff = int(a[i]) - mx
            diff_arr.append(diff)

        mix = []

        num = diff_arr
        for i in num:
            if i < 0:
                i = -i
            mix.append(i)
        return mix

    def maximumDifference():
        return max(mix)

# End of Difference class

n = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)