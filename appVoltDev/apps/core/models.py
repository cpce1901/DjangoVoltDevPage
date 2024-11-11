from django.db import models
from django.core.exceptions import ValidationError


class PersonalImagen(models.Model):
    name = models.CharField('Nombre', max_length=100)
    imagen = models.ImageField('Imagen Personal', upload_to='personal/')

    class Meta:
        verbose_name = 'Imagen Personal'
        verbose_name_plural = 'Imagen Personales'

    def save(self, *args, **kwargs):
        if not self.pk and PersonalImagen.objects.exists():
            raise ValidationError('Solo se permite un registro en esta base de datos.')
        super(PersonalImagen, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class PersonalCV(models.Model):
    name = models.CharField('Nombre', max_length=100)
    doc = models.FileField('Curriculum')

    class Meta:
        verbose_name = 'Cv Personal'
        verbose_name_plural = 'Cvs Personales'

    
    def __str__(self):
        return f'{self.name}'


class Tags(models.Model):
    name = models.CharField('Tag', max_length=128)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Tags, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Projects(models.Model):
    title = models.CharField('Titulo', max_length=255)
    tags= models.ManyToManyField(Tags, verbose_name='Marcas')
    year = models.PositiveIntegerField('Año')
    details = models.TextField('Detalles')
    image = models.ImageField('imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return f'{self.title}'