from django.contrib import admin
from cmsapp.models import Carousel,Cards,About,Contact,Photogallery

# Register your models here.
# admin.site.register(Carousel)

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id','image','title']

@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ['id','photo','description']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','aboutpic','aboutdesc']

# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['sno','name','email','phone','document','desc','time']
    

# admin.site.register(Photogallery)
    # both styles are ok for all data registration im admin 

@admin.register(Photogallery)
class PhotogalleryAdmin(admin.ModelAdmin):
    list_display = ['id','photogallery','phototitle']
    
    

    
    
    

    

