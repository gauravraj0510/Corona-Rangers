from django import forms
from .models import Post,Category, Donation

choices = Category.objects.all().values_list('name','name')

choice_list =[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','category','content')

        widgets = {

            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'})
        
        }

class Form(forms.ModelForm):
    quantity= forms.IntegerField()
    class Meta:
        model= Donation
        fields=('quantity',)