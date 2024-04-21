from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from testing.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'indexx.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contacts = Contact(Name=name, Email=email, Phone=phone, Message=message, Date=datetime.today())
        contacts.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/contact')  # Assuming you have a URL named 'contact' in your urls.py
    return render(request, 'indexx.html')
