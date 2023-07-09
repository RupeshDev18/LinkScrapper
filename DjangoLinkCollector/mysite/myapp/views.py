from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponseRedirect
from .models import Link
# Create your views here.

def scrape(request):
    if request.method == "POST":
        site=request.POST.get('site','')
        page=requests.get(site)
        soup=BeautifulSoup(page.text,'html.parser')
    

        for link in soup.find_all('a'):
            link_address=(link.get('href'))
            link_text=link.string
            Link.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data=Link.objects.all()


    return render(request,'myapp/result.html',{'data':data})


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')