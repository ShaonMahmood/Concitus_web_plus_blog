from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title','slug','status','text','tags',)

    # def clean_slug(self):
    #     slug = self.cleaned_data.get('slug', '')
    #     existing = Post.objects.filter(slug=slug)
    #     if len(existing):
    #         raise forms.ValidationError(
    #             "Slug already exits",
    #             code='invalid'
    #         )
    #     return slug


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


