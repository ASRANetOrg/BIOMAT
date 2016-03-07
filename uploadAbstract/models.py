from __future__ import unicode_literals
from django.db import models
from CORE.email_functionality import email_admin, email_client


class SubmittedAbstract(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=60, unique=True)
    paper_title = models.CharField(max_length=60)
    abstract = models.CharField(max_length=2000)

    def save(self, *args, **kwargs):

        sorted_self = [["Salutation", self.salutation], ["First name", self.first_name], ["Last Name", self.last_name],
                       ["Email", self.email], ["Paper Title", self.paper_title], ["Abstract", self.abstract],
                       ]

        email_client(self, "CORE 2016 Abstract Upload", "You have uploaded an abstract.")
        email_admin(self, "New CORE 2016 Abstract", "Please find enclosed the details for the new DISS "
                                                    "2016 abstract upload.", sorted_self)

        super(SubmittedAbstract, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email
