#!/usr/bin/env python
# encoding=utf-8
 
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy import log
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

class CodehausJiraSpider(BaseSpider):
  name = "codehausJira"
  allowed_domains = ["jira.codehaus.org"]
  start_urls = ["http://jira.codehaus.org/secure/BrowseProjects.jspa#all"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    file_codehaus = open("./codehausJira.txt", 'w')
    
    for i in range(1, 100):

      # Check the item exist or else we are out of bounds   
      div = '/html/body/div/section/div/div[2]/div[' + str(i) + ']'  
      getdiv = hxs.select(div)

      if getdiv:

        for j in range (1,300):
	
          # Project name lazy XPath
          name = '/html/body/div/section/div/div[2]/div[' + str(i) + ']/div[2]/div/table/tbody/tr[' + str(j) + ']/td/a'

          # Project key lazy XPath
          key = '/html/body/div/section/div/div[2]/div[' + str(i) + ']/div[2]/div/table/tbody/tr[' + str(j) + ']/td[2]'
 
          project_name = hxs.select(name).extract()
          project_key = hxs.select(key).extract()
  
          if project_name and project_key:

            # Crapy regexps but it works
            m = re.match(r".*\">(.*)</a>(.*)\">(.*)</a>(.*)\">(.*)</a>.*", str(project_name))
            n = re.match(r".*\\n\s*(\w+)\\n.*", str(project_key))

            if m and n:
              file_codehaus.write('"' + str(n.group(1)) + '", "' + str(m.group(1)) + '", ')

	  else:
            break
