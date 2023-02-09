import XMLParse
import re

testStr = """
<a></a>
<asdf><dd>사    업     보    고    서</dd></asdf>
<TITLE ATOC="Y">I. 나는 열심히 합니다</TITLE>
"""

attrPattern = re.compile(r' ([^=]+)=("[^"]+")')
rddSpace = re.compile(r' {2,}')

def convert(string):
    resDict = dict()
    resDict['title'] = "NULL"
    resDict['companyName'] = "NULL"
    
    def matchToHTML(match):
        tag = match.group(1)
        rawAttr = match.group(2)
        innerText = match.group(3)

        if tag in ('COLGROUP', 'COL', 'TABLE', 'THEAD', 'TR', 'TH', 'TBODY', 'TD', 'TE', 'TU'):
            if tag in ('TU', 'TE'): # Converting invalid XML tag into valid HTML tag
                tag = 'TD'
            convertedAttr = ""
            if rawAttr is not None:
                for attrMatch in attrPattern.finditer(rawAttr):
                    att = attrMatch.group(1)
                    val = attrMatch.group(2)

                    # Process of converting xml att to html att (have to add if needed)

                    if att in ('ROWSPAN', 'COLSPAN'):
                        convertedAttr += " {}={}".format(att, val)
            return "<{}{}>{}</{}>\n".format(tag, convertedAttr, stringToHTML(innerText), tag)
        
        if innerText == "": return ""

        # Parse XML content
        if tag == "BODY":
            tag = 'div class="container"'
        elif tag == "DOCUMENT-NAME":
            tag = 'div class="documentName"'
            resDict['title'] = innerText
        elif tag == "COMPANY-NAME":
            tag = 'div class="companyName"'
            resDict['companyName'] = innerText
        elif tag == 'COVER' or tag == 'SECTION-1':
            tag = 'div class="splitPoint"'
        else: tag = 'div'

        return "<{}>{}</{}>\n".format(tag, stringToHTML(innerText), tag)
        
    def stringToHTML(string):
        res = ""
        for match in XMLParse.XMLIter(string):
            # print(match.group(0))
            res += matchToHTML(match)
        if res == "":
            return re.sub(rddSpace, '', string) # Remove redundant spaces
        return res
    
    resDict['html'] = stringToHTML(string)
    return resDict

# print(convert(testStr))