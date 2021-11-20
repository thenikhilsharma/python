import textwrap

def wrap(string, max_width):
    string = list(string)
    arr = []
    for o in range(len(string)):
        a = (o+max_width)-1
        if a <= len(string):
            arr.append(string[o:a])
        else:
            
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)