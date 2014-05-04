# -*- coding: utf-8 -*-

import datetime

import tinkerer
import tinkerer.paths

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = 'akun\'s blog'

# Change this to the tagline of your blog
tagline = u'软体动物鼻涕虫的各种随便'

# Change this to the description of your blog
description = 'This is an awesome blog'

# Change this to your name
author = 'akun'

# Change this to your copyright string
year = datetime.datetime.now().year
copyright = '1985-%d, %s' % (year, author)

# Change this to your blog root URL (required for RSS feed)
website = 'http://zhengkun.info/'

language = 'zh_cn'

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = 'zhengkun'

# Change your favicon (new favicon goes in _static directory)
html_favicon = '_static/tinkerer.ico'

# Pick another Tinkerer theme or use your own
html_theme = 'flat'

# Theme-specific options, see docs
html_theme_options = {}

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = 'feed.atom'

# Generate full posts for RSS feed even when using "read more"
rss_generate_full_posts = False

# Set rss_max_items to the number of items to include in the feed,
# or 0 to include everything.
rss_max_items = 0

# rutherford config
blog_date = year
rights = 'This work is licensed under a Creative Commons Attribution 4.0 License: http://creativecommons.org/licenses/by/4.0/'

# Number of blog posts per page
posts_per_page = 10

# Character use to replace non-alphanumeric characters in slug
slug_word_separator = '_'

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus', 'rutherford']

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['_themes', tinkerer.paths.themes]

# Add file patterns to exclude from build
exclude_patterns = ['drafts/*', '_templates/*']

# Add templates to be rendered in sidebar here
html_sidebars = {
    '**': ['searchbox.html', 'recent.html', 'tags_cloud.html', 'categories.html']
}

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
