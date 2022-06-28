from django.shortcuts import render, redirect
from . models import book,Branch
from shop.models import Flower
#Create your views here.

def booking(request):
        flower = Flower.objects.all()
        branch=Branch.objects.all()
        if request.method == 'POST':
            name = request.POST.get('name', )
            address = request.POST.get('address', )
            phone = request.POST.get('phone', )
            flo = book(name=name,  phone=phone ,address=address,flower=flower,branch=branch)
            flo.save()
            return redirect('/')
        return render(request, 'booking.html',{'showflower':flower,'branch':branch})
def conform(request):
    return render(request,'conformed.html')
