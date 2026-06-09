from django import forms
from .models import Student

class DummyForm(forms.Form):
    name = forms.CharField(
        max_length=100
    )
    age = forms.IntegerField()
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError(
                "Age must be at least 18"
            )
        return age
    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"