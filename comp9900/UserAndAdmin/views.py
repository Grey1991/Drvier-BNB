'''

视图文件


'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from UserAndAdmin import forms, models
from django.contrib import messages
from django.core.mail import send_mail
from COMP9900 import settings


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        print(register_form.errors)
        if register_form.is_valid():
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data["password"]

            same_email_user = models.User.object.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = "Email already exists!"
                print(message)
                return HttpResponse(1)
                # 当一切都OK的情况下，创建新用户

            new_user = models.User()
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.set_password(password)
            new_user.email = email
            new_user.save()
            #  发送邮件
            #
            # subject = "Thank you for your registration "
            # message = "welcome to NSWLodge! we are very much appreciate your bussiness./n we will be in touch soon."
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [new_user.email]
            # send_mail(subject,message,from_email,to_list,fail_silently=True)



        return HttpResponse(2)
    else:
        return render(request,"index.html")



def login(request):
    if request.method == 'POST':
        #  前端 保证 email  password 有值
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        # 检查该用户 邮箱是否存在 并 确认
        _email = models.User.object.filter(email=email)
        if not _email.exists():
            message = "email account doesn't exist!"
            return HttpResponse(0)

        _is_active =_email[0].active
        if not _is_active:
            message = "please confirm your email account!"
            return HttpResponse(1)

        user = auth.authenticate(email=email, password=password)

        if user:
            auth.login(request,user)
            return HttpResponse(3)
        else:
            message = "Your email or password is incorrect. "
            return HttpResponse(2)
    return render(request,"index.html")



def logout(request):
    auth.logout(request)
    return redirect("userandadmin:index")

def editprofile(request,page_id):
    print(page_id)

    if page_id == '1':
        return render(request,'editprofile_editprofile.html')
    elif page_id == '2':
        return render(request,'editprofile_photos.html')
    else:
        return render(request,'editprofile.html')

def accountsetting(request):
    return render(request,'accountsetting.html')