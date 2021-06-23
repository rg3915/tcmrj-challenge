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
    list_display = ('__str__', 'user', 'get_category', 'subcategory', 'status')
    search_fields = ('title', 'description')
    list_filter = ('status', 'subcategory')
    date_hierarchy = 'created'

    @admin.display(description='Categoria')
    def get_category(self, obj):
        return obj.subcategory.category
