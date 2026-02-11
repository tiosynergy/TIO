import datetime
from datetime import datetime

def get_days_from_today(date):
    current_date=datetime.now().date()
    dlt=current_date-date.date()
    return dlt.days

input_year=int(input("Введіть рік: "))
input_month=int(input("Введіть міяць: "))
input_day=int(input("Введіть день: "))

input_date=datetime(input_year,input_month,input_day)
print(get_days_from_today(input_date))
