from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible

# Create your models here.
class DarazItem(models.Model):
    title = models.CharField(max_length=512)
    image = models.CharField(max_length=344)
    url = models.CharField(max_length=324)
    price = models.CharField(max_length=32)
    description = models.CharField(max_length=322)


    def __unicode__(self):
        return "{}".format(self.title)


class NepBayItem(models.Model):
    title = models.CharField(max_length=512)
    image = models.CharField(max_length=344)
    url = models.CharField(max_length=324)
    price = models.CharField(max_length=32)
    description = models.CharField(max_length=322)


    def __unicode__(self):
        return "{}".format(self.title)


class SdealItem(models.Model):
    title = models.CharField(max_length=512)
    image = models.CharField(max_length=344)
    url = models.CharField(max_length=324)
    price = models.CharField(max_length=32)
    description = models.CharField(max_length=322)


    def __unicode__(self):
        return "{}".format(self.title)
