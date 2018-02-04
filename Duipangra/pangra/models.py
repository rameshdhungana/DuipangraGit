from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import  User
# Create your models here.
#from time import timezone
from datetime import datetime



# class CustomUserManager(BaseUserManager):
#
#     def _create_user(self,email, password,
#                      is_staff, is_superuser, **extra_fields):
#         """
#         Creates and saves a User with the given username, email and password.
#         """
#         now = datetime.now()
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email,
#                           is_staff=is_staff, is_active=True,
#                           is_superuser=is_superuser,
#                           date_joined=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, email=None, password=None, **extra_fields):
#         return self._create_user(email, password, False, False,
#                                  **extra_fields)
#
#     def create_superuser(self,email, password, **extra_fields):
#         return self._create_user(email, password, True, True,
#                                  **extra_fields)


# class MyUser(AbstractBaseUser,PermissionsMixin):
#
#     #username=models.CharField(max_length=50,unique=True)
#     #password=models.CharField(max_length=128)
#     email=models.EmailField(max_length=254,unique=True)
#     address=models.CharField(max_length=50)
#     post=models.CharField(max_length=50)
#     #date_joined = models.DateTimeField(default=datetime.now)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_supersuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS =[]
#     objects=CustomUserManager()
#
#     def __str__(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.email
#
#     def get_username(self):
#
#         return self.email
#
#
#     class Admin:
#         pass
#
#     class Meta:
#         verbose_name_plural = 'hello sir'
#         ordering = ['email']

class Bikeobject(models.Model):
    status=models.CharField(max_length=30)
    image1=models.ImageField(width_field=100,height_field=100,default='hello',upload_to='image')


    class Admin:
        pass

char_choice=(('1','first'
              '2','second'
              '3','third'
              '4','fourth'
              '5','fifth'))





class All(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size=models.CharField(null=True,blank=True,choices=SHIRT_SIZES,max_length=40,help_text='this defines shirt size')
    #auto=models.AutoField(primary_key=True) # this is autofiled that can be set to primary key but only one auto filed in one class
    verbose_check=models.CharField('this is field to check verbose name',max_length=70)
    # verbose name is the human readable name for fields ,django will generate it if not given
    # by converting underscore to spaces

    #bikeobject=models.ForeignKey(Bikeobject)# LATER SEE on_delete=models.CASCADE not worked

    user=models.ManyToManyField(User,through='all_and_user')# manytomany fields can be on any one of model but no
    #on both models

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('login',agrs=[(self.id)])


    class Admin:
        pass
    def save(self,*args,**kwargs):
        if self.shirt_size=='S':
            return ('you are small in size')
        else:
            super().save(*args,**kwargs)

class all_and_user(models.Model):
    user=models.ForeignKey(User,related_name='inter_user',related_query_name='user_filter')
    all=models.ForeignKey(All,related_name="%(app_label)s%(class)srelated")
    date=models.IntegerField()

    class Admin:
        pass

class Specialuser(models.Model):
    location=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    post=models.OneToOneField(User,related_name="%(app_label)s%(class)srelated_name")

    def __str__(self):
        return ('specialuser has location %s and post %s '%(self.location,self.post))

    class Meta:
        verbose_name_plural='hello sir'
        ordering=['post']

    class Admin:
        pass




class commoninfo(models.Model):
    dob=models.DateField()

    class Meta:
        abstract=True


class ChildClass(commoninfo):

    duty = models.CharField(max_length=20)
    digit=models.IntegerField()
    dob=models.DateField()

    class Meta(commoninfo.Meta):
        ordering=['duty']

class Place(models.Model):
    add=models.CharField(max_length=10)


class Restuarent(Place):
    food=models.CharField(max_length=10)


class Supplier(Place):
   # pasal=models.ManyToManyField(Place) # only this line gave error  Reverse query name for 'Supplier.pasal' clashes with reverse query name for 'Supplier.place_ptr'.
       # HINT: Add or change a related_name argument to the definition for 'Supplier.pasal' or 'Supplier.place_ptr'.
   pasal = models.ManyToManyField(Place,related_name='provider')
   goods=models.CharField(max_length=68)

class proxyclass(Place):# exactly as Base class but Meta things can be changed and functions can be overriden or written
    class Meta:
        proxy=True
        ordering=['add']





#these class are  used to give example that its better to avoid class of multiple primary key of main tables
# inheritated by child class.thus provide a single base that is inheritated by more than two classes which are #
# then indheritated by single class separated by comma

class Piece(models.Model):
    pass
class Article(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

class BookReview(Book, Article):
    pass

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()



    def __str__(self):
        return self.name
class Custom_queryset(models.QuerySet):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def _ramesh(self):
        blog = Author.objects.filter(name='ramesh')
        return blog

    def ramesh(self): # both to qqueryset and base manager (public)
        blog = Author.objects.filter(name='ramesh')
        return blog

    def _dhungana(self): # only to queryser (private)
        blog = Author.objects.filter(name='ramesh')
        return blog
    _dhungana.queryset_only = True # only to queryset
    def dhungana(self):
        blog = Author.objects.filter(name='ramesh')
        return blog
    dhungana.queryset_only = False # both to manager and queryser




class Custom_Manager(models.Manager):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def count_function(self):
        blog = Blog.objects.all()
        return blog

    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    objects = Custom_Manager() # adding custom manager in model

    ramesh_objects = Custom_queryset.as_manager()

    def __str__(self):
        return self.name
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(null=True)
    mod_date = models.DateField(null=True)
    authors = models.ManyToManyField(Author,null=True)
    comments = models.IntegerField(null=True)
    pingbacks = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)

    entries = models.Manager()# custome manager

    def __str__(self):
        return self.headline

    
class Customer(User):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    landline_number = models.BigIntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='customer_pp/', null=True, blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return "{0} {1}".format(self.username, self.company_name)

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() ]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)