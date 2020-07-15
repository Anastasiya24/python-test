# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from quickstart.models import Orders

admin.site.register(Orders)