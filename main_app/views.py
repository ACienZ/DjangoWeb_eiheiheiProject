from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def MainPage(request):
    sess=request.session.get('username')
    if sess:
        return render(request,'main_app/Mainpage.html',{'login':True,'username':sess})
    else:
        return render(request,'main_app/Mainpage.html',{'login':False})

#将首页跳转到MainPage.html
def JumpToMainPage(request):
    return HttpResponseRedirect(reverse('MainPage'))

# def test(request):
#     return render(request,'main_app/ColumnPage_template.html')

def GreenShitOps(request):
    return render(request,'main_app/Ops_GreenShit.html')