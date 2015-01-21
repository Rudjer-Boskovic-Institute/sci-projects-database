#!/usr/bin/python

import mechanize

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

print link1.url

response = br.open(urlhost + '/' + link1.url)

link2 = br.find_link(url_regex='page',nr=1)
	


#help(br.links)

# br.follow_link takes either a Link object or a keyword arg (such as nr=0).

# br.links() lists all the links.

# br.links(url_regex='...') lists all the links whose urls matches the regex.

# br.links(text_regex='...') lists all the links whose link text matches the regex.

# br.follow_link(nr=num) follows the numth link on the page, with counting starting at 0. It returns a response object (the same kind what br.open(...) returns)

# br.find_link(url='...') returns the Link object whose url exactly equals the given url.

# br.find_link, br.links, br.follow_link, br.click_link all accept the same keywords. Run help(br.find_link) to see documentation on those keywords.
