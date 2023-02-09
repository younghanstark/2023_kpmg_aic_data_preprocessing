import XMLParse
import re

testStr = """
<TD WIDTH="150" HEIGHT="30" VALIGN="MIDDLE" ALIGN="CENTER" USERMARK=" BC0XD7D7D7 B">제44기</TD>
"""

attrPattern = re.compile(r' ([^=]+)=("[^"]+")')

def convert(string):
    title = ""
    companyName = ""
    def matchToHTML(match):
        tag = match.group(1)
        rawAttr = match.group(2)
        innerText = match.group(3)

        if tag in ('COLGROUP', 'COL'): return ""

        if tag in ('TABLE', 'THEAD', 'TR', 'TH', 'TBODY', 'TD', 'TE', 'TU'):
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

        if tag == "DOCUMENT-NAME":
            tag = 'h1'
            nonlocal title
            title = innerText
        elif tag == "COMPANY-NAME":
            tag = 'h2'
            nonlocal companyName
            companyName = innerText
        else: tag = 'div'

        return "<{}>{}</{}>\n".format(tag, stringToHTML(innerText), tag)
        
    def stringToHTML(string):
        res = ""
        for match in XMLParse.XMLIter(string):
            # print(match.group(0))
            res += matchToHTML(match)
        if res == "": return string
        return res
    return (stringToHTML(string), title, companyName)

# print(stringToHTML(testStr))