import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import cached_property

@dataclass
class Advisory:
    destination: str
    severity: str

class ItineraryGuard:
    def __init__(self, feeds):
        self.feeds = feeds
        self.cache = {}
        self.cache_expires = datetime.now() + timedelta(hours=12)

    @cached_property
    def aggregated_advisories(self):
        advisories = []
        for feed in self.feeds:
            advisories.extend(self.parse_feed(feed))
        return advisories

    def parse_feed(self, feed):
        advisories = []
        for destination, severity in feed.items():
            advisories.append(Advisory(destination, severity))
        return advisories

    def get_advisory(self, destination):
        if self.cache and self.cache_expires > datetime.now():
            return self.cache.get(destination)
        else:
            self.cache = {advisory.destination: advisory for advisory in self.aggregated_advisories}
            self.cache_expires = datetime.now() + timedelta(hours=12)
            return self.cache.get(destination)

    def check_itinerary(self, itinerary):
        advisories = []
        for destination in itinerary:
            advisory = self.get_advisory(destination)
            if advisory:
                advisories.append(advisory)
        return advisories

    def update_feeds(self, new_feeds):
        self.feeds = new_feeds
        self.cache = {}
        self.cache_expires = datetime.now() + timedelta(hours=12)
