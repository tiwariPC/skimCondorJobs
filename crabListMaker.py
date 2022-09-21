import os,sys
#coded by Deepak
'''
    For the given path, get the List of all files in the directory tree
    python Crab_ListMaker.py inputpath outputFolder
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def main(dirName):
    print ("******STARTING**********")
    pref="root://eoscms.cern.ch/"
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        if 'failed' in dirpath:continue
        if 'log' in dirpath:continue
        if not dirnames or dirnames[0]=='failed' or dirnames[0]=='log':
            dataSetName = dirpath.split('/')[-4]
            print ('dirpath',dirpath)
            fout = open(outDir+'/'+str(dataSetName)+'.txt','a')
            [fout.write(pref+dirpath+'/'+filename+'\n') for filename in filenames]
            listOfFiles += [os.path.join(dirpath, file) for file in filenames if '.root' in file]
    fileout='combined.txt'
    Fout=open(fileout,'w')
    for elem in listOfFiles:
        #print(elem)
        #if 'failed' not in elem:
        Fout.write(elem+'\n')
    print ("========DONE=========")


if __name__ == '__main__':
    path = sys.argv[1]
    outDir = 'Filelists_'+sys.argv[2]
    os.system('rm -rf '+outDir)
    os.system('mkdir '+outDir)
    os.system('rm -rf '+outDir+'/*')
    main(path)
