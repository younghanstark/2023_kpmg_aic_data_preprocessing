import os
import XMLToHTML
import sys

fileList = os.listdir('../datas/kic')
fileCount = len(fileList)
currentCount = 0
errorCount = 0
errorList = []
for fileName in fileList:
    try:
        XMLToHTML.preprocessXML(fileName)
    except KeyboardInterrupt:
        sys.exit()
    except:
        errorCount += 1
        print("An error occured while processing", fileName)
        errorList.append(fileName)
    currentCount += 1
    print("Progress: ({}/{}), Error: ({}/{})".format(currentCount, fileCount, errorCount, fileCount))

print("Files with error while processing:", errorList)