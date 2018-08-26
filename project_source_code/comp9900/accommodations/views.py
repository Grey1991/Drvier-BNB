'''

视图文件


'''
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login



def mainPage(request):
    return render(request,"mainpage.html")




def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('u')
        password = request.POST.get('p')
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'mainpage.html', {})
            else:
                return HttpResponse("please confirm your email account!")

        else:
            print ("Invalid login details: {0}, {1}".format(email, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})

