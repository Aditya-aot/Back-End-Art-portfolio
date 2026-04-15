from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Artwork
from django import forms
from django.utils.html import format_html


class ArtworkAdminForm(forms.ModelForm):
    types = forms.MultipleChoiceField(
        choices=Artwork.ART_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Artwork
        fields = '__all__'

    def clean_types(self):
        return ",".join(self.cleaned_data['types'])



class ArtworkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'type_display','date', 'order', 'preview_image', 'id')

    # 👇 allows editing order manually
    list_editable = ('order',)

    # 👇 ensures ordering is consistent
    ordering = ('-order',)

    form = ArtworkAdminForm 


    def preview_image(self, obj):
        if obj.preview:
            return format_html('<img src="{}" width="60" />', obj.preview.url)
        return "-"
    
    def type_display(self, obj):
        return obj.get_types_display()


admin.site.register(Artwork, ArtworkAdmin)