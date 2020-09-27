from django import forms

from PostApp.models import Posts, Catagory


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'catagory', 'body']

        widgets = {
            'title': forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'Post title goes here...'
            })),
            'catagory': forms.Select(attrs=({
                'class': 'form-control',
                'placeholder': 'Body text goes here...'
            })),
            'body': forms.Textarea(attrs=({
                'class': 'form-control',
                'placeholder': 'Body text goes here...'
            }))
        }


class EditCatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ['name',]

        widgets = {
            'name': forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'add new catagroy...'
            }))
        }