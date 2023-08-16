from django.db import models


class CreatedModel(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Дата загрузки на ревью',
        auto_now_add=True
    )

    class Meta:
        abstract = True
