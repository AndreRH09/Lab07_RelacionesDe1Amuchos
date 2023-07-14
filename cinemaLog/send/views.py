from django.shortcuts import render
from django.core.mail import send_mail  

# Create your views here.

def index(request):
    send_mail('hello from Andre',
    'Hello there this is an automated message.',
    'anthony@prettyprinted.com',
    ['favav60651@iturchia.com'],
    fail_silently=False)
    return render(request,'send/index.html')
