from django.conf.url = import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'email_generator.views.input')
)