from __future__ import unicode_literals

from django.db import models

class Orders(models.Model):
    name = models.TextField()
    seller = models.CharField(max_length = 100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name: 'Order'
        verbose_name_plural: 'Orders'