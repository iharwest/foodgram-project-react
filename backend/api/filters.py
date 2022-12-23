from django_filters.rest_framework import FilterSet, filters
from django_filters.widgets import BooleanWidget
from recipes.models import Ingredient, Recipe
from users.models import User


class IngredientFilter(FilterSet):
    """Фильтр для ингридиентов."""

    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    """Фильтр для рецептов."""

    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug'
    )
    is_favorited = filters.BooleanFilter(widget=BooleanWidget())
    is_in_shopping_cart = filters.BooleanFilter(widget=BooleanWidget())

    class Meta:
        model = Recipe
        fields = ('is_favorited', 'is_in_shopping_cart', 'author', 'tags')
