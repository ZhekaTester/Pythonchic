def is_year_leap(year):
    return year % 4 == 0

year_to_check = 2020
result = is_year_leap(year_to_check)

print(f"Год {year_to_check}: {result}")