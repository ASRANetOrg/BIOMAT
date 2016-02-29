from __future__ import unicode_literals

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

    def __unicode__(self):
        return str(self.order)
