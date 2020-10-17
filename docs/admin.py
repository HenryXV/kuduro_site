from django.contrib import admin

from .models import Category, Command, Usage, Option, Example, Alias

class UsageInline(admin.TabularInline):
    model = Usage

class OptionInline(admin.TabularInline):
    model = Option

class ExampleInline(admin.TabularInline):
    model = Example

class AliasInline(admin.TabularInline):
    model = Alias

class CommandAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['command_name']}),
        ('Command information', {'fields': ['command_category', 'command_info']}),
    ]

    inlines = [UsageInline, OptionInline, ExampleInline, AliasInline]
    list_display = ('command_name', 'command_category', 'command_info')
    search_fields = ['command_name']

admin.site.register(Category)
admin.site.register(Command, CommandAdmin)
