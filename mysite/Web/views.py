from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import laptop

def Web(request):
    mylaptops = laptop.objects.all()
    template = loader.get_template('test.html')
    context = {
        'mylaptops': mylaptops,
    }
    return HttpResponse(template.render(context, request))
def product(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())