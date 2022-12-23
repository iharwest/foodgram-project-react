from django.contrib import admin

from recipes.models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                            ShoppingCart, Tag)


class IngredientInRecipeInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInRecipeInline,)
    list_display = (
        'name',
        'author'
    )
    list_filter = (
        'author',
        'name',
        'tags'
    )
    readonly_fields = ('is_favorited',)

    def is_favorited(self, instance):
        return instance.favorite_recipes.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit'
    )
    search_fields = ('measurement_unit',)
    list_filter = ('measurement_unit',)


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'ingredient',
        'recipe',
        'amount'
    )
    search_fields = ('recipe__name', 'ingredient__name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug'
    )
    list_filter = ('name', 'color', 'slug')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipe'
    )
    search_fields = (
        'user__username',
        'user__email',
        'recipe__name'
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipe'
    )
    search_fields = (
        'user__username',
        'user__email',
        'recipe__name'
    )
