from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html

AuthUserModel = get_user_model()


# class RegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=128, required=True, label='First name')
#     last_name = forms.CharField(max_length=128, required=True, label='Last name')
#     username = forms.CharField(max_length=128, required=True, label='Username')
#     password = forms.CharField(
#         max_length=128,
#         required=True,
#         label='Password',
#         widget=forms.PasswordInput,
#         help_text=password_validators_help_text_html()
#     )
#     password_confirmation = forms.CharField(
#         max_length=128,
#         required=True,
#         label='Confirm password',
#         widget=forms.PasswordInput
#     )
#
#     # validate username
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#
#         try:
#             AuthUserModel.objects.get(username=username)
#         except AuthUserModel.DoesNotExist:
#             return username
#
#         raise forms.ValidationError(f'{username} already exists!')
#
#     def clean_password(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         password = self.cleaned_data.get('password')
#
#         user = AuthUserModel(
#             first_name=first_name,
#             last_name=last_name,
#         )
#
#         validate_password(password, user=user)
#
#         return password
#
#     # validate confirmation_password
#     def clean_password_confirmation(self):
#         password = self.cleaned_data.get('password')
#         password_confirmation = self.cleaned_data.get('password_confirmation')
#
#         if password != password_confirmation:
#             raise forms.ValidationError('Password not confirmed.')
#
#         return password_confirmation
#
#     def save(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         # DON'T DO IT -> PASSWORD WILL BE CLEAN IN DB
#         # user = AuthUserModel(
#         #     first_name=first_name,
#         #     last_name=last_name,
#         #     username=username,
#         #     password=password,
#         # )
#         # user.save()
#
#         # DON'T DO IT -> PASSWORD WILL BE CLEAN IN DB
#         # user = AuthUserModel.objects.create(
#         #     first_name=first_name,
#         #     last_name=last_name,
#         #     username=username,
#         #     password=password,
#         # )
#
#         # user = AuthUserModel(
#         #     first_name=first_name,
#         #     last_name=last_name,
#         #     username=username,
#         # )
#         # user.set_password(password)
#         # user.save()
#
#         user = AuthUserModel.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             password=password,
#         )
#
#         return user

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = AuthUserModel
#         fields = ['first_name', 'last_name', 'username']
#         # exclude = []
#
#     password = forms.CharField(
#         max_length=128,
#         required=True,
#         label='Password',
#         widget=forms.PasswordInput,
#         help_text=password_validators_help_text_html()
#     )
#
#     password_confirmation = forms.CharField(
#         max_length=128,
#         required=True,
#         label='Confirm password',
#         widget=forms.PasswordInput
#     )
#
#     def clean_password(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         password = self.cleaned_data.get('password')
#
#         user = AuthUserModel(
#             first_name=first_name,
#             last_name=last_name,
#         )
#
#         validate_password(password, user=user)
#
#         return password
#
#     def clean_password_confirmation(self):
#         password = self.cleaned_data.get('password')
#         password_confirmation = self.cleaned_data.get('password_confirmation')
#
#         if password != password_confirmation:
#             raise forms.ValidationError('Password not confirmed.')
#
#         return password_confirmation
#
#     def save(self, commit=True):
#         password = self.cleaned_data['password']
#
#         user = super(forms.ModelForm, self).save(commit=False)
#         user.set_password(password)
#         user.save()
#
#         return user


class RegisterForm(UserCreationForm):
    class Meta:
        model = AuthUserModel
        fields = ['first_name', 'last_name', 'username']
