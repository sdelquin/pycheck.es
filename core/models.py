from django.db import models


class Context(models.Model):
    # 2022-2023/IESPTO/DAW/PRO
    # 2023-1/EOI/NAC
    code = models.SlugField(unique=True, max_length=32)
    name = models.CharField(unique=True, max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    max_score = models.DecimalField(decimal_places=2, max_digits=5, default=10)  # 3!
    score_limit = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        default=10,
        help_text='Número de ejercicios a completar correctamente para conseguir'
        ' "max_score" puntos',
    )


class Student(models.Model):
    username = models.SlugField(unique=True, max_length=32)
    password_hash = models.CharField(max_length=32)  # md5
    context = models.ForeignKey(Context, on_delete=models.PROTECT, related_name='students')
    last_active = models.DateTimeField(blank=True, null=True)


class Section(models.Model):
    name = models.CharField(max_length=32)
    start_date = models.DateField()
    context = models.ForeignKey(Context, on_delete=models.PROTECT, related_name='sections')
