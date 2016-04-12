from __future__ import unicode_literals
from BIOMAT.email_functionality import email_admin, email_client
from django.db import models


class SubmittedAbstract(models.Model):
    salutation = models.CharField(max_length=6)
    primary_author_first_name = models.CharField(max_length=35)
    primary_author_surname = models.CharField(max_length=35)
    co_authors_names = models.CharField(max_length=770)
    email = models.EmailField(max_length=60, unique=True)
    paper_title = models.CharField(max_length=60)
    abstract = models.CharField(max_length=2000)

    def save(self, *args, **kwargs):

        sorted_self = [["Salutation", self.salutation], ["Primary Author First Name", self.primary_author_first_name],
                       ["Primary Author Surname", self.primary_author_surname],
                       ["Co Authors Names", self.co_authors_names], ["Email", self.email],
                       ["Paper Title", self.paper_title], ["Abstract", self.abstract],
                       ]

        email_client(self, "BIOMAT 2016 Abstract Upload", "Thank you for uploading your abstract to BIOMAT 2016")
        email_admin(self, "New BIOMAT 2016 Abstract", "Please find enclosed the details for the new BIOMAT "
                                                    "2016 abstract upload.", sorted_self)

        super(SubmittedAbstract, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email
