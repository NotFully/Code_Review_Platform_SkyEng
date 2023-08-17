from django import forms
from .models import File, ReviewComment


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', )


class ReviewCommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
        fields = ('review_text', )
