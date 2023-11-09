from django import forms

from .models import Category, Post


class PostForm(forms.ModelForm):
    """
    Форма заполнения бланков потраченных средств
    """
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ("name", "category", "price", "quant")

    def save(self, commit: bool = True):
        post_form = super(PostForm, self).save(commit=False)
        post_form.amount = post_form.price * post_form.quant
        if commit:
            return post_form.save()
        return post_form
