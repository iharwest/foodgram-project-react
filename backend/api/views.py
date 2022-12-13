from django.db.models import Sum
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from recipes.models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                            ShoppingList, Tag)

from .filters import IngredientFilter, RecipeFilter
from .pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (TagSerializer, IngredientSerializer,
                          RecipeSerializer, CreateRecipeSerializer)
from .utils import get_post, get_delete


class TagViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class IngredientViewSet(TagViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filterset_class = IngredientFilter


class FavouriteViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, recipe_id):
        return get_post(request, recipe_id, Favorite)

    def delete(self, request, recipe_id):
        return get_delete(request, recipe_id, Favorite)


class ShoppingListViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, recipe_id):
        return get_post(request, recipe_id, ShoppingList)

    def delete(self, request, recipe_id):
        return get_delete(request, recipe_id, ShoppingList)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecipeSerializer
        return CreateRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context


class DownloadShoppingCart(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        buying_list = {}
        recipe_id = request.user.purchases.values_list('recipe__id')
        ingredients = IngredientInRecipe.objects.filter(recipe__in=recipe_id)
        ingredients = ingredients.values(
            'ingredient',
            'ingredient__name',
            'ingredient__measurement_unit'
        )
        ingredients = ingredients.annotate(sum_amount=Sum('amount'))
        for ingredient in ingredients:
            sum_amount = ingredient.get('sum_amount')
            name = ingredient.get('ingredient__name')
            measurement_unit = ingredient.get('ingredient__measurement_unit')
            if name not in buying_list:
                buying_list[name] = {
                    'measurement_unit': measurement_unit,
                    'sum_amount': sum_amount
                }
        wishlist = []
        for item in buying_list:
            wishlist.append(f'{item} - {buying_list[item]["sum_amount"]} '
                            f'{buying_list[item]["measurement_unit"]} \n')
        wishlist.append('\n')
        wishlist.append('FoodGram Service')
        response = HttpResponse(wishlist, 'Content-Type: text/plain')
        response['Content-Disposition'] = 'attachment; filename="wishlist.txt"'
        return response
