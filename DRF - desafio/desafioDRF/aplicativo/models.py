from django.db import models

# Create your models here.

class Afazeres(models.Model):
    nome = models.CharField(max_length=30)
    status = models.BooleanField(verbose_name=('feito'), default=False)
    data = models.DateField(verbose_name="Data de lancamento")
