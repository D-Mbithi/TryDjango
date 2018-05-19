from django import forms
from pagedown.widgets import PagedownWidget
from blog.models import Post


class PostForm(forms.ModelForm):
    published = forms.DateField(widget=forms.SelectDateWidget)
    post = forms.CharField(widget=PagedownWidget(show_preview=False))

    class Meta:
        model = Post
        fields = ['title', 'images', 'post', 'draft', 'published']
