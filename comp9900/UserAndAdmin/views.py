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
            password1 = register_form.cleaned_data["password1"]
            password2 = register_form.cleaned_data["password2"]

            if password1 != password2:
                message ="passwords do not match!"
                return render(request,'register.html',locals())

            same_email_user = models.User.object.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = "Email already exists!"
                return render(request,'register.html',locals())
                # 当一切都OK的情况下，创建新用户

            new_user = models.User()
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.set_password(password1)
            new_user.email = email
            new_user.save()
            #  发送邮件

            subject = "Thank you for your registration "
            message = "welcome to NSWLodge! we are very much appreciate your bussiness./n we will be in touch soon."
            from_email = settings.EMAIL_HOST_USER
            to_list = [new_user.email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)



        return redirect('userandadmin:login')  # 自动跳转到登录页面
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        #  前端 保证 email  password 有值
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        # 检查该用户 邮箱是否存在 并 确认
        _email = models.User.object.filter(email=email)
        if not _email.exists():
            message = "email account doesn't exist!"
            return render(request, 'login.html', locals())

        _is_active =_email[0].active
        if not _is_active:
            message = "please confirm your email account!"
            return render(request, 'login.html',locals())

        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request,user)
            return redirect("userandadmin:index")
        else:
            message = "Your email or password is incorrect. "
            return render(request, 'login.html',locals())
    return render(request,'login.html')





def logout(request):
    auth.logout(request)
    return redirect("userandadmin:index")
