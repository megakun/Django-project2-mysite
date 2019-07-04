from django.shortcuts import render
from django.http import HttpResponse, Http404
from myapp.models import Product
from django.template.loader import get_template
import random

# Create your views here.
def about(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)


def listing(request):
    #main body#
    p = Product.objects.all()
    template =  get_template('list.html')
    html = template.render({'products': p})
    return HttpResponse(html)#reformat and insert main body

def disp_detail(request, sku):
    try: 
        p = Product.objects.get(sku = sku) # this is fairly important 
    except Product.DoesNotExist:
        raise Http404('Wrong place hahaha')
    num = p.sku
    template = get_template('disp.html')
    html = template.render({'product': p ,'num': num})#assign p to product for the template
    return HttpResponse(html)

def index(request):
    q =  ['This is not a quote',
          'what is in your head',
          'wrong place']
    template = get_template('index.html')
    html = template.render({'quote' : random.choice(q) })
    return HttpResponse(html)