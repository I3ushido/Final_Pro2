# "x" - Create - will create a file, returns an error if the file exist
#
# "a" - Append - will create a file if the specified file does not exist
#
# "w" - Write - will create a file if the specified file does not exist

#f = open("myfile.txt", "x") #create Textfile
import datetime

import datetime
def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)
with open(timeStamped('.txt'),'w') as outf:
    outf.write('data!')



x = datetime.datetime.now()
z = x.strftime("%X")
print(z)
file = z+".txt"
print(file)
f = open(file, "x")
f.write("Data ")
f.close()