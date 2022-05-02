from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from rss.models import Feed


def save_new_entries(fp):
    try:
        feed_name = fp.channel.title
    except:
        feed_name = fp.feed.title

        image = fp.feed.image.href

    for item in fp.entries:
        if not Feed.objects.filter(description=item.description).exists():
            name = feed_name
            title = item.title
            link = item.link
            pub_date = parser.parse(item.published)

            entry = Feed(
                name=feed_name,
                title=item.title,
                link=item.link,
                pub_date=pub_date,
                image=fp.feed.image.href,
            )
            entry.save()


def fetch_quanta():
    _fp = feedparser.parse("https://api.quantamagazine.org/feed/")
    save_new_entries(_fp)


def fetch_reuters():
    _fp = feedparser.parse("https://www.reutersagency.com/feed/?best-topics=tech&post_type=best")
    save_new_entries(_fp)


def fetch_bbc():
    _fp = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml#")
    save_new_entries(_fp)


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_reuters()
        fetch_quanta()
        fetch_bbc()
