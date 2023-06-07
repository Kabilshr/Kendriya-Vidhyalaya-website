from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TC)
admin.site.register(principals_message)
admin.site.register(Holiday)
admin.site.register(Alumni)
admin.site.register(Class)
admin.site.register(News_letter)
admin.site.register(vmc_member)
admin.site.register(member_list)
admin.site.register(Vacancy)
admin.site.register(Notice)
admin.site.register(Fee_structure)
admin.site.register(Carousel_image)
admin.site.register(News_and_Events,News_and_Events_GalleryAdmin)
admin.site.register(Images)
admin.site.register(Gallery,News_and_Events_GalleryAdmin)
admin.site.register(Committies)

