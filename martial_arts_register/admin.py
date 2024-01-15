from django.contrib import admin
from .models import MartialArt, Motherland, Artist, Technique, Embodyment
from django.apps import apps

# Register your models here.


class MartialArtsAdmin(admin.ModelAdmin):

    # in admin panel field "slug" will be visible for
    # admin and how it's created depands on fields which
    # i input here in tuple, i.e. slug consists of "name"
    # and anything in very same tuple
    prepopulated_fields = {"slug": ("name", )}

    list_filter = ("rating", "country_of_origin")
    list_display = ("name", "rating", "country_of_origin",
                    "joint_locks_allowed")


class MotherlandAdmin(admin.ModelAdmin):
    list_filter = ("name", "continent")
    list_display = ("name", "continent")


class TechniqueAdmin(admin.ModelAdmin):
    list_display = ("name", "effective_range", "originating_martial_art")

# class ArtistAdmin(admin.ModelAdmin):
#     list_display= ("first_name", "last_name", "motherland", "birth_year")


class EmbodymentAdmin(admin.ModelAdmin):
    list_display: ("feature_name", )


# this is for displaying MartialArt settings
# for admin in django admin panel
admin.site.register(MartialArt, MartialArtsAdmin)
admin.site.register(Motherland, MotherlandAdmin)
admin.site.register(Technique, TechniqueAdmin)
# admin.site.register(Artist, ArtistAdmin)
admin.site.register(Embodyment, EmbodymentAdmin)
