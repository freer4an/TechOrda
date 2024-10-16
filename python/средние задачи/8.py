def which_season(day, month):
    seasons = {
        "Winter": [(12, 1, 2)],
        "Spring": [(3, 4, 5)],
        "Summer": [(6, 7, 8)],
        "Autumn": [(9, 10, 11)]
    }
    
    for season, months in seasons.items():
        if month in months[0]:
            return season

day = 10
month = int(input("month = "))

season = which_season(day, month)
print(f"{day}.{month} belongs to: {season}")