#!/usr/bin/python

import pprint
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

urlhost = 'http://www.hrzz.hr'

urlpath = 'default.aspx?id=78&search=yes'

url = urlhost + "/" + urlpath

response = br.open(url)

#
# FOLLOW BY PAGINATION
#
#for link in br.links(url_regex='page',nr=1):
#    print link.text, link.url

link1 = br.find_link(url_regex='page',nr=1)

print (link1.url)

response = br.open(urlhost + '/' + link1.url)

link2 = br.find_link(url_regex='id=78&pid=',nr=1)


response = br.open(urlhost + '/' + link2.url)

html_doc = response.read()


soup = BeautifulSoup(html_doc)

ptitle = soup.select('.page_content > strong > span')
project_title = ptitle[0].findAll(text=True)
print str(project_title) + "\n"

phead = soup.select('.page_content > table:nth-of-type(1) > tr:nth-of-type(2) > td:nth-of-type(1)')
project_head = phead[0].findAll(text=True)
print str(project_head) + "\n"

ptype = soup.select('.page_content > table:nth-of-type(1) > tr:nth-of-type(2) > td:nth-of-type(2)')
project_type = ptype[0].findAll(text=True)
print str(project_type) + "\n"

pcall = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
project_call = pcall[0].findAll(text=True)
print str(project_call) + "\n"

pcode = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)')
project_code = pcode[0].findAll(text=True)
print str(project_code) + "\n"

pacro = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(3)')
project_acro = pacro[0].findAll(text=True)
print str(project_acro) + "\n"

pdura = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(4)')
project_dura = pdura[0].findAll(text=True)
print str(project_dura) + "\n"

pstatus = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(5)')
project_status = pstatus[0].findAll(text=True)
print str(project_status) + "\n"

pval = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(6)')
project_val = pval[0].findAll(text=True)
print str(project_val) + "\n"


for node in soup.findAll('strong'): 
  if node.next.endswith('Rok:'):
#texts.append(node.next)
    pprint.pprint(node.next)



pdet = soup.select('.page_content')
project_det = pdet[0].findAll(text=True)


#output = []
#output += [project_det[3], project_det[6], project_det[7], project_det[14], project_det[15], project_det[16], project_det[17], project_det[18]]  

#pprint.pprint(output)

#################################################################################

# REGEX

# dataPattern = re.compile(r"<td>[a-zA-Z]+</td>... etc.")
# match = dataPattern.find(htmlstring)
# field1 = match.group(1)
# field2 = match.group(2)



#help(br.links)


# br.follow_link takes either a Link object or a keyword arg (such as nr=0).

# br.links() lists all the links.

# br.links(url_regex='...') lists all the links whose urls matches the regex.

# br.links(text_regex='...') lists all the links whose link text matches the regex.

# br.follow_link(nr=num) follows the numth link on the page, with counting starting at 0. It returns a response object (the same kind what br.open(...) returns)

# br.find_link(url='...') returns the Link object whose url exactly equals the given url.

# br.find_link, br.links, br.follow_link, br.click_link all accept the same keywords. Run help(br.find_link) to see documentation on those keywords.


# response = br.open(url)
# print response.read()

# SOUP

#soup = BeautifulSoup(html_doc)

#print soup.getText()



# SELECTORS

#pprint(soup.select(".sister")) # select by class
#pprint(soup.select("#link1")) # select by id
#pprint(soup.select('a[href="http://example.com/elsie"]')) 
# find tags by attribute value
#pprint(soup.select('a[href^="http://example.com/"]'))
# find tags by attribute value, all contains 'http://example.com/'
#pprint(soup.select('p[lang|=en]')) # Match language codes
 

#print [elm.span.text for elm in soup.findAll('div', {'class': 'title'})]

##
