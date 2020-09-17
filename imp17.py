def capitalise():
    file = open('/home/kain/Documents/data.txt','r')
    file2 = open('/home/kain/Documents/text1.txt','a')
    for i in file:
        s = i.split('.')
        s1 = str(s)
        new_s = s1.capitalize()
        print(file2.write(new_s))
    file.close()
    file2.close()