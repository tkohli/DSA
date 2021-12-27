"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
"""


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = {recipe: [] for recipe in recipes}
        supplies = set(supplies)
        can_make = {}

        def dfs(recipe):
            if recipe not in can_make:
                can_make[recipe] = False
                can_make[recipe] = all([dfs(ingr) for ingr in graph[recipe]])
            return can_make[recipe]
        for i, recipe in enumerate(recipes):
            for ingr in ingredients[i]:
                if ingr not in supplies:
                    graph[recipe].append(ingr if ingr in graph else recipe)
        return [recipe for recipe in recipes if dfs(recipe)]
        # out = []
        # for idx, ind in enumerate(ingredients):
        #     found = True
        #     for i in ind:
        #         if i not in supplies:
        #             found = False
        #     if found:
        #         out.append(recipes[idx])
        #         supplies.append(recipes[idx])
        # for idx, ind in enumerate(ingredients):
        #     if ind in out:
        #         continue
        #     found = True
        #     for i in ind:
        #         if i not in supplies:
        #             found = False
        #     if found and recipes[idx] not in out :
        #         out.append(recipes[idx])
        #         supplies.append(recipes[idx])
        # return (out)
