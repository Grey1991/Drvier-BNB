from django import forms
from accommodations.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'date_of_birth')


class RegisterForm(forms.ModelForm):
    """
    def create_user(self,email,first_name = None,last_name =None,password = None,date_of_birth = None,is_staff = False,is_admin = False, is_active = True):
    注册一个新用户

    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model =User
        fields = ('email', 'password', 'first_name','last_name','date_of_birth')

    def clean_password2(self):

        # 检查2次 密码是否一致

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

