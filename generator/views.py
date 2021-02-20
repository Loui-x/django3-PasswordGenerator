from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):

    return render(request,'generator/home.html', {'password':'48yhuhtruht849wurd3'})

def password(request):
    passwordGen=''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upperCase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('specials'):
        characters.extend('!@#$%^&*(){}[]/?\><')
    for x in range(int(request.GET.get('len', 12))):
        passwordGen += random.choice(characters)
    return render(request,'generator/password.html',{'password':passwordGen} )



def about(request):

    return render(request,'generator/about.html')
