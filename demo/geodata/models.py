from django.db import models

# Create your models here.

class GeoData(models.Model):  
    """
    GeoData is the detailed information about a location
    """
    addressZH = models.TextField()
    nameZH = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    nameEN = models.TextField()
    addressEN = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.nameZH,
                           self.addressZH)

