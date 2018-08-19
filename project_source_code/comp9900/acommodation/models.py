from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unknown"),
    )

    #user_id = models.AutoField(primary_key=True)
    # 姓名
    first_name = models.CharField(max_length=30,default="default")
    last_name = models.CharField( max_length=30,default='default')

    # 邮箱（登陆用邮箱） 密码
    user_email = models.EmailField(unique=True,default="default@gmail.com")
    user_password = models.CharField(max_length=30,default="default")
    # 性别 /生日 / 头像
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default="U")
    birthdate = models.DateField(null=True)
    image = models.ImageField(null=True)

    #自动生成字段 / 首次注册时间 /
    # register_login = models.DateField()
    # last_login= models.DateField()

    #可选字段 /用户自我介绍 / 用户联系电话
    user_description = models.TextField(max_length=100,blank=True,null=True)
    user_phone =  models.CharField(max_length=15,blank=True,null=True)

    #验证字段
    email_activated  = models.BooleanField(default=False)


class Lodging(models.Model):
    name = models.CharField(max_length=50)

    # NEIGHNOURHOOD_CHOICES=(
    # 'Ashfield',
    # 'Auburn',
    # 'Bankstown',
    # 'Blacktown',
    # 'Botany',
    # 'Bay',
    # 'Burwood',
    # 'Camden',
    # 'Campbelltown',
    # 'Canada',
    # 'Bay',
    # 'Canterbury',
    # 'City',
    # 'Of',
    # 'Kogarah',
    # 'Fairfield',
    # 'Holroyd',
    # 'Hornsby',
    # 'Hunters',
    # 'Hill',
    # 'Hurstville',
    # 'Ku - Ring - Gai',
    # 'Lane',
    # 'Cove',
    # 'Leichhardt',
    # 'Liverpool',
    # 'Manly',
    # 'Marrickville',
    # 'Mosman',
    # 'North',
    # 'Sydney',
    # 'Parramatta',
    # 'Penrith',
    # 'Pittwater',
    # 'Randwick',
    # 'Rockdale',
    # 'Ryde',
    # 'Strathfield',
    # 'Sutherland',
    # 'Shire',
    # 'Sydney',
    # 'The',
    # 'Hills',
    # 'Shire',
    # 'Warringah',
    # 'Waverley',
    # 'Willoughby',
    # 'Woollahra')



















