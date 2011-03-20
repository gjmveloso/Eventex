from django.db import models
from django.utils.translation import ugettext as _
import datetime

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    description = models.TextField(blank=True)
    avatar = models.FileField(upload_to='palestrantes', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Palestrante'
    
    def __unicode__(self):
        return self.name
        
class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind
        
    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs.filter = kind=self.kind
        return qs        
        
class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')))
    speaker = models.ForeignKey(Speaker, verbose_name=_('Palestrante'))
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)
    
    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
    
class PeriodManager(models.Manager):
    midday = datetime.time(12)
    
    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = self.order_by('start_time')
        return qs
        
    def at_afternoon(self):
        qs = self.filter(start_time__gt=self.midday)
        qs = self.order_by('start_time')
        return qs

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))
    
    objects = PeriodManager()
    
    class Meta:
        verbose_name = 'Palestra'
    
    def __unicode__(self):
        return unicode(self.title)
        
class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()
    
    class Meta:
        verbose_name = 'Curso'
    
        
    
    
