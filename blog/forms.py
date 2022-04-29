from django import forms
from .models import Comment

class CommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Enter your content',
        'id':'usercomment',
        'rows':'4'
    }))

    class Meta:
        model=Comment
        fields=('content', )


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


    