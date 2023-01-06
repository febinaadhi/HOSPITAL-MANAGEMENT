from django.shortcuts import render
from .models import department1,doctors1
from .forms import Bookingform


# Create your views here.
def  index(request):
    return render(request,'index.html')
def  about(request):
    return render(request,'about.html')
def  booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
    form=Bookingform()
    dict_book={
        'book':form
    }
    return render(request,'booking.html',dict_book)

def  contact(request):
    return render(request,'contact.html')
def  doctors(request):  
     
    dict_doc={
        'doc':doctors1.objects.all()
         }
    
    return render(request,'doctors.html',dict_doc)
def  department(request):
    dict_dept={
        'dept':department1.objects.all()
    }
    return render(request,'department.html',dict_dept)