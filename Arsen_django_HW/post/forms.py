from . models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'rate', 'category', 'tags']
        labels = {'image': 'Image',
                  'title': 'Title',
                  'content': 'Content',
                  'rate': 'Rate',
                  'category': 'Category',
                  'tags': 'Tags'}
        widgets = {'tags': forms.CheckboxSelectMultiple()}


    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0 or rate > 5:
            raise forms.ValidationError("Rate must be between 1 and 5.")
        return rate


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment'}
