from django.contrib import admin

from .models import DappCategory, Dapp, ToolCategory, Tool, SuggestedTool


admin.site.register(DappCategory)
admin.site.register(Dapp)
admin.site.register(ToolCategory)
admin.site.register(Tool)
admin.site.register(SuggestedTool)
