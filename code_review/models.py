from django.db import models
from core.models import CreatedModel
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class File(CreatedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    file = models.FileField(
        upload_to='uploaded_files/',
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=['py'])],
    )

    class Meta:
        ordering = ['-pub_date']


class ReviewComment(CreatedModel):
    review_text = models.TextField(
        verbose_name='Текст ревью',
    )
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review_text[:15]

