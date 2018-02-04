from django.shortcuts import render,redirect,HttpResponseRedirect,Http404
from django.contrib.auth.forms import UserCreationForm
from .forms import register_form
# Create your views here.
from .forms import login_form,product_insert_form
from django.shortcuts import HttpResponse
from django.contrib.auth import login as auth_login
#from pangra.backends import CustomUserAuth
from django.conf import settings
from pangra.models import Entry

from django.contrib.auth import get_user_model as model_now

#from django.contrib.auth import authenticate
from django.views.generic import TemplateView,CreateView
from django.core.mail import send_mail

from django.views import View
from django.views.generic import TemplateView,DetailView,ListView,FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from .forms import *
from django.forms import BaseFormSet,formset_factory,modelformset_factory,BaseModelFormSet
from jsonfield import JSONField
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt


class Postajaxexample(View):

    @method_decorator(csrf_exempt)
    @method_decorator(xframe_options_exempt)
    def post(self,request,*args,**kwargs):
        # print(request.data)
        print(request.POST)

        # firstname = request.POST.get('firstname')
        # first = request.POST.get('first')
        # print(first)
        #
        # lastname = request.POST.get('lastname')
        # last = request.POST.get('lastname')
        # last_name = request.POST.get('last_name')
        # print(last)
        # print('this is last name form name attribute' +last_name)
        #
        # lastname = lastname+'@gmail.com'
        # a=Author.objects.create(name=firstname,email=lastname)
        # a.save()

        #array sent as value form ajax
        key1= request.POST.getlist('key1[]')
        print(key1)
        key2= request.POST.get('key2')
        print(key2)

        #sending json data
        data = {}
        data['status'] = 'okay'
        data['actual_data'] = '<p>hello is this paragraph </p> '+str(key1)+'this is key2'+key2+ "<h1 class='label label-success'>Ramesh</h1>"
        return HttpResponse(json.dumps(data))


class UsernameValidation(View):


    def get(self,request,**kwargs):
        username =self.kwargs.get('username')
        if Customer.objects.filter(username=username).exists():
            return HttpResponse('already used')
        else:
            print(username)
            return HttpResponse('okay')

class AjaxView(TemplateView):

    template_name = 'ajax_html.html'
    form_class = CustomerSignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print(self.kwargs.get('name'))
        # context=self.kwargs.get('name')
        context['check_name']='Ramesh'
        context['form']=self.form_class
        return context

class JsonAjax(TemplateView):
    template_name = 'postajaxexample.html'

    def get(self,request):
        data=[]
        data.append({'na':'ramesh',
                     'nam': 'rame',
                     'name': 'ra'})
        data.append({'na': 'aaaa',
                     'nam': 'bbbb',
                     'name': 'cccc'})
        return HttpResponse(json.dumps(data),content_type = 'application/json')


class CarAndTruck(TemplateView):
    template_name = 'car_and_truck.html'

class ModelFilterQuery(BaseModelFormSet):

    def __init__(self):
        super().__init__()
        self.queryset = Blog.objects.all()

def ModelBlogFormsetView(request):
    template_name = 'modelformset.html'
    comboblog = modelformset_factory(Blog, fields=['name', 'tagline'])
    # making collection of Blog from moddels.py using modelformeset_factory

    if request.method == 'POST':
        formset = comboblog(request.POST, request.FILES)
        if formset.is_valid():
            # print('this is testing 2222')
            #
            # for form in formset:
            #     name = form.cleaned_data.get('name')
            #     tagline= form.cleaned_data.get('tagline')
            #     blog = Blog.objects.create(name=name, tagline=tagline)
            #     blog.save()
            formset.save()
            return HttpResponse('/blog/')
        else:
            raise forms.ValidationError('form is not valid')
    else:
        formset = comboblog(queryset = Blog.objects.filter(name__icontains='r'))
    return render(request, 'modelformset.html', {'formset': formset})
#model formset view





#ajax check
def FormSetFactory(request):
    print('this is testing 11111')
    FormsetFactory = formset_factory(student,extra=4)

    if request.method == 'POST':
        formset = FormsetFactory(request.POST,request.FILES)
        print('this is testing 2222')
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                roll = form.cleaned_data.get('roll')
                blog=Blog.objects.create(name=name,tagline=roll)
                blog.save()
            return HttpResponse('/blog/')
    else:
        formset=FormsetFactory
    return render(request,'formsetfactory.html',{'formset':formset})





class FormsetFactoryView(FormView):
    # initial = {'name': 'ramesh', 'roll': '1'}
    # Formset=initial)
    # form_class = FormsetFactory
    template_name = 'formsetfactory.html'
    success_url = '/'

    # if form_valid(self,form):
    #     if self.request.method =='POST':







class FormTestView(FormView):
    form_class = FormTest
    template_name = 'formtest.html'
    success_url = '/'


class BlogView(FormView):
    form_class = BlogForm
    success_url = '/'
    template_name = 'geolocation.html'


def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.save()
    return super().form_valid(form)

#pagination example is here
class EntryView(TemplateView):
    # model = Entry
    template_name='entry.html'

    def dispatch(self,request,*args,**kwargs):
        contact_list = Entry.entries.all()
        paginator = Paginator(contact_list,3,orphans=2,allow_empty_first_page=True)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts=paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {'contacts': contacts})

def extraarguments(request,num):
    return HttpResponse(num +'extra argumnents' )

def nestedarguments(request,num):
    return HttpResponse(num +'nested argumnents' )

def projectcreate(request,num):
    return HttpResponse(num +'project create' )

def projectupdate(request,num):
    return HttpResponse(num +'project update')

def defaultarguments(request,year='2017',month='9'):
    return HttpResponse(year + '' + month)

def year_archive(request,year,month):
    return HttpResponse(year + '' + month)

def articles(request,year,month,day):
    return HttpResponse(year+month+day)

def keywordarguments(request,month,year):
    return HttpResponse(year+month)

decorators=[never_cache,login_required]
@method_decorator(decorators,name='dispatch')
class multiple_decorators(DetailView):
    template_name='login.html'


class templateview(TemplateView):
    template_name='login.html'

    @method_decorator(never_cache)
    def dispatch(self,*args, **kwargs):
        return super(templateview, self).dispatch(*args, **kwargs)



class Myview(View):
    result = 'hello'
    def get(self,request):

        return HttpResponse(self.result)
class replyview(Myview):
    result='this is reply'

class class_form(View):
    form_class=login_form
    initial={'username':'ramesh'}
    template_name='login.html'

    def get(self,request,*args,**kwargs):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    def post (self,request,*args,**kwargs):
        form=self.for_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data('username')
            return HttpResponse(' the username is %s '%username)
        return render(request,self.template_name,{'form':form})




def insert_bike(request):
    form=product_insert_form()
    if request.method=='POST':

        form = product_insert_form(request.POST,request.FILES)
        if form.is_valid():

            return HttpResponseRedirect('/')
        form.email = form.cleaned_data['email']

    return render(request,'bike_form.html',{'form':form})


def email(request):
    send_mail(subject='hello',message='this is message',from_email='admin@gmail.com',recipient_list=['rdramesh2009@gmail.com'],fail_silently=False,auth_user='rdramesh2009@gmail.com',auth_password='futureheroes')

# def homepage(request):
#
#     #cla=request.class
#     return HttpResponse("the app is %s "%(app_label))

def homepage(request):

    return render(request,'homepage.html')


def register(request):
    if request.method=='POST':
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form=register_form()
    return render(request,'register.html',{'form':form,'current_model':model_now})

def login(request):#since login is name while calling login(request,user) error saying login takes 1 but 2 args were given appeared.ao we changed django import to auth_login
    if request.method=='POST':

        form=login_form(data=request.POST)
        if form.is_valid():

            email=form.cleaned_data['email']
            raw_password=form.cleaned_data['password']
            auth=CustomUserAuth()
            user=auth.authenticate(email=email,password=raw_password)
            user.backend=settings.AUTHENTICATION_BACKENDS
            auth_login(request,user)
            username=user.email
            password=user.password
            return HttpResponseRedirect('/')

            return HttpResponse('new user is logged in%s  %s'%(email,password))
        else:
            return HttpResponse('form is not valid')
    else:
        form=login_form()
    return render(request,'login.html',{'form':form })


# rest framework examples
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your views here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class pygments_examples(FormView):
    template_name = 'restframework.html'
    form_class = PygmentForm

    # def get(self,request):
    #     print(LEXERS)
    #     print(LANGUAGE_CHOICES)
    #     print(STYLE_CHOICES)
    #     return HttpResponse(LANGUAGE_CHOICES)