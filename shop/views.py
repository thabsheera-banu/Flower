
from . models import Flower
from django.shortcuts import render, redirect
# Create your views here.
#def demo(request):
    #return HttpResponse('hello world')
#@login_required
def demo(request):
    pass
    # flower=Flower.objects.all()
    # context={
    #     'flower_list':flower
    # }


    # return render(request,'main.html',context)
    return render(request,'main.html')







