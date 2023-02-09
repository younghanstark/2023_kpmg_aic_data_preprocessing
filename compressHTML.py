from bs4 import BeautifulSoup

def compressHTML(html_object):
    soup = BeautifulSoup(html_object, "lxml")

    for x in soup.find_all():
        if len(x.get_text(strip=True)) == 0 and x.name not in ['colgroup', 'col', 'table', 'thead', 'tr', 'th', 'tbody', 'td', 'br', 'img']:
            x.extract()

    return soup

if __name__ == "__main__":
    import sys
    argFileName = sys.argv[1]
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    with open("../" + argFileName, 'r') as f:
        with open("../" + argFileName.replace('.html', '_n.html'), 'w') as g:
            g.write(str(compressHTML(f)))