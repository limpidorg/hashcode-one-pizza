preferences = [
    [('cheese', 'peppers'), ()],
    [('basil',), ('pineapple',)],
    [('mushrooms', 'tomatoes'), ('basil',)],
]

ingredients = ('cheese', 'peppers', 'basil',
               'tomatoes', 'pineapple', 'mushrooms')

userscores = [0, 0, 0]


def calculateIngredientImpact(ingredient, preferences, currentUserScores):
    impact = 0
    for user in range(len(preferences)):
        if ingredient in preferences[user][0]:
            numberOfIngredients = len(preferences[user][0])
            impact += 1 / numberOfIngredients
        elif ingredient in preferences[user][1]:
            impact -= currentUserScores[user]
    return impact


for ingredient in ingredients:
    print(ingredient, calculateIngredientImpact(
        ingredient, preferences, userscores))
