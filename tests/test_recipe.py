from lib.recipe import Recipe

"""
Recipe constructs with an id, name and genre
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 5, 10)
    assert recipe.id == 1
    assert recipe.name == "Test Recipe"
    assert recipe.average_cooking_time == 5
    assert recipe.rating == 10

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Recipe", 5, 10)
    assert str(recipe) == "Recipe(1, Test Recipe, 5, 10)"
    # Try commenting out the `__repr__` method in lib/recipe.py
    # And see what happens when you run this test again.

"""
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test Recipe", 5, 10)
    recipe2 = Recipe(1, "Test Recipe", 5, 10)
    assert recipe1 == recipe2
    # Try commenting out the `__eq__` method in lib/recipe.py
    # And see what happens when you run this test again.
