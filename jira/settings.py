# Scrapy settings for jira project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'jira'

SPIDER_MODULES = ['jira.spiders']
NEWSPIDER_MODULE = 'jira.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jira (+http://www.yourdomain.com)'
