from django.contrib import admin

from .models import Call, Category, Subcategory


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (SubcategoryInline,)
    list_display = ('__str__',)
    search_fields = ('title',)
    date_hierarchy = 'created'


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category')
    search_fields = ('title',)
    list_filter = ('category',)
    date_hierarchy = 'created'


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'status')
    search_fields = ('title', 'description')
    list_filter = ('status',)
    date_hierarchy = 'created'
