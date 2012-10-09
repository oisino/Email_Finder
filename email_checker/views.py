from django.http import HttpResponse
import urllib2
import urllib
 

def email_validator(request):
    p=urllib2.urlopen("http://mailtester.com/")
    c=p.read()
    return HttpResponse(c)