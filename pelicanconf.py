#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGINS = []

AUTHOR = 'Shu Zhao'
SITENAME = 'Shu Zhao'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

#DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME="themes/shu-zhao"
DISPLAY_CATEGORIES_ON_MENU=False
#MENUITEMS = [('Contact','/articles')]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
INDEX_SAVE_AS='articles/index.html'
PAGE_URL='{slug}.html'
PAGE_SAVE_AS='{slug}.html'
STATIC_PATHS = ['images','scripts','downloads','pages/scripts','blog/media']
JINJA_EXTENSIONS = []

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
