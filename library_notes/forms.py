from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from library_notes.models import Content, Theme


class ContentForm(forms.ModelForm):
      """Form for comments to the article."""

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["content"].required = False

      class Meta:
          model = Content
          fields = ("theme", "name", "content", "is_published")
          widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"
              )
          }


class ThemeForm(forms.ModelForm):
      """Form for comments to the article."""

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

      class Meta:
          model = Theme
          fields = ("name",)