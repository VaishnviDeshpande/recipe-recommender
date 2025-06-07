def recommend_recipes(df, user_ingredients):
    user_ingredients = [i.strip().lower() for i in user_ingredients]
    results = []

    for _, row in df.iterrows():
        recipe_ingredients = [x.strip().lower() for x in row['ingredients'].split(',')]
        match_count = len(set(user_ingredients) & set(recipe_ingredients))

        if match_count > 0:
            results.append({
                'name': row['name'],
                'ingredients': row['ingredients'],
                'steps': row['steps'],
                'match_score': match_count
            })

    # Sort by most matched ingredients
    results.sort(key=lambda x: x['match_score'], reverse=True)

    return results[:5]  # top 5 matched recipes
