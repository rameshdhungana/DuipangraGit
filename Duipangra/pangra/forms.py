from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory,BaseFormSet


class login_form(forms.Form):

    #email=forms.EmailField(max_length=64,help_text="Email address will be verified")
    username=forms.CharField(max_length=64,help_text="Email address will be verified")
    password=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        #fields=('email','password')
        #fields='__all__'


        # widgets = {
        #         'password': forms.PasswordInput(), ## we can provide widgets through meta class too
        #     }

class register_form(UserCreationForm):
    # email=forms.EmailField(max_length=64,help_text="Email address will be verified")

    class Meta:
        model=User
        #fields=('email',)
        fields='__all__'


class product_insert_form(forms.Form):
    city_options=(('chitwan','chitwan'),
                  ('kathmandu','kathmandu'),
                  ('bhaktapur','bhaktapur'),
                  ('lamjung', 'lamjung'),)
    price_negotiable_options=(('yes','Yes'),
                              ('no','No'),)
    conditions_options=(('new','New'),
                  ('like new','Like New'),
                  ('good','Good Condition'),
                  ('not working', 'Not Working'),)
    adtype_options= (('buy','Want to Buy'),
                              ('sell','Want to Sell'),)

    email=forms.EmailField()
    #lot_no=forms.CharField(max_length=16)
    #kilometers_used=forms.CharField(max_length=64)
    #vehicle_color=forms.CharField(max_length=64)
    #engine_cc=forms.CharField(max_length=64)
    #price=forms.IntegerField(max_value=9999999999)
    #market_price=forms.IntegerField(max_value=9999999999)
    #is_price_negotiable=forms.ChoiceField(widget=forms.RadioSelect,choices=price_negotiable_options)
    #condition=forms.ChoiceField(widget=forms.RadioSelect,choices=conditions_options)
    #ad_type=forms.ChoiceField(widget=forms.RadioSelect,choices=adtype_options)
    #contact_number=forms.IntegerField(max_value=30)
    #image=forms.ImageField()






    def clean_price(self):
        lot_no=self.cleaned_data['price']
        if lot_no< 100:
            raise forms.ValidationError('price is less than 100')
        return lot_no
class CalendarWidget(forms.TextInput):
    class Media:
        css = {
        'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')

class BlogForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Blog
        widgets={'name':CalendarWidget(),
                 }



class FormTest(forms.Form):
    first_name = forms.CharField(max_length=10,help_text='Enter First Name')
    last_name = forms.CharField(max_length=10,help_text="Enter Last Name")
    email=forms.EmailField()

    def clean(self):
        cleaned_data = super(FormTest,self).clean()
        first_name=cleaned_data.get('first_name')
        last_name=cleaned_data.get('last_name')
        if first_name!=last_name:
            raise forms.ValidationError('Enter both surname and first name same')

class student(forms.Form):
    name = forms.CharField(max_length=40)
    roll = forms.CharField(max_length=40)

class BaseFormFactory (BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        titles=[]
        for form in self.forms:
            title=form.cleaned_data.get('name')
            if title in titles:
                raise forms.ValidationError('duplication in tilte')
            titles.append(title)


# FormsetFactory = formset_factory(student,extra=4,max_num=6)

# Formsettest = FormsetFactory(initial=[{'name':'ramesh',
#                                         'roll':'1'}])


class EntryForm(forms.ModelForm):
    authors =  forms.CharField(max_length=10)


    class Meta:
        model=Entry
        fields=['authors']

# class MultipleForm(forms.ModelForm,forms.Form):
#     name=forms.CharField(max_length=39)
#
#
#     class Meta:
#        model=EntryForm
#        exclude=('authors',)
class CalendarWidget(forms.TextInput):
    class Media:
        css = {
        'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')

class CustomerSignUpForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder':  'Name'}))

    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={'class': 'form-control', 'placeholder':  'Email Address'}))
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder':  'Password'}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder':  'Confirm Password'}))
    #
    # def clean(self):
    #     cleaned_data = super(CustomerSignUpForm, self).clean()
    #     email = cleaned_data.get("email")
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     try:
    #         User.objects.get(email=email)
    #         raise forms.ValidationError(
    #             "Email address already in use")
    #     except User.DoesNotExist:
    #         pass

        # if password != confirm_password:
        #     raise forms.ValidationError(
        #         "Password and confirm password does not match")


class PygmentForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = '__all__'