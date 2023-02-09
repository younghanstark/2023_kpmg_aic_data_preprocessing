import toHTML
import re

datePattern = re.compile(r'AUNIT="PERIOD[^"]+" AUNITVALUE="([0-9]+)"')

def XMLToHTML(XMLFileName, reqEncoding):
    XMLFilePath = "../datas/kic/" + XMLFileName

    dateDict = dict()
    with open(XMLFilePath, 'r', encoding=reqEncoding) as f:
        XMLData = f.read()
        XMLData = XMLData.split('\n', maxsplit=1)[1] # Trimming <?xml version="1.0" encoding="utf-8"?>
        XMLData = XMLData.replace('&cr;', '<br />') # Replacing unvalid carriage returns with valid ones
        dates = re.findall(datePattern, XMLData)
        dateDict['start'] = dates[0]
        dateDict['end'] = dates[1]
    
    return dict(toHTML.convert(XMLData), **dateDict)

if __name__ == "__main__":
    import sys
    argFileName = sys.argv[1]
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    with open("../" + argFileName.replace('.xml', '.html'), 'w') as f:
        try:
            resDict = XMLToHTML(argFileName, 'euc-kr')
        except:
            resDict = XMLToHTML(argFileName, 'utf-8')
        f.write(resDict['html'])