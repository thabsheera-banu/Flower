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
from django.shortcuts import render, redirect
from . models import book,Branch
from shop.models import Flower
#Create your views here.

def booking(request):
    print("tesy")
    flower = Flower.objects.all()
    branch=Branch.objects.all()
    if request.method == 'POST':
        print("post")
        name = request.POST.get('firstname', )
        flId= request.POST.get('flower', )
        email=request.POST.get('email',)
        flower1=Flower.objects.get(id=flId)
        address = request.POST.get('address', )
        branchId=request.POST.get('branch', )
        branchselected=Branch.objects.get(id=branchId)
        phone = request.POST.get('phone', )
        Quantity=request.POST.get('quantity')
        flo = book(name=name,Email=email,  phone=phone , Quantity=Quantity,adress=address,flower=flower1,category=branchselected)
        flo.save()
        return redirect('/booking/conformed')
    return render(request, 'booking.html',{'showflower':flower,'branch':branch})
def conform(request):
    return render(request,'conformed.html')
