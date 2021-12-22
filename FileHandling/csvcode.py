import csv

def write_csv(L):
    f = open('list.csv', 'w', newline='')
    w = csv.writer(f, delimiter=',')
    for i in L:
        w.writerow(i)
    f.close()

def read_csv():
    f = open('list.csv', 'r')
    r = csv.reader(f, delimiter=',')
    for i in r:
        print(i)
    f.close()

L = []
n = int(input("Enter num of values: "))
for i in range(n):
    inp = list(input("Enter value: ").split())
    L.append(inp)

write_csv(L)
read_csv()