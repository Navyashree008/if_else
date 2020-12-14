my_file = open("file_q3.txt")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("oher.txt","w")
# file_data = my_file.read()
# print (file_data)
for data in my_file:
    if "delhi" in data:
        file1.write(data)
    elif "shimla" in data:
        file2.write(data)
    else:
        file3.write(data)
file1.close()