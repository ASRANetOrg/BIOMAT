from __future__ import unicode_literals
from django.contrib.sitemaps import ping_google
from django.db import models


class InfoPage(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    page = models.ForeignKey(InfoPage)
    headline = models.CharField(max_length=40)
    element_id = models.CharField(max_length=40, unique=True)
    order = models.IntegerField()
    text = models.CharField(max_length=3000)

    def table_class(self):

        new_self = self.text.replace('<table border="1" cellpadding="1" cellspacing="1" style="width:500px">',
                                 '<table class="table table-striped" style="text-align: center">')
        new_self = new_self.replace('<p>', '<p style="text-align: justify">')
        return new_self


class Entry(models.Model):
    # ...
    def save(self, force_insert=False, force_update=False):
        super(Entry, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

    def __unicode__(self):
        return str(self.order)
