from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Motivation)

admin.site.register(Pastors)

admin.site.register(DonationAndOffering)


admin.site.register(ChurchPrograms)

admin.site.register(UpcomingEvents)
admin.site.register(ContactUs)



class ImageGalleryAdmin(admin.StackedInline):
    model = ImageGallery


@admin.register(ChurchGallery)
class ChurchProgrammAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryAdmin]

    #class Meta:
    #   model =ChurchGallery


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    pass




'''
from django.contrib import admin
from .models import ChurchGallery, ImageGallery

class ImageGalleryInline(admin.StackedInline):
    model = ImageGallery
    extra = 1
    fields = ('img',)

class ChurchGalleryAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline,]

admin.site.register(ChurchGallery, ChurchGalleryAdmin)
'''
