from django import forms
from .models import Article, BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name', 'user_email', 'content']

        widgets = {
            'user_name': forms.TextInput(),
            'user_email': forms.EmailInput(),
            'content': forms.Textarea()
        }
