import csv, pickle

class file_handling_csv:

    def __init__(self, file_name):
        self.name = file_name

    def  write_data(self):
        work_file = open(self.name, 'w', newline='')
        writing = csv.writer(work_file, delimiter=',')
        while True:
            data = list(input("Enter data for rows: ").split())
            if data[0] != 'break':
                writing.writerow(data)
            else: break
        work_file.close()

    def read_data(self):
        work_file = open(self.name, 'r')
        reading = csv.reader(work_file, delimiter=',')
        for line in reading:
            print(line)
        work_file.close()

class file_handling_binary:

    def __init__(self, file_name):
        self.name = file_name
    
    def write_data(self):
        work_file = open(self.name, 'wb')
        print('type break to exit')
        print('Enter your data: ', end='')
        data_to_enter = []
        while True:
            data = list(input().split())
            if data[0] == "break": break
            else: data_to_enter.append(data)
        pickle.dump(data_to_enter, work_file)
        work_file.close()
    
    def read_data(self):
        work_file = open(self.name, 'rb')
        reading = pickle.load(work_file)
        for line in reading:
            for word in line:
                print(word, end=' | ')
            print('')
        work_file.close()

class file_handling_text:

    def __init__(self, file_name):
        self.name = file_name
    
    def write_data(self):
        work_file = open(self.name, 'w')
        print('type break to exit')
        print('enter ur data: ', end='')
        while True:
            data = input()
            if data != 'break':
                work_file.write(data)
            else: break
        work_file.close()
    
    def read_data(self):
        work_file = open(self.name, 'r')
        print(work_file.read())
        work_file.close


file_name = input("Enter name of file (with extension): ")   #file name

extension = file_name.split('.')
if extension[1] == 'csv':
    file_class = file_handling_csv(file_name)
elif extension[1] == 'dat':
    file_class = file_handling_binary(file_name)
elif extension[1] == 'txt':
    file_class = file_handling_text(file_name)

action = input("ACTION | read or write (read/write, r/w)| : ")
if action == 'write' or action == 'w': file_class.write_data()
elif action == 'read' or action == 'r': file_class.read_data()