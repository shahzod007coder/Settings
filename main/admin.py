from django.contrib import admin
from main.models import Categoriya


# @admin.register(Categoriya)
# class CategoriyaAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'img', 'text',"time","price"]
#
#     class Meta:
#         model = Categoriya


admin.site.register(Categoriya)