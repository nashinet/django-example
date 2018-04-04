from django.conf.urls import url, include
from . import views

# TEMPLATE TAGGING, global name
app_name = 'basic_app'
urlpatterns = [
    url(r'^relative/$', views.relative_url_templates, name='relative'),
    url(r'^other/$', views.other, name='other')
]
