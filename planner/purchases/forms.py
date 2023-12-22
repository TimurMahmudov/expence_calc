from django import forms

from .models import Category, Post


class PostForm(forms.ModelForm):
    """
    Форма заполнения бланков потраченных средств
    """
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label="Выберите категорию")

    class Meta:
        model = Post
        fields = ("name", "category", "price", "quant")
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Введите наименование продукта"
            }),
            "price": forms.NumberInput(attrs={
                "placeholder": "Укажите цену"
            }),
            "quant": forms.NumberInput(attrs={
                "placeholder": "Укажите кол-во/массу"
            })
        }

    def save(self, commit: bool = True):
        post_form = super(PostForm, self).save(commit=False)
        post_form.amount = post_form.price * post_form.quant
        if commit:
            return post_form.save()
        return post_form
