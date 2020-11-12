from django.contrib import admin

# Register your models here.
from company.models import Employ_Form, Employ_Form2, Employ_Form3, Review, Job


admin.site.register(Employ_Form),
admin.site.register(Employ_Form2),
admin.site.register(Employ_Form3),


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('image','name', 'logo', 'rating_figures', 'rating', 'location', 'work', 'work1', 'work2', 'work3', 'work4', 'loc1', 'loc2', 'loc3', 'loc4', 'job1', 'job2', 'job3','description', 'url',)
    readonly_fields = ('created_date', 'updated_date')
admin.site.register(Review, ReviewAdmin),

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'company', 'company2', 'company3','location', 'amount', 'requirements', 'details', 'url',)
    readonly_fields = ('created_date', 'updated_date')
admin.site.register(Job, JobAdmin)