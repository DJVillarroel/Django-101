from django import forms

class PostForm(forms.Form):
    img = forms.FileField()
    text = forms.CharField(label="title", max_length=30)