from django.contrib import admin
from .models import HomeSettingModel, FeedbackModel, GuideModel, HitsCountModel, TotalHitsModel


class HitsCountModelAdmin(admin.ModelAdmin):
    list_display = ['ip', 'mac', 'created', 'updated', 'count']


class TotalHitsModelAdmin(admin.ModelAdmin):
    list_display = ['date', 'hits']


admin.site.register(HitsCountModel, HitsCountModelAdmin)
admin.site.register(TotalHitsModel, TotalHitsModelAdmin)
admin.site.register(HomeSettingModel)
admin.site.register(FeedbackModel)
admin.site.register(GuideModel)
