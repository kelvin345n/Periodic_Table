from django.shortcuts import render
from.models import Element

# Create your views here.
def home(request):
    elements = Element.objects.all()

    context = {'elements': elements}
    return render(request, 'elementss/home.html', context)

def description(request, pk):
    elements = Element.objects.get(name=pk)
    context = {'elements': elements}
    return render(request, 'elementss/description.html', context)