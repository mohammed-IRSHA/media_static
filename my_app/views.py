from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def med(request):
    data=user.objects.all()
    return render(request,'read.html',{'my':data})
def upload(request):
    if request.method =='POST':
        title=request.POST.get('title')
        image=request.FILES.get('image')
        md_obj=user()
        md_obj.titles=title 
        md_obj.imagess=image
        md_obj.save()
        return redirect('meds')
    return render(request,"form.html")