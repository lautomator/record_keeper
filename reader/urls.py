from django.conf.urls import patterns, url

from reader import views

urlpatterns = patterns(
    '',
    # /reader/
    url(r'^$', views.reader_home, name='index'),
    # /reader/overview/
    url(r'^overview/$', views.reader_overview, name='overview'),
    # /reader/<reader_id>/details/
    url(r'^(?P<reader_id>\d+)/details/$', views.reader_details,
        name='details'),
    # /reader/add/
    url(r'^add/$', views.reader_add, name='add'),
    # /reader/<reader_id>/edit/
    url(r'^(?P<reader_id>\d+)/edit/$', views.reader_edit, name='edit'),
    # /reader/<reader_id>/delete/
    url(r'^(?P<reader_id>\d+)/delete/$', views.reader_delete,
        name='delete')
)
