from django.conf.urls import url, patterns
from uploadAbstract import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='uploadAbstract'),)
