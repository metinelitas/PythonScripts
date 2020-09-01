import requests
from bs4 import BeautifulSoup
import codecs
import sys

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

link = 'https://www.sahibinden.com/alt-kategori/motosiklet'
link = 'https://www.sahibinden.com/alt-kategori/otomobil'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r = codecs.open("C:\\home\\personalProjects\\sah\\say.html", 'r', 'utf-8')
# soup = BeautifulSoup(r, 'html.parser')

r = requests.get(link,timeout=1,headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

listtt = []

def takeSecond(elem):
    return int(elem.count)

class Arac:
  def __init__(self, name, count):
    self.name = name
    self.count = count

for x in soup.find_all('span'):
    if (x.parent.name == 'div'):
        vechileCountRaw = x.parent.span.string
        vechileBrand = x.parent.a.string

        if (vechileCountRaw is not None ) and (vechileBrand is not None):
            vechileCount = vechileCountRaw.replace('(','').replace(')','').replace('.','')
            print('Brand: ' +  vechileBrand + '       Count: ' + vechileCount)
            listtt.append(Arac(str(vechileBrand),str(vechileCount)))

 # Create table
fileout = open("html-table.html", "w", encoding="utf-8")

table = r'<meta charset="UTF-8">'
table += "<table>\n"

# Create the table's column headers
table += "  <tr>\n"
table += "    <th>{0}</th>\n".format('Marka')
table += "    <th>{0}</th>\n".format('Adet')
table += "  </tr>\n"

listtt.sort(key=takeSecond,reverse=True)

for vech in listtt:
    table += "  <tr>\n"
    table += "    <td>{0}</td>\n".format(vech.name)
    table += "    <td>{0}</td>\n".format(vech.count)
    table += "  </tr>\n"

table += "</table>"

fileout.writelines(table)
fileout.close()