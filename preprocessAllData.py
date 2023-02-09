import os
import XMLToHTML

fileList = os.listdir('../datas/kic')
fileCount = len(fileList)
currentCount = 0
errorCount = 0
errorList = []
for fileName in fileList:
    try:
        try:
            XMLToHTML.preprocessXML(fileName, 'euc-kr')
        except:
            XMLToHTML.preprocessXML(fileName, 'utf-8')
    except:
        errorCount += 1
        print("An error occured while processing", fileName)
        errorList.append(fileName)
    currentCount += 1
    print("Progress: {}%({}/{}), Error: {}%({}/{})".format(currentCount / fileCount * 100, currentCount, fileCount, errorCount / fileCount * 100, errorCount, fileCount))

print("Files with error while processing:", errorList)