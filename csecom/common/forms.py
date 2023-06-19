from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    student_id = forms.CharField(label='학번', max_length=10)
    name = forms.CharField(label='이름', max_length=20)
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('student_id', 'name',)

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        qs = User.objects.filter(student_id=student_id)
        if qs.exists():
            raise forms.ValidationError('이미 존재하는 학번입니다.')
        return student_id

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('student_id', 'name', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']
