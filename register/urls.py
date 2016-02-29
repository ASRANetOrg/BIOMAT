from django.conf.urls import url, patterns
from register import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='register'),)
