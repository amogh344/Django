
# # from django import forms
# # from .models import Student
# # from django.contrib.auth.models import User
# # from django.contrib.auth.hashers import make_password
# # from django.contrib.auth import authenticate


# # class ContactForm(forms.Form):
# #     name = forms.CharField(
# #         label='Name',
# #         max_length=40,
# #         widget=forms.TextInput(attrs={
# #             'class': 'form-control',
# #             'placeholder': 'Username',
# #             'required': True
# #         })
# #     )
# #     email = forms.EmailField(
# #         label='Email',
# #         max_length=40,
# #         widget=forms.EmailInput(attrs={
# #             'class': 'form-control',
# #             'placeholder': 'Email',
# #             'required': True
# #         })
# #     )
# #     message = forms.CharField(
# #         label='Message',
# #         max_length=200,
# #         widget=forms.Textarea(attrs={
# #             'class': 'form-control',
# #             'placeholder': 'Your message',
# #             'required': True
# #         })
# #     )

# #     def clean(self):
# #         cleaned_data = super().clean()
# #         name = cleaned_data.get('name')
# #         if name and len(name) < 3:
# #             raise forms.ValidationError('Name must be at least 3 characters long.')
# #         return cleaned_data


# # class RegisterForm(forms.ModelForm):
# #     confirm_password = forms.CharField(
# #         label='',
# #         max_length=50,
# #         widget=forms.PasswordInput(attrs={
# #             'type': 'password',
# #             'class': 'form-control',
# #             'placeholder': 'Confirm Password',
# #             'required': True
# #         })
# #     )

# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password']
# #         widgets = {
# #             'username': forms.TextInput(attrs={
# #                 'type': 'text',
# #                 'class': 'form-control',
# #                 'placeholder': 'Username',
# #                 'required': True
# #             }),
# #             'email': forms.EmailInput(attrs={
# #                 'type': 'email',
# #                 'class': 'form-control',
# #                 'placeholder': 'Email',
# #                 'required': True
# #             }),
# #             'password': forms.PasswordInput(attrs={
# #                 'type': 'password',
# #                 'class': 'form-control',
# #                 'placeholder': 'Password',
# #                 'required': True
# #             }),
# #         }
# #         labels = {
# #             'username': '',
# #             'email': '',
# #             'password': '',
# #         }
# #         help_texts = {
# #             'username': '',
# #             'email': '',
# #             'password': '',
# #         }

# #     def clean(self):
# #         cleaned_data = super().clean()
# #         password = cleaned_data.get('password')
# #         confirm_password = cleaned_data.get('confirm_password')

# #         if password and confirm_password and password != confirm_password:
# #             raise forms.ValidationError("Passwords do not match.")
# #         return cleaned_data

# #     def save(self, commit=True):
# #         user = super().save(commit=False)
# #         user.password = make_password(self.cleaned_data['password'])  
# #         if commit:
# #             user.save()
# #         return user


# # # 🔒 Old LoginForm (Commented Out)
# # # class LoginForm(forms.Form):
# # #     username = forms.CharField(
# # #         label='',
# # #         max_length=50,
# # #         widget=forms.TextInput(attrs={
# # #             'type': 'text',
# # #             'class': 'form-control',
# # #             'placeholder': 'Username',
# # #             'required': True
# # #         })
# # #     )
# # #     password = forms.CharField(
# # #         label='',
# # #         max_length=50,
# # #         widget=forms.PasswordInput(attrs={
# # #             'type': 'password',
# # #             'class': 'form-control',
# # #             'placeholder': 'Password',
# # #             'required': True
# # #         })
# # #     )

# # #     def clean(self):
# # #         cleaned_data = super().clean()
# # #         username = cleaned_data.get('username')
# # #         password = cleaned_data.get('password')

# # #         if username and password:
# # #             try:
# # #                 User = User.objects.get(username=username)
# # #                 if not check_password(password, User.password):
# # #                     raise forms.ValidationError("Invalid username or password.")
# # #             except User.DoesNotExist:
# # #                 raise forms.ValidationError("Invalid username or password.")
# # #         return cleaned_data


# # # ✅ Updated LoginForm using `authenticate`
# # class LoginForm(forms.Form):
# #     username = forms.CharField(
# #         label='',
# #         max_length=50,
# #         widget=forms.TextInput(attrs={
# #             'type': 'text',
# #             'class': 'form-control',
# #             'placeholder': 'Username',
# #             'required': True
# #         })
# #     )
# #     password = forms.CharField(
# #         label='',
# #         max_length=50,
# #         widget=forms.PasswordInput(attrs={
# #             'type': 'password',
# #             'class': 'form-control',
# #             'placeholder': 'Password',
# #             'required': True
# #         })
# #     )

# #     def clean(self):
# #         cleaned_data = super().clean()
# #         username = cleaned_data.get('username')
# #         password = cleaned_data.get('password')

# #         if username and password:
# #             user = authenticate(username=username, password=password)
# #             if user is None:
# #                 raise forms.ValidationError("Invalid username or password.")
# #         return cleaned_data


# # class StudentForm(forms.ModelForm):
# #     class Meta:
# #         model = Student
# #         fields = ['username', 'email', 'password']
# #         widgets = {
# #             'username': forms.TextInput(attrs={'class': 'form-control'}),
# #             'email': forms.EmailInput(attrs={'class': 'form-control'}),
# #             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
# #         }

# #     def save(self, commit=True):
# #         student = super().save(commit=False)
# #         student.password = make_password(self.cleaned_data['password'])
# #         if commit:
# #             student.save()
# #         return student


# from django import forms
# from .models import Student
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         label='',
#         max_length=40,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Name',
#             'required': True
#         })
#     )
#     email = forms.EmailField(
#         label='',
#         max_length=40,
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Email',
#             'required': True
#         })
#     )
#     message = forms.CharField(
#         label='',
#         max_length=200,
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': 'Your message',
#             'required': True
#         })
#     )

#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         if name and len(name) < 3:
#             raise forms.ValidationError('Name must be at least 3 characters long.')
#         return cleaned_data


# class RegisterForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         label='',
#         max_length=50,
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Confirm Password',
#             'required': True
#         })
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Username',
#                 'required': True
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email',
#                 'required': True
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password',
#                 'required': True
#             }),
#         }
#         labels = {
#             'username': '',
#             'email': '',
#             'password': '',
#         }
#         help_texts = {
#             'username': '',
#             'email': '',
#             'password': '',
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.password = make_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user


# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label='',
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Username',
#             'required': True
#         })
#     )
#     password = forms.CharField(
#         label='',
#         max_length=50,
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Password',
#             'required': True
#         })
#     )

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user is None:
#                 raise forms.ValidationError("Invalid username or password.")
#         return cleaned_data


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

#     def save(self, commit=True):
#         student = super().save(commit=False)
#         student.password = make_password(self.cleaned_data['password'])
#         if commit:
#             student.save()
#         return student



from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=40,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'required': True
        })
    )
    email = forms.EmailField(
        label='',
        max_length=40,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': True
        })
    )
    message = forms.CharField(
        label='',
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your message',
            'required': True
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name and len(name) < 3:
            raise ValidationError('Name must be at least 3 characters long.')
        return cleaned_data

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'required': True
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': True
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': True
            }),
        }
        labels = {
            'username': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'username': '',
            'email': '',
            'password': '',
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': True
        })
    )
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password.")
        return cleaned_data

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data['password'])
        if commit:
            student.save()
        return student