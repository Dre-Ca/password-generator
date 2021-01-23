from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length'))
    thepassword = ''
    characters = list('abcdefghigklmnop')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOP'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()<>?/'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
