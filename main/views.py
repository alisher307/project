from django.shortcuts import render
from .models import *
# Create your views here.


def index_view(request):
    context ={
        "banner": Banner.objects.all(),
        "about_us": About_us.objects.all(),
        "special": Special.objects.all(),
        "awards": Awards.objects.all(),
        "employee": Emplayee.objects.all()
    }
    return render(request, 'index.html', context)


def create_reservation_view(request):
    if request.method == "POST":
        date = request.POST['date']
        time = request.POST['time']
        phone = request.POST['phone']
        last_name = request.POST['last_name']
        message = request.POST['message']
        Reservation.objects.create(
            date=date,
            time=time,
            phone=phone,
            last_name=last_name,
            message=message,
        )
        return redirect('index_url')
    context = {
        "banner": Banner.objects.all(),
        "about_us": About_us.objects.all(),
        "special": Special.objects.all(),
        "awards": Awards.objects.all(),
        "employee": Emplayee.objects.all()
    }
    return render(request,'index.html', context)
