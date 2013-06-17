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

class EclipseSpider(BaseSpider):
  name = "eclipse"
  allowed_domains = ["bugs.eclipse.org"]
  start_urls = ["https://bugs.eclipse.org/bugs/describecomponents.cgi"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    file_eclipse = open("./eclipseProjectsHash.txt", 'w')
 
    for i in range(1, 200):

      # Check the item exist or else we are out of bounds
      div = '/html/body/div[2]/table/tr[' + str(i) + ']/th/a'  
      getdiv = hxs.select(div).extract()

      if getdiv:
        print getdiv
        # Crapy regexps but it works
        n = re.match(r".*\">(\w+)</a>.*", str(getdiv))

        if n:
          file_eclipse.write('"' + str(n.group(1)).upper() + '", "' + n.group(1) + '", ')

      else:
        break
