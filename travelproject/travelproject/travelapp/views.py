from django.shortcuts import render
from.models import place
from.models import charecter

# Create your views here.
def demo(request):
    obj = place.objects.all()
    det = charecter.objects.all()
    return render(request,"index.html",{'result':obj,'menu':det})
