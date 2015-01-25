#!/usr/bin/python

import re
import time
import pprint
import codecs
import mechanize
import urllib2
import logging
from bs4 import BeautifulSoup
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

#
# FUNC
#
def parse ( html_doc ):

	soup = BeautifulSoup(html_doc)
	
	ptitle = soup.select('.page_content > strong > span')
	project_title = ptitle[0].findAll(text=True)
	
	phead = soup.select('.page_content > table:nth-of-type(1) > tr:nth-of-type(2) > td:nth-of-type(1)')
	project_head = phead[0].findAll(text=True)
	
	ptype = soup.select('.page_content > table:nth-of-type(1) > tr:nth-of-type(2) > td:nth-of-type(2)')
	project_type = ptype[0].findAll(text=True)
	
	pcall = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
	project_call = pcall[0].findAll(text=True)
	
	pcode = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)')
	project_code = pcode[0].findAll(text=True)
	
	pacro = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(3)')
	project_acro = pacro[0].findAll(text=True)
	
	pdura = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(4)')
	project_dura = pdura[0].findAll(text=True)
	
	pstatus = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(5)')
	project_status = pstatus[0].findAll(text=True)
	
	pval = soup.select('.page_content > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(6)')
	project_val = pval[0].findAll(text=True)
	
	# REGEX PART
	
	pdet = soup.select('.page_content')
	project_det = pdet[0]
	
	ustanova = re.search("<strong>Institution:<\/strong><br\/>(.*?)<br/>", str(project_det), re.DOTALL)
	#print ustanova.groups()[0]
	
	zn_podrucja = re.search("<strong>Scientific\ fields:<\/strong><br\/>(.*?)<br/>", str(project_det), re.DOTALL)
	#print zn_podrucja.groups()[0]
	
	zn_polja = re.search("<strong>Scientific\ areas:<\/strong><br\/>(.*?)<br/>", str(project_det), re.DOTALL)
	#print zn_polja.groups()[0]
	
	suradnici = re.search("<strong>Members:<\/strong><br\/>(.*?)<br/>", str(project_det), re.DOTALL)
	#print suradnici.groups()[0]
	
	sazetak = re.search("<strong>Abstract:<\/strong><br\/>(.*?)<", str(project_det), re.DOTALL)
	#print sazetak.groups()[0]
	
	keyw = re.search("<strong>Keywords:<\/strong><br\/>(.*?)<br/>", str(project_det), re.DOTALL)
	#print keyw.groups()[0]
	
	if len(project_status)==0: 
		project_status = ['null']
	
	project_line = '|' + project_code[0] + "|\t|" + project_title[0] + "|\t|" + project_head[0] + "|\t|" + project_val[0] + "|\t|" + project_type[0] + "|\t|" + project_call[0] + "|\t|" + project_acro[0] + "|\t|" + project_dura[0] + "|\t|" + project_status[0] + "|\t|" + ustanova.groups()[0] + "|\t|" + zn_polja.groups()[0] + "|\t|" + suradnici.groups()[0] + "|\t|" + sazetak.groups()[0] + "|\t|" + zn_podrucja.groups()[0] + "|\t|" + keyw.groups()[0] + "|"

	project_line = project_line.replace('\n', ' ').replace('\r', '') + "\n"

	return project_line;

#
# MAIN
#

f = codecs.open('out/hrzz.en.out', encoding='utf-8', mode='w+')

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

br1 = mechanize.Browser()
br1.set_handle_robots(False)
br1.set_handle_refresh(False)
br1.addheaders = [('User-agent', 'Firefox')]

br2 = mechanize.Browser()
br2.set_handle_robots(False)
br2.set_handle_refresh(False)
br2.addheaders = [('User-agent', 'Firefox')]


urlhost = 'http://www.hrzz.hr'

urlpath = 'default.aspx?id=1205&search=yes'

url = urlhost + "/" + urlpath

response = br1.open(url)

pages = br1.links(url_regex='page')

for page in pages:

	print page.url

	response = br2.open(urlhost + '/' + page.url)
	
	links = br2.links(url_regex='id=1205&pid=')
	
	for link in links:
		
		print "\t" + link.url
	
		response = urllib2.urlopen(urlhost + '/' + link.url)
	
		html_doc = response.read()
		
		project_line = parse( html_doc )
		
		f.write(project_line)
	
		time.sleep(1.5)

f.close()



# FIND HACKS

#for node in soup.findAll('strong'): 
#  if node.next.endswith('Rok:'):
#texts.append(node.next)
#    pprint.pprint(node.next)


#output = []
#output += [project_det[3], project_det[6], project_det[7], project_det[14], project_det[15], project_det[16], project_det[17], project_det[18]]  

#pprint.pprint(output)

#################################################################################

# REGEX

#ustanova = re.search("<strong>Ustanova:<\/strong><br\/>(.*?)<br/>", str(project_det))

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
