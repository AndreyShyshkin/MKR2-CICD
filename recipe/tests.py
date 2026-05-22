from django.test import TestCase
from recipe.models import Category, Recipe

class RecipeAppTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")
