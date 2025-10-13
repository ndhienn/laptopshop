from django.http import HttpResponse
from django.template import loader
from web.models import Laptop
from django.shortcuts import render, get_object_or_404

# Create your views here.
def web(request):
    mylaptops = Laptop.objects.all()
    template = loader.get_template('product.html')
    context = {
        'mylaptops': mylaptops,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def product_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    return render(request, 'product_detail.html', {'laptop': laptop})