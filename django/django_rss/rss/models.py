from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    link = models.URLField()
    pub_date = models.DateTimeField()
    image = models.URLField(default="http://localhost/django_rss/static/imgs/sun_symbol.png")

    def __str__(self) -> str:
        return f"{self.name}: {self.title}"
