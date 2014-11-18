# -*- encoding: utf-8 -*-
from django.contrib import admin
from core.models import Project, Category, Contact, AboutMe

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
  ''' panel for project in admin view '''

	# Group All Available Information
	Gruppiert die Übersicht mit mehr Informationen
	list_display = ('name', 'description', 'category', 'img', 'link')

	# Group input fields
	fieldsets = [
		('Create new project', {
				'fields': ['name', 'description', 'category', 'img', 'link']
		})]

	def save_model(self, request, obj, form, change):
		super(ProjectAdmin, self).save_model(request, obj, form, change)
		
class CategoryAdmin(admin.ModelAdmin):
  ''' panel for category in admin view '''
	
	# Group All Available Information
	list_display = ('name', 'description', 'img')

	# Group input fields
	fieldsets = [
		('Create new category', {
				'fields': ['name', 'description', 'img']
		})]

	def save_model(self, request, obj, form, change):
		super(CategoryAdmin, self).save_model(request, obj, form, change)

class AboutMeAdmin(admin.ModelAdmin):
  ''' panel for about me in admin view '''
	
	# Group All Available Information
	list_display = ('name', 'img',  'quote')

	# Group input fields
	fieldsets = [
		('Create new user', {
				'fields': ['name', 'img', 'quote']
		})]

	def save_model(self, request, obj, form, change):
		super(AboutMeAdmin, self).save_model(request, obj, form, change)

# Register Models For Admin Panel
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
