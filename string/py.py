st = input("This is a string input guys enter something\n")
st_len = print("Length of your entered text is : ", len(st))

fndspaces = st.find("  ", 0 , st_len)
x = range(0,100,fndspaces)
for i in x:
    st = st.replace("  ", " ")
print("Your text without Spaces looks like this",st)

further_spaces_del = input("Do you want to delete further spaces (Y/N) ")

further_spaces_del_range = range(0,5,len(st))
if further_spaces_del == "Y":
    for j in further_spaces_del_range:
        st = st.replace("   ", " ")
    print(st)
else:
    print("You are damn straight forward")

fnd_string = input("Which Word do you want to find\n")
print(st.find(fnd_string)+1)

replace_confirmation = input("Do you want to replace Y/N")

if replace_confirmation == "Y":
    replaced_word = input("Enter a word to replace: ")
    replaced_sentence = st.replace(fnd_string, replaced_word)
    print(replaced_sentence)
elif replace_confirmation == "N":
    print(st)

save_confirmation = input("Do you want to save this file (Y/N) ")
if save_confirmation == "Y":
    file1 = open("D:\\textFILE","w")
    file1.write(replaced_sentence)
    file1.close()
else:
    print("Really ;)")