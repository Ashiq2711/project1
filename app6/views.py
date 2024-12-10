
from django.shortcuts import render,redirect
from app6.models import StudyTable
from app6.forms import table
from django.http import HttpResponse
from app6.forms import LoginForm
from django.contrib import messages

def myform(request):
    a=table()
    if request.method=="POST":
        b=table(request.POST)
        if b.is_valid():
            b.save()
            return HttpResponse("saved")
    return render(request,"form.html",{"key1":a})

def welcome(request):
    return render(request,"welcome.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = StudyTable.objects.get(Username=username)
                if user.check_password(password):

                    return redirect('welcome')  # Redirect to home page or dashboard
                else:
                    messages.error(request, 'Invalid username or password.')
            except StudyTable.DoesNotExist:
                messages.error(request, 'Invalid username or password.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def card(request):
    a=StudyTable.objects.all()
    return render(request,"card.html",{"kay2":a})

# Create your views here.
