from __future__ import unicode_literals
from django.db import models
from BIOMAT.email_functionality import email_admin, email_client

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class User(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    organisation = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)
    fee_normal = models.BooleanField(default=False)
    fee_student = models.BooleanField(default=False)
    fee_one_day = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        sorted_self = [["Salutation", self.salutation], ["First name", self.first_name], ["Last Name", self.last_name],
                       ["Email", self.email], ["Telephone", self.telephone], ["Address", self.address],
                       ["City", self.city], ["Country", self.country], ["Postcode", self.postcode],
                       ["Organisation", self.organisation], ["Paying Normal Fee", str(self.fee_normal)],
                       ["Paying Student Fee", str(self.fee_student)], ["One Day Pass Fee", str(self.fee_one_day)],
                       ]

        email_client(self, "BIOMAT 2016 Conference Registration", "You are officially registered for BIOMAT 2016")
        email_admin(self, "New BIOMAT 2016 Registrant", "Please find enclosed the details for the new BIOMAT "
                                                      "2016 registrant.", sorted_self)

        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email
