from django.http import HttpResponse
from django.template import loader

# Create your views here.
def web(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())