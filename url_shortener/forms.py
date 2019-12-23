from django import forms
from .models import Url
import os
from .form_utils import get_clean_short_url, get_absolute_short_path


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["short_url", "text", "clicks"]

        widgets = {
            "short_url": forms.TextInput(attrs={"class": "form-control"}),
            "clicks": forms.NumberInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_short_url(self):
        cleaned_short_url = get_clean_short_url(self.cleaned_data["short_url"])

        return get_absolute_short_path(cleaned_short_url)


class UrlFormCreate(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["original_url", "short_url"]

        widgets = {
            "short_url": forms.TextInput(
                attrs={
                    "class": "form-control pl-4 pr-4",
                    "placeholder": "Your short URL(optional)",
                }
            ),
            "original_url": forms.URLInput(
                attrs={"class": "form-control  pl-4 pr-4", "placeholder": "Your URL"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(UrlFormCreate, self).__init__(*args, **kwargs)
        self.fields["short_url"].required = False

    def clean_short_url(self):
        cleaned_short_url = get_clean_short_url(self.cleaned_data["short_url"])

        return get_absolute_short_path(cleaned_short_url)
