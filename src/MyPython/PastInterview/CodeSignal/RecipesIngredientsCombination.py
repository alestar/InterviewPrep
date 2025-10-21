"""
In cooking terms, recipe is a prep-list combination of ingredients if you can prepare it by mixing together the first several ingredients from your list, one after another, starting from the very beginning.
 More formally, string recipe is a prep-list combination of array of strings ingredients if there is some index i ≥ 0 such that
  recipe = ingredients[0] + ingredients[1] + ... + ingredients[i].

For example, consider an array ingredients = ["flour", "sugar", "eggs"].
recipe = "flour" is a prep-list combination of the ingredients array, as ingredients[0] = recipe = "flour",
recipe = "floursugar" is a prep-list combination of the ingredients array, as ingredients[0] + ingredients[1] = recipe = "floursugar",
recipe = "floursug" is not a prep-list combination of the ingredients array,
recipe = "floureggs" is not a prep-list combination of the ingredients array.

Task: Given two arrays of  ingredients and recipes, for each recipe in recipes, find out whether it is a prep-list combination of ingredients.
As a result, return an array of length recipes.length, where the ith element is true if recipes[i] is a prep-list combination of ingredients, and false otherwise.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(ingredients.length2 × recipes.length) will fit within the execution time limit.

Example:
For ingredients = ["flour", "sugar", "eggs"]
and recipes = ["floursugar", "random", "flour", "sugarflour", "sugareggs"],

the output should be:
 solution(ingredients, recipes) = [true, false, true, false, false].

recipes[0] = "floursugar" is a prep-list combination, as ingredients[0] + ingredients[1] = recipes[0] = "floursugar", so 'true' is appended to the result.
recipes[1] = "random" is not a prep-list combination, so 'false' is appended to the result.
recipes[2] = "flour" is a prep-list combination, as ingredients[0] = recipes[2] = "flour", so 'true' is appended to the result.
recipes[3] = "sugarflour" is not a prep-list combination.It may be obtained by evaluating ingredients[1] + ingredients[0], but it is not a consecutive combination. So 'false' is appended to the result.
recipes[4] = "sugareggs" is not a prep-list combination. It may be obtained by evaluating ingredients[1] + ingredients[2],but it is not a combination of the first ingredients of the ingredients array, as it doesn't start with ingredients[0].So 'false' is appended to the result.

 Thus, the resulting array is [true, false, true, false, false].

Input/Output [execution time limit] 4 seconds (py3) [memory limit] 1 GB [input] array.string ingredients An array of ingredients.
It is guaranteed that each element only consists of English letters.
Guaranteed constraints: 1 ≤ ingredients.length ≤ 100, 1 ≤ ingredients[i].length ≤ 100. [input] array.string recipes An array of recipes.
It is guaranteed that each element only consists of English letters. Guaranteed constraints: 1 ≤ recipes.length ≤ 100, 1 ≤ recipes[i].length ≤ 100.
"""

def solution(ingredients, recipes):
    # Precompute the prefix combinations of ingredients
    prefix_combinations = set()
    current_combination = ""

    for ingredient in ingredients:
        current_combination += ingredient
        prefix_combinations.add(current_combination)

    # Check each recipe against the precomputed combinations
    result = []
    for recipe in recipes:
        if recipe in prefix_combinations:
            result.append(True)
        else:
            result.append(False)

    return result

# Example usage:
ingredients = ["flour", "sugar", "eggs"]
recipes = ["floursugar", "random", "flour", "sugarflour", "sugareggs"]
print(solution(ingredients, recipes))  # Output: [True, False, True, False, False]