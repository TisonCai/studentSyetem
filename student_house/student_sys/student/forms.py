from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    def clean_QQ(self):
        cleaned_data = self.cleaned_data["QQ"]
        if not cleaned_data.digit():
            raise forms.ValidationError('必须是数字')

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = ('name','sex','profession','email','QQ','phone')