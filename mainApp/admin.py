from django.contrib import admin
from django import forms
from mainApp.models import InfoPage, Item
from ckeditor.widgets import CKEditorWidget


class ItemAdminForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget())
    order = str(forms.IntegerField)

    class Meta:
        model = Item
        fields = ('page', 'headline', 'element_id', 'order', 'text')


class ItemAdmin(admin.ModelAdmin):

    list_display = ('page', 'order', 'headline', 'element_id')
    search_fields = ('headline', 'element_id')
    ordering = ('page', 'order')
    form = ItemAdminForm


admin.site.register(Item, ItemAdmin)
admin.site.register(InfoPage)
