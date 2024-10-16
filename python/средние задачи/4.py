from datetime import datetime

def is_valid_date(date: str):
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return "date format is correct"
    except ValueError:
        return "date format is not correct"

date = input("input the date in dd.mm.yyyy format: ")
print(is_valid_date(date))
