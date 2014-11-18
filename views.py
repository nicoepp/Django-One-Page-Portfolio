# -*- encoding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from core.models import Category, Project, AboutMe

# Create your views here.

def index(request):
	''' Generates content for index.html '''
	context = RequestContext(request)
	categories = Category.objects.all()
	projects = Project.objects.all()
	aboutme = get_object_or_404(AboutMe, name='Your Name') # Replace Your Name for the name in your database
	context_dict = {
		'headline': 'Portfolio',
		'message': 'Message one your website',
		'categories': categories,
		'projects': projects,
		'aboutme': aboutme,
	}
	return render_to_response('core/index.html', context_dict, context)
