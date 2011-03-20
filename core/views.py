# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from core.models import Talk

def homepage(request):
    context = RequestContext(request)   
    return render_to_response('homepage.html', context)
    
def speaker(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = RequestContext(request, {'speaker': speaker})
    return render_to_response('core/speaker.html', context)
    
def talks(request):
    return direct_to_template(request, 'core/talks.html', {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(), })
    
    

