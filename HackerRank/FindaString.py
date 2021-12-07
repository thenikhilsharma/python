#by Nikhil Sharma on 27 NOV 2021 @ 6:30pm
#hackerrank
#solved
def count_substring(string, sub_string):
    # Find a string in Python - Hacker Rank Solution START
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count
    # Find a string in Python - HackerRank Solution END
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
'''
def count_substring(string, sub_string):
    search = sub_string

    l = len(string)
    n = 0

    j = string.index(search)
    string = string[j::]

    for i in range(0,len(string),len(search)-1):
        arr = string[i:l]
        a = arr.count(search)
        n = a+n

    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)'''