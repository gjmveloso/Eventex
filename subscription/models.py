# encoding: utf-8

from django.db import models
from subscription import validators

# Create your models here.

class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True, validators=[validators.CpfValidator])
    email = models.EmailField('E-mail', unique=True, blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('Data inscrição', auto_now_add=True)
    #paid = models.BooleanField('Pagou?', default=False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["created_at"]
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições"
        

