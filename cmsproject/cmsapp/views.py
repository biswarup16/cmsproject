from django.shortcuts import render
from .models import Carousel,Cards,About,Contact, Photogallery


# Create your views here.
def index(request):
    carousel = Carousel.objects.all()
    # context  = {'carousel' : carousel}

    cards = Cards.objects.all()
    about = About.objects.all()
    # context2  = {'carousel' : carousel}
    photogallery = Photogallery.objects.all()

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")

        phone = request.POST.get("phone")

        desc = request.POST.get("desc")

        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()
    return render(request,'index.html' ,{'carousel' : carousel,'cards' : cards,'about':about,'photogallery':photogallery})



def about(request):
    about = About.objects.all()
    return render(request,'about.html',{'about':about})



def services(request):
    cards = Cards.objects.all()
    return render(request,'services.html',{'cards' : cards})   


def photogallery(request):
    photogallery = Photogallery.objects.all()
    return render(request,'photogallery.html',{'photogallery' : photogallery}) 


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")

        phone = request.POST.get("phone")

        desc = request.POST.get("desc")

        document = request.POST.get("document")

        instance = Contact(name=name, email=email, phone=phone, desc=desc,document=document)
        instance.save()
    return render(request,'contact.html')      
