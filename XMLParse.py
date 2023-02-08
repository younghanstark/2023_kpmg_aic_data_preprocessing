import re

testStr = """"""

pattern = re.compile(r'<([^ >]+)( [^>]+)?>([\s\S]*?)<\/\1>')

def XMLIter(string):
    # Example usage
    # for match in XMLIter(test_str):
    #   print("Tag: {}, Attr: {}, Text: {}".format(match.group(1), match.group(2), match.group(3)))
    return pattern.finditer(string)
