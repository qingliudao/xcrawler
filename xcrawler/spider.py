"""
    spider
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import logging
from .http.request import Request

__all__ = ['BaseSpider']

logger = logging.getLogger(__name__)


class BaseSpider(object):
    name = ''
    start_urls = []
    custom_settings = {}

    def __init__(self):
        self.crawler = None

    def __repr__(self):
        return '<{} name="{}">'.format(self.__class__.__name__, self.name)

    def __str__(self):
        return 'spider:' + self.name

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_request_from_url(url)

    def make_request_from_url(self, url):
        return Request(url, spider=self, callback=self.parse)

    def parse(self, response):
        raise NotImplementedError

    def on_engine_idle(self, engine):
        """You can add more requests to the engine by
        calling :meth:`engine.append_request(req)`."""
        pass
