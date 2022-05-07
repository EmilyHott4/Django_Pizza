from django import forms
from .models import Comment

class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        labels = {'comment_text':''}
        widgets = {'comment_text': forms.Textarea(attrs={'cols':80})}