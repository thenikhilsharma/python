import SelectionSort
import BubbleSort
import InsertionSort

#8 4 1 5 9 2
inp1 = list(map(int, input('Input array: ').split()))
inp2 = list(map(int, input('Input array: ').split()))
inp3 = list(map(int, input('Input array: ').split()))

print(SelectionSort.Sort(inp1))
print(BubbleSort.Sort(inp2))
print(InsertionSort.Sort(inp3))