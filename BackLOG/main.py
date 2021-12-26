import csv

class file_handling_csv:

    def __init__(self, file_name):
        self.name = file_name

    def  write_data(self):
        work_file = open(self.name, 'a', newline='')
        writing = csv.writer(work_file, delimiter=',')
        print('Code,:,Name,:,LectToDO,:,Lec From To(L1 L2)')
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
            for word in line:
                print(word, end=' ')
            print('')
        work_file.close()

main_file = file_handling_csv('D:\\git repository\\thenikhilsharma_python\\BackLOG\\data.csv')
phy_file = file_handling_csv('D:\\git repository\\thenikhilsharma_python\\BackLOG\\sub_phy.csv')
chem_file = file_handling_csv('D:\\git repository\\thenikhilsharma_python\\BackLOG\\sub_chem.csv')
maths_file = file_handling_csv('D:\\git repository\\thenikhilsharma_python\\BackLOG\\sub_maths.csv')

while True:
    cmd = input()
    if cmd == 'display main': main_file.read_data()
    elif cmd == 'exit': break
    elif cmd == 'show phy': phy_file.read_data()
    elif cmd == 'show chem': chem_file.read_data()
    elif cmd == 'show maths': maths_file.read_data()
    elif cmd == 'add data':
        sub = input("select file as phy_file, chem_file, maths_file: ")
        if sub == 'phy_file':
            phy_file.read_data()#reading and writing data
            phy_file.write_data()#reading and writing data
        elif sub == 'chem_file':
            chem_file.read_data()#reading and writing data
            chem_file.write_data()
        elif sub == 'maths_file':
            maths_file.read_data()
            maths_file.write_data()