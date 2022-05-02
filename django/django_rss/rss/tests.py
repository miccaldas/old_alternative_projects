from datetime import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Feed


class RssTests(TestCase):
    def setUp(self):
        self.feed = Feed.objects.create(
            name="Lobsters",
            title="ZFS Woes, or how ZFS Saved Me From Data Corruption",
            description="so much to tell",
            link="https://battlepenguin.com/tech/zfs-woes-or-how-zfs-saved-me-from-data-corruption",
            pub_date=timezone.now(),
            image="https://image.myawesomeshow.com",
        )

    def test_feed_content(self):
        self.assertEqual(self.feed.name, "Lobsters")
        self.assertEqual(self.feed.title, "ZFS Woes, or how ZFS Saved Me From Data Corruption")
        self.assertEqual(self.feed.description, "so much to tell")
        self.assertEqual(
            self.feed.link, "https://battlepenguin.com/tech/zfs-woes-or-how-zfs-saved-me-from-data-corruption"
        )
        self.assertEqual(self.feed.image, "https://image.myawesomeshow.com")

    def test_episode_str_representation(self):
        self.assertEqual(str(self.feed), "Lobsters: ZFS Woes, or how ZFS Saved Me From Data Corruption")

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(
            response,
            "ZFS Woes, or how ZFS Saved Me From Data Corruption",
        )
