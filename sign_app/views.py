from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import auth

from sign_app.forms import UserSignInForm
from sign_app.forms import UserSignUpForm
from sign_app.models import UserModel

# Create your views here.

def sign_in(request):
    if request.method=="GET":
        form=UserSignInForm()
        return render(
            request,
            'sign_app/SignIn.html',
            {'form':form,}
        )
    elif request.method=="POST":
        form=UserSignInForm(request.POST)
        if form.is_valid():
            username_=form.cleaned_data['username']
            passwd_=form.cleaned_data['passwd']
            user=UserModel.objects.filter(username__exact=username_,passwd__exact=passwd_)
            if user:
                request.session['username']=username_
                return HttpResponseRedirect('MainPage')
            else:
                return HttpResponse(u'wrong')

def sign_up(request):
    if request.method=="GET":
        form=UserSignUpForm()
        return render(
            request,
            'sign_app/SignUp.html',
            {'form':form,}
        )
    elif request.method=="POST":
        form=UserSignUpForm(request.POST)
        if form.is_valid():
            username_=form.cleaned_data['username']
            passwd1_=form.cleaned_data['passwd1']
            passwd2_=form.cleaned_data['passwd2']
            user=UserModel.objects.filter(username__exact=username_)
            if user:
                return HttpResponse(u'username has already used')
                # return HttpResponseRedirect('MainPage')
            else:
                if passwd1_==passwd2_:
                    newuser=UserModel(username=username_,passwd=passwd1_)
                    newuser.save()
                    request.session['username']=username_
                    return HttpResponseRedirect('MainPage')
                else:
                    return HttpResponse(u'passwords are not same')

def sign_out(request):
    auth.logout(request)
    return HttpResponseRedirect('MainPage')