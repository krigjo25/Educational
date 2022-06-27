'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                           Chapter 8 - Working with files



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