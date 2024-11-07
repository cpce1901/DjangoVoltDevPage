from django.contrib import admin
from .models import Materials, Unit, Provider, Boss, Items, Budget

# Inlines
class ItemsInlines(admin.TabularInline):
    autocomplete_fields = ('item', )
    model = Items
    extra = 4


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    search_fields = ('description', )

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    pass

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    exclude = ('total_price', )

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    search_fields = ('project_name', 'boss__name')
    list_display = ('project_name', 'boss', 'file', 'show_total_budget', 'created')
    exclude = ('total_budget', 'file')
    readonly_fields = ('created', )
    inlines = [ItemsInlines, ]

    @admin.display(description='total')
    def show_total_budget(self, obj):
        total = obj.total_budget if obj.total_budget is not None else 0
        return f"${int(total):,}".replace(",", ".")
