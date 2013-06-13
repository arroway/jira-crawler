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
  name = "libreoffice"
  allowed_domains = ["www.libreoffice.org"]
  start_urls = ["https://www.libreoffice.org/bugzilla/describecomponents.cgi"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    file_office = open("./libreofficeProjects.txt", 'w')
 
    for i in range(1, 130):

      # Check the item exist or else we are out of bounds
      div = '/html/body/div[2]/table/tr[' + str(i) + ']/th/a'  
      getdiv = hxs.select(div).extract()

      if getdiv:
        print getdiv
        # Crapy regexps but it works
        n = re.match(r".*\">(\w+)</a>.*", str(getdiv))

        if n:
          file_office.write(str(n.group(1)) + '|')

      else:
        break
