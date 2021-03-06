from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm password')

    class Meta:
        model = User
        fields = ['email',]
    def clead_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('email is take')
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label_suffix = "", widget = forms.PasswordInput)
    password2 = forms.CharField(label_suffix = "", widget = forms.PasswordInput)
    class  Meta:
        model = User
        fields = ['email',]
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit = True):
        user = super(UserAdminCreationForm,self).save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('email', 'password','active','admin')
    def clean_password(self):
        return self.initial["password"]
