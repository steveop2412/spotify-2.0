from django.shortcuts import render

# Create your views here.
def Signup(request):
    return render(request,'signup.html')
def SignMob(request):
    return render(request,'signwmob.html')