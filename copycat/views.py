from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authlogin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

@login_required(login_url='login')
def result(request):
    ptext = request.POST.get('ptext', 'no text')
    print(ptext)
    plager = ptext
    params = {'plagiarized_text' : plager}
    messages.success(request, "Submission complete, kindly wait for processing")
    return render(request, 'result.html', params)

def submissions(request):
    return render(request, 'submissions.html')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(request, username = loginusername, password = loginpassword)
        if user is not None:
            authlogin(request,user)
            messages.success(request, "you are successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "invalid credentials")
            return redirect('login')

    return HttpResponse("logeed in")

def handleLogout(request):
    logout(request)
    messages.success(request, "you are successfully logged out")
    return redirect('login')

    # return HttpResponse("logeed out")