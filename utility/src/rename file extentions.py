# e.g rename file with extension .cpp to .txt
import sys
import os
import glob

cppFiles = glob.glob('/Users/ezhou/Google Drive/algorithm/cpp2 copy/*')
# print cppFiles
# sys.exit()

for oldFileName in cppFiles:
    print "processing", oldFileName
    # sys.exit()
    newFileName = oldFileName.replace('.cpp', '.txt')
    output = os.rename(oldFileName, newFileName)