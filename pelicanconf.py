#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR = 'David Koppstein'
SITENAME = 'David Koppstein'
SITEURL = 'http://www.davidkoppstein.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = '../pelican-sober'

STATIC_PATHS = ['blog', 'images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DISQUS_SITENAME = 'davidkoppstein'


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/dkoppstein/'),
          ('bitbucket', 'https://bitbucket.org/dkoppstein'),
          ('twitter', 'https://twitter.com/dkoppstein'),
          ('rss', 'http://davidkoppstein.com/feeds/all.atom.xml'))

PELICAN_SOBER_TWITTER_CARD_CREATOR = 'dkoppstein'
    
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
