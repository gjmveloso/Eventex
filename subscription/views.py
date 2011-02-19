# coding: utf-8
# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from subscription.models import Subscription
from subscription.forms import SubscriptionForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

def subscribe(request):
    if request.method == "POST":
        return create(request)
    else:
        return new(request)
    
def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form':form})
    return render_to_response('subscription/new.html', context)
    
def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        context = RequestContext(request, {'form':form})
        return render_to_response('subscription/new.html', context)
    
    subscription = form.save()
    send_subscription_confirmation(subscription)
    return HttpResponseRedirect(reverse('subscription:success', args=[subscription.pk]))

def send_subscription_confirmation(subscription):
    send_mail(
        subject = u'EventeX - Confirmação de inscrição',
        message = u'{0}, obrigado por se inscrever no EventeX!'.format(subscription.name),
        from_email = "no-reply@eventex.com.br",
        recipient_list = [subscription.email],
    )

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription':subscription})
    return render_to_response('subscription/success.html', context)
    
    
     
        
    
              
    
    
