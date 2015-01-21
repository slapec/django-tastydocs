from django.conf.urls import patterns
from tastydocs.views import doc

urlpatterns = patterns(
    '',
    (r'^api/$', doc),
    (r'^example/(?P<resource_name>.+)/', 'tastydocs.views.example_data'),
)
