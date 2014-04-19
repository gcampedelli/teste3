import scraperwiki
import requests 

html = requests.get("https://www.secom.planalto.gov.br/consea/boletins.nsf/01ContatoxNome?OpenView&Start=1", verify=False).content

import lxml.html
root = lxml.html.fromstring(html)
table=root.cssselect('table')[1]
for td in table:
        data={
                'nome': table[0].text_content(),
                'email': table[2].text_content(),
        }

print data
