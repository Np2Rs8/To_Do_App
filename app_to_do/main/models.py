
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

#Modelo de la tabla
class TaskModel(models.Model):
    
    class Meta:
        verbose_name_plural = 'Tasks_lists'
        verbose_name = 'Task_list'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    id_usuario = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    estado = models.CharField(max_length=50, default="Incompleto")
    cuerpo = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.descripcion)
        super(TaskModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return f"/creacionTareas/{self.slug}"



    