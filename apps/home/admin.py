# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Upload, User, AllSparePart, SparePartOutRecord, SparePartOutRequest
# Register your models here.

admin.site.register(User)
admin.site.register(AllSparePart)
admin.site.register(Upload)
admin.site.register(SparePartOutRecord)
admin.site.register(SparePartOutRequest)
