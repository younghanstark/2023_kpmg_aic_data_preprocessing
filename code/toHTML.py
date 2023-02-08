import XMLParse
import re

testStr = """
<TD WIDTH="150" HEIGHT="30" VALIGN="MIDDLE" ALIGN="CENTER" USERMARK=" BC0XD7D7D7 B">제44기</TD>
"""

attrPattern = re.compile(r' ([^=]+)=("[^"]+")')

def matchToHTML(match):
    tag = match.group(1)
    rawAttr = match.group(2)
    innerText = match.group(3)

    if tag in ('TABLE', 'COLGROUP' , 'COL', 'THEAD', 'TR', 'TH', 'TBODY', 'TD', 'TE', 'TU'):
        if tag in ('TU', 'TE'): # Converting invalid XML tag into valid HTML tag
            tag = 'td'
        convertedAttr = ""
        if rawAttr is not None:
            for attrMatch in attrPattern.finditer(rawAttr):
                att = attrMatch.group(1)
                val = attrMatch.group(2)

                # Process of converting xml att to html att (have to add if needed)

                if att in ('ROWSPAN', 'COLSPAN'):
                    convertedAttr += " {}={}".format(att, val)
        return "<{}{}>{}</{}>\n".format(tag, convertedAttr, stringToHTML(innerText), tag)
    
    return "<{}>{}</{}>\n".format('div', stringToHTML(innerText), 'div')
    
def stringToHTML(string):
    res = ""
    for match in XMLParse.XMLIter(string):
        # print(match.group(0))
        res += matchToHTML(match)
    if res == "": return string
    return res

# print(stringToHTML(testStr))