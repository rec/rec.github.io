AUTHOR = 'Tom Ritchford'
SITENAME = 'On computer programming'
SITEURL = 'https://rec.github.io'


# Experimental
TYPOGRIFY = True

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%a %d %b %Y, %H:%M %Z'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Programming'
DELETE_OUTPUT_DIRECTORY = True
WITH_FUTURE_DATES = False

LOAD_CONTENT_CACHE = True

OUTPUT_PATH = 'docs'

UTTERANCES_REPO = "rec/rec.github.io"
UTTERANCES_LABEL = "Comments"
UTTERANCES_FILTER = False
UTTERANCES_THEME = "github-light"

COMMENTS_INTRO="You can comment about this article with your GitHub account"

# Blogroll
LINKS = (
    ('Python.org', 'https://www.python.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/rec'),
    ('Mastodon', 'https://toot.community/@TomSwirly'),
#    ('RSS', 'https://rec.github.io/feeds/all.atom.xml'),
#    ('LinkedIn', 'https://www.linkedin.com/in/tomritchford/'),
)

DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
