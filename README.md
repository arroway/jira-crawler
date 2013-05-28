# jira-crawler

JIRA crawler for very specific purpose

* Uses scrapy to get the list of projects from Apache and Codehaus JIRA servers.
* Generates the content of a hash with the key and the name of each project.

## Dependencies

This is a [scrapy][scrapy] project.

## Running

To run the two spider scripts:
 
~~~ sh
$ cd jira-crawler/jira
$ scrapy crawl apacheJira
$ scrapy crawl codehausJira
~~~

It should generate the files apacheJira.txt and codehausJira.txt.

[scrapy]: http://scrapy.org/
