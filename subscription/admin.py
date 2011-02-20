# encoding: utf-8
import datetime
from django.contrib import admin
from subscription.models import Subscription
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.http import HttpResponse
from django.conf.urls.defaults import patterns, url

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ['created_at', 'paid']
    
    actions = ['mark_as_paid']
    
    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()
               
    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True
    
    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        msg = ungettext (
            u'%(count)d inscrição foi marcada como paga.',
            u'%(count)d inscrições foram marcadas como pagas.',
            count) % {'count': count}
        self.message_user(request, msg)
        
    mark_as_paid.short_description = _(u'Marcar como pagas')      
    
    def export_subscriptions(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions] #list comprehension
        response = HttpResponse('\r\n'.join(rows))
        response.mimetype = 'text/csv'
        response['Content-Disposition'] = 'attachment; filename=inscritos.csv'
        
        return response
        
    def get_urls(self):
        default_urls = super(SubscriptionAdmin, self).get_urls()
        new_urls = patterns('', 
            url(r'^exportar-inscricoes/$', self.admin_site.admin_view(self.export_subscriptions),
            name='export_subscriptions'))
            
        return new_urls + default_urls            
        

admin.site.register(Subscription, SubscriptionAdmin)
