# from .models import  MyUser
# from django.contrib.auth.backends import ModelBackend
# class CustomUserAuth(object):
#
#     def authenticate(self,email=None,password=None):
#         try:
#             user=MyUser.objects.get(email =email)
#             if user.check_password(password):
#                 return user
#         except MyUser.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         try:
#             return MyUser.objects.get(pk=user_id)
#         except MyUser.DoesNotExist:
#             return None
#
# from django.conf import settings
# from django.contrib.auth import get_user_model
#
# class CustomUserAuth(object):
#     """
#     This is a ModelBacked that allows authentication with either a username or an email address.
#
#     """
#     def authenticate(self, username=None, password=None):
#         if '@' in username:
#             kwargs = {'email': username}
#         else:
#             kwargs = {'username': username}
#         try:
#             user = get_user_model().objects.get(**kwargs)
#             if user.check_password(password):
#                 return user
#         except MyUser.DoesNotExist:
#             return None
#
#     def get_user(self, email):
#         try:
#             return get_user_model().objects.get(pk=email)
#         except get_user_model().DoesNotExist:
#             return None