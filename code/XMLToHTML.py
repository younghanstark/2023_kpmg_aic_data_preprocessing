import toHTML

baseHTML = """<!DOCTYPE html>
<head>
<title>report</title>
<style>
table, th, td {
    border: 1px solid;
}
</style>
</head>
<body>
"""

def preprocessXML(XMLFileName):
    XMLFilePath = "../datas/kic/" + XMLFileName

    with open(XMLFilePath, 'r') as f:
        XMLData = f.read()
        XMLData = XMLData.split('\n', maxsplit=1)[1] # Trimming <?xml version="1.0" encoding="utf-8"?>
        XMLData = XMLData.replace('&cr;', '<br />') # Replacing unvalid carriage returns with valid ones

    HTMLFilePath = "../preprocessed_datas/" + XMLFileName.replace('.xml', '.html')
    with open(HTMLFilePath, 'w') as f:
        f.write(baseHTML)
        f.write(toHTML.stringToHTML(XMLData))
        f.write('</body>')

if __name__ == "__main__":
    import sys
    argFileName = sys.argv[1]
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    preprocessXML(argFileName)