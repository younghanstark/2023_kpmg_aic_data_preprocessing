import os
import XMLToHTML
import compressHTML


def preprocessData(fileName):
    try:
        resDict = XMLToHTML.XMLToHTML(fileName, 'euc-kr')
    except:
        resDict = XMLToHTML.XMLToHTML(fileName, 'utf-8')
    
    soup = compressHTML.compressHTML(resDict['html'])
    
    count = 0
    for i in soup.findAll('div', {'class': 'splitPoint'}):
        with open('../preprocessed_datas/' + "{}_{}_{}_{}_{}".format(resDict['companyName'], resDict['title'], resDict['start'], resDict['end'], count) + ".html", 'w') as f:
            f.write(str(i))
        count += 1


if __name__ == "__main__":
    import time
    import datetime

    start = time.time()

    fileList = os.listdir('../datas/kic')
    fileCount = len(fileList)
    currentCount = 0
    errorCount = 0
    errorList = []
    for fileName in fileList:
        try:
            preprocessData(fileName)
        except:
            errorCount += 1
            print("An error occured while processing", fileName)
            errorList.append(fileName)
        currentCount += 1
        print("Progress: {}%({}/{}), Error: {}%({}/{})".format(currentCount / fileCount * 100, currentCount, fileCount, errorCount / fileCount * 100, errorCount, fileCount))

    print("Files with error while processing:", errorList)

    end = time.time()

    sec = (end - start)
    est = datetime.timedelta(seconds=sec)
    print("Execution time:", str(est).split(".")[0])