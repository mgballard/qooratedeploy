#!/usr/bin/env python
from brubeck.auth import authenticated
from brubeck.request_handling import JSONMessageHandler, cookie_encode, cookie_decode
from brubeck.templating import load_jinja2_env, Jinja2Rendering
from dictshield import fields
from dictshield.document import Document, EmbeddedDocument
from dictshield.fields import ShieldException
from gevent import Greenlet
from gevent.event import Event
from urllib import unquote, quote
import sys
import logging
import httplib
import os
import time
import random
import datetime
from qoorateserver.qoorate import Qoorate
from qoorateserver.handlers.feed import FeedHandler
from qoorateserver.handlers.embed import EmbedHandler,EmbedHandlerJSON 
from qoorateserver.handlers.oauth import QoorateOAuthHandler
from brubeckuploader.handlers import TemporaryImageUploadHandler, TemporaryImageViewHandler


##
## runtime configuration
##

## Turn on some debugging
logging.basicConfig(level=logging.DEBUG)
httplib.HTTPConnection.debuglevel = 1

#set the project directory to the root of our deployment directory
project_dir = '.'
logging.info("Using project directory: " + project_dir)

config = {
    'project_dir': project_dir,
    'mongrel2_pair': ('ipc://run/qoorateserver/mongrel2_send', 'ipc://run/qoorateserver/mongrel2_rcv'),
    'handler_tuples': [ ## Set up our routes
        (r'^/q/feed', FeedHandler),
        (r'^/q/embed/json', EmbedHandlerJSON),
        (r'^/q/embed', EmbedHandler),
        (r'^/q/uploader/images/(?P<file_name>.+)$', TemporaryImageViewHandler),
        (r'^/q/uploader', TemporaryImageUploadHandler),
        (r'^/q/oauth/(?P<provider>.+)/(?P<action>.+)$', QoorateOAuthHandler),
    ],
    'cookie_secret': '_1sRe%%66a^O9s$4c6ld!@_F%&9AlH)-6OO1!',
    'template_loader': load_jinja2_env( project_dir + '/apps/qoorateserver/templates'),
    'settings_file': project_dir + '/config/qoorateserver/settings.py',
    'log_level': logging.DEBUG,
}

## other settings should be put in the file specified by 'settings_file'

##
## get us started!
##


app = Qoorate(**config)
## start our server to handle requests
if __name__ == "__main__":
    app.run()
