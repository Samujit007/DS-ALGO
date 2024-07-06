def kids_with_max_cadies(candies, extraCandies):
    max_can = max(candies)
    for idx, each in enumerate(candies):
        if each+extraCandies >= max_can:
            candies[idx] = True
        else:
            candies[idx] = False

    return candies

candies = [2,3,5,1,3]
extraCandies = 3

print(kids_with_max_cadies(candies, extraCandies))