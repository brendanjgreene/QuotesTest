from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quote(models.Model):

    class Meta:
        app_label = "quotesTest_app"

    author_name = models.CharField(max_length=100)
    authorLast_name = models.CharField(max_length=100)
    quote_full = models.CharField(max_length=255)

    def __str__(self):
        return ' '.join([
            self.author_name,
            self.authorLast_name,
            self.quote_full,
        ])
