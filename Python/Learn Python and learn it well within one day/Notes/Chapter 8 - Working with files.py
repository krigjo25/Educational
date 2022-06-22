'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                           Chapter 8 - Working with files

8.1 Openning & Reading Text Files
    
    Modes :
        r   - Read Only,
        r+  - for read and write
        w   - Write Only,
                - If the specified file does not exist, it will be created, 
                otherwise the previous data will be erased

        a   - appending text
                -   if the specified file does not exist it will be created,
                    otherwise any data will be added to the end of the file
        
    
    built-in
        f = open('path to txt file','mode')
        f.readline() - Reads only one line
        f.readlines() - reads everything ( using for i in f print(i)) is an alternative way
        f.write() - writes in to the document
        read() - reads the document
        remove(file)
        rename(old|new)

8.3 Writing text to files

8.4 Opening and Reading Text Files by Buffer Size

8.5 Opening, Reading and Writing Binary Files
    Binary files refer to any file which is non-text e.g (img / video)

    Modes
        rb - Read binary
        wb - write binary

8.6 Rename & Delete Files

'''
f = open('D:\\Jottacloud\\Educational\\Programming\\Python\\Learn Python and learn it well within one day\\lib\\demo\\demo.txt', 'r')
for i in f:
    print("8.1 Opening & Reading files\n", i, end ='')
f.close()

f = open('D:\\Jottacloud\\Educational\\Programming\\Python\\Learn Python and learn it well within one day\\lib\\demo\\demo.txt', 'a')
f.write("\n\n8.3 Writing text to files \nPython is fun !")
f.close()

r = open('D:\\Jottacloud\\Educational\\Programming\\Python\\Learn Python and learn it well within one day\\lib\\demo\\demo.txt', 'r')
w = open('D:\\Jottacloud\\Educational\\Programming\\Python\\Learn Python and learn it well within one day\\lib\\demo\\opdemo.txt', 'w')
msg = r.read(10)

while len(msg):
    w.write(msg)
    msg = r.read(10)
r.close()
w.close()

r = open('C:\\Users\\krigj\\OneDrive\\Desktop\\france.jpg', 'rb')
w = open('D:\\Jottacloud\\Educational\\Programming\\Python\\Learn Python and learn it well within one day\\lib\\demo\\demopic.jpg', 'wb')
msg = r.read(10)

while len(msg):
    w.write(msg)
    msg = r.read(10)
r.close()
w.close()