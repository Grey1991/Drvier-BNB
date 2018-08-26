from django.db import models
from datetime import datetime
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name=None, last_name=None, password=None, date_of_birth=None, is_active=True):
        if not email:
            raise ValueError("empty email! ")

        if not password:
            raise ValueError("empty password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.set_date_of_birth(date_of_birth)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, first_name=None, last_name=None, password=None):

        staff = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name

        )
        staff.staff = True
        staff.save(using=self._db)
        return staff

    def create_superuser(self, email, first_name=None, last_name=None, password=None):
        admin = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name

        )
        admin.staff = True
        admin.admin = True
        admin.save(using=self._db)
        return admin


class User(AbstractBaseUser, PermissionsMixin):
    # 登陆 为用户名登陆
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True)
    USERNAME_FIELD = "email"

    '''
     AbstractBaseUser 内部实现了  密码 和 登陆时间
    password = models.CharField(_('password'), max_length=128)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
 
    staff 工作人员
    admin 管理员 
    
    '''
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    '''
    必填项
    
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    # required_fileds /  创建createsuperuser
    REQUIRED_FIELDS = ['first_name', 'last_name']

    object = UserManager()

    '''
    方法
    
    '''

    def set_date_of_birth(self, raw_date_of_birth):
        if not raw_date_of_birth:
            raw_date_of_birth = datetime.now()
        self.date_of_birth = raw_date_of_birth

    # long /short 用户标识别
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    # 权限

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        return False

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    '''
    个人信息
    性别
    用户自我介绍
    用户手机
    '''

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unknown"),
    )
    user = models.OneToOneField(User, models.CASCADE)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default="U")
    image = models.ImageField(null=True)
    user_description = models.TextField(max_length=100, blank=True, null=True)
    user_phone = models.CharField(max_length=15, blank=True, null=True)







class Property(models.Model):
    """房屋表：
        隐藏字段：user_ID、property_ID、Image_ID、注册时间 created_at、最后信息跟新时间updated_at
        显示在网页上的字段：
        1. 价格（price）
        2. 房源类型：property、apartment、studio
        3. 地点（address）
        4. 入住时间
        5. 入住人数
        6. 卧室数量
        7. 床铺类型
        8. 床铺数量：double、single、softbed
        9. 卫生间数量
        10. 面积（整体）

        12. 便利设施：厨房、洗漱用品、暖气、空调、洗衣机、烘干机、WIFI、早餐、吹风机、电视机、婴儿床、浴缸
        13. 设施：停车位、健身房、游泳池
        14. 房屋守则：是否适合举办party，是否允许携带宠物，是否允许吸烟
        15. 是否发布
    """
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    # user_ID = models.ForeignKey('UserAndAdmin.User', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    TYPE_PROPERTY_CHOICES = (
        ('H', 'House'),
        ('A', 'Apartment'),
        ('S', 'Studio'),
        ('O', 'others'),
    )
    types_property = models.CharField(max_length=1, choices=TYPE_PROPERTY_CHOICES, default='O')
    num_guests = models.IntegerField(default=0)
    num_rooms = models.IntegerField(default=0)

    num_doubleBed = models.IntegerField(default=0)
    num_singleBed = models.IntegerField(default=0)
    num_sofaBed = models.IntegerField(default=0)

    num_bathrooms = models.IntegerField(default=0)
    overall_size = models.FloatField(default=0.0)

    """
       12. 便利设施：厨房、洗漱用品、暖气、空调、洗衣机、烘干机、WIFI、早餐、吹风机、电视机、婴儿床、浴缸
       Kitchen, toiletries, heating, air conditioning, washing machine,
       dryer, WIFI, breakfast, hair dryer, TV, crib, bathtub
    """
    has_kitchen = models.BooleanField(default=False)
    has_toiletries = models.BooleanField(default=False)
    has_heating = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_washing_machine = models.BooleanField(default=False)
    has_dryer = models.BooleanField(default=False)
    has_breakfast = models.BooleanField(default=False)
    has_hair_dryer = models.BooleanField(default=False)
    has_TV = models.BooleanField(default=False)
    has_crib = models.BooleanField(default=False)
    has_bathtub = models.BooleanField(default=False)
    """
        13. 设施：停车位、健身房、游泳池
        Parking Spaces, gyms, swimming pools
    """
    has_parking = models.BooleanField(default=False)
    has_gyms = models.BooleanField(default=False)
    has_swimming_pools = models.BooleanField(default=False)
    """
        14. 房屋守则：是否适合举办party，是否允许携带宠物，是否允许吸烟
        party, pet, smoking
    """
    is_allowed_party = models.BooleanField(default=False)
    is_allowed_pet = models.BooleanField(default=False)
    is_allowed_smoking = models.BooleanField(default=False)
    is_allowed_couple = models.BooleanField(default=False)

    longitude = models.FloatField()  # 经度
    latitude = models.FloatField()  # 纬度

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=False)








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
