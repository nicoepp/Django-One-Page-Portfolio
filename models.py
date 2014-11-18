# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Project(models.Model):
	""" model for projects """
	category = models.ForeignKey("Category", related_name="projects", null=True)
	name = models.CharField(max_length=128, unique=True)
	img = models.ImageField(upload_to='proj_img')
	description = models.TextField()
	link = models.TextField()

	def __unicode__(self):
		return self.name

  # path to specific project
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('core.views.project', args=[str(self.id)])

class Category(models.Model):
	""" model for categories """
	name = models.CharField(max_length=128, unique=True, help_text="Name of the category")
	description = models.TextField()
	img = models.ImageField(upload_to='cat_img')

	def __unicode__(self):
		return self.name

  # path to specific category
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('core.views.category', args=[str(self.id)])

class Contact(models.Model):
	""" model for contact form """
	mail = models.EmailField(help_text="Your E-Mail")
	copy = models.TextField(help_text="Your Message")
	sender = models.CharField(max_length=128, help_text="Your Name")

	def __unicode__(self):
		return self.sender

class AboutMe(models.Model):
	""" model for about me """
	name = models.CharField(max_length=128, help_text="Username")
	img = models.ImageField(upload_to='about_img')
	quote = models.TextField()	
	
	def __unicode__(self):
		return self.name
	
