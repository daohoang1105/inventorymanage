# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('sptable', views.sptable, name='sptable'),
    path('sptable/goodnew', views.sptablegoodnew, name='sptablegoodnew'),
    path('sptable/failscrap', views.sptablefailscrap, name='sptablefailscrap'),
    path('outsptable', views.outsptable, name='outsptable'),
    path('requestsp', views.requestsp, name='requestsp'),
    path('upload/fromfile', views.uploadfromfile, name='uploadfromfile'),
    path('upload/fromfile/success', views.uploadfromfilesuccess, name='uploadfromfilesuccess'),
    path('upload/fromfile/error', views.uploadfromfileerror, name='uploadfromfileerror'),
    path('upload', views.upload, name='upload'),
    path('addgsp', views.addgsp, name='addgsp'),
    path('update-spare/<str:pk>/', views.updateSpare, name="updatespare"),
    path('delete-spare/<str:pk>/', views.deleteSpare, name="deletespare"),
    path('sptable/item<str:pk>', views.spmanage, name='spmanage'),
    path('addgsp/sp<str:pk>', views.updateGsp, name="updateGsp"),
    path('exportcsv', views.exportcsv, name="exportcsv"),
    path('exportoutcsv', views.exportoutcsv, name="exportoutcsv"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
