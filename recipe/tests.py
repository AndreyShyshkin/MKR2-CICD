from django.test import TestCase
from recipe.models import Category, Recipe

class RecipeAppTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")

    def test_recipe_creation(self):
        category = Category.objects.create(name="Soup")
        recipe = Recipe.objects.create(
            title="Tomato Soup",
            description="A warm and delicious soup.",
            instructions="Boil tomatoes, blend, add seasoning.",
            ingredients="Tomatoes, water, salt, pepper",
            category=category
        )
        self.assertEqual(recipe.title, "Tomato Soup")
        self.assertEqual(recipe.description, "A warm and delicious soup.")
        self.assertEqual(recipe.instructions, "Boil tomatoes, blend, add seasoning.")
        self.assertEqual(recipe.ingredients, "Tomatoes, water, salt, pepper")
        self.assertEqual(recipe.category, category)
        self.assertEqual(str(recipe), "Tomato Soup")
        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)

    def test_category_iteration(self):
        category = Category.objects.create(name="Salads")
        recipe1 = Recipe.objects.create(
            title="Caesar Salad",
            description="Classic Caesar salad.",
            instructions="Mix ingredients, add Caesar dressing.",
            ingredients="Romaine lettuce, croutons, parmesan, caesar dressing",
            category=category
        )
        recipe2 = Recipe.objects.create(
            title="Greek Salad",
            description="Healthy Greek salad.",
            instructions="Chop vegetables, mix with feta and olives.",
            ingredients="Tomatoes, cucumbers, onions, olives, feta, olive oil",
            category=category
        )
        
        # Check iteration yields all recipes in Category
        recipes = list(category)
        self.assertEqual(len(recipes), 2)
        self.assertIn(recipe1, recipes)
        self.assertIn(recipe2, recipes)
