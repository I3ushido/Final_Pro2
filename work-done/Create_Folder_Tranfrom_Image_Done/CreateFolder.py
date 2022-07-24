import os


Folder = 4

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def createFolder_Dataset(directory,TotalFolder):
    # print('directory : ' + directory + ' TotalFolder : ' + TotalFolder)
    i = 1
    while i <= TotalFolder:
        try:
            if not os.path.exists(directory):                
                os.makedirs(directory+str(i))
                print(directory+str(i))
        except OSError:
            print ('Error: Creating directory. ' +  directory)
        i+=1

    print(TotalFolder)


##createFolder_Dataset('Pre_Dataset/Out',Folder)
createFolder_Dataset('./Out',Folder)






