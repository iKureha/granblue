from django.conf.urls import url
from django.contrib import admin
from . import view

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^granblue/$', view.index),
    url(r'^server-status/$', view.index),
    url(r'^ajax_all_boss/$', view.ajax_all_boss),
    url(r'^ajax_tiamat/$', view.ajax_tiamat),
    url(r'^ajax_colossus/$', view.ajax_colossus),
    url(r'^ajax_leviathan/$', view.ajax_leviathan),
    url(r'^ajax_yggdrasil/$', view.ajax_yggdrasil),
    url(r'^ajax_celeste/$', view.ajax_celeste),
    url(r'^ajax_luminiera/$', view.ajax_luminiera),
]
