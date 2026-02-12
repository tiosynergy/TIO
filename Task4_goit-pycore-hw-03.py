import datetime
from datetime import datetime, date, timedelta

users = [
    {"name": "Alice Johnson", "birthday": "1992.02.08"},
    {"name": "Bob Williams", "birthday": "1988.02.14"},
    {"name": "Charlie Brown", "birthday": "1988.02.09"},
    {"name": "Diana Evans", "birthday": "1995.02.08"},
    {"name": "Ethan Foster", "birthday": "1980.01.14"},
    {"name": "Fiona Garcia", "birthday": "1998.09.05"},
    {"name": "George Harris", "birthday": "1987.02.25"},
    {"name": "Hannah Irving", "birthday": "1993.04.18"},
    {"name": "Ivan Kuznetsenko", "birthday": "1984.06.30"},
    {"name": "Julia Lopez", "birthday": "1991.08.12"}
]
now=datetime.now().date()
def get_upcoming_birthdays(user): #/ user - DICT словарь 
    user_birth_dt_format=({"name":user["name"],"birthday":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})
    birthday=user_birth_dt_format["birthday"]

    user_birthday_this_year=({"name":user["name"],"birthday":datetime(now.year,birthday.month,birthday.day)})

    if 0<= (user_birthday_this_year["birthday"].date() - now).days <=7:
        congratulattion_date=user_birthday_this_year
        congratulattion_date["r_b"]=user["birthday"]
        print(type(congratulattion_date["r_b"]))

        if user_birthday_this_year["birthday"].weekday()==5:

           new_date=user_birthday_this_year["birthday"].date()+timedelta(days=2)
           congratulattion_date=({"name":user["name"],"birthday":datetime(now.year,new_date.month,new_date.day),"r_b":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})

        if congratulattion_date["birthday"].weekday()==6:
            new_date=user_birthday_this_year["birthday"].date()+timedelta(days=2)
            congratulattion_date=({"name":user["name"],"birthday":datetime(now.year,new_date.month,new_date.day),"r_b":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})
        return(congratulattion_date)

upcoming_birthdays=[get_upcoming_birthdays(user_birthday) for user_birthday in users]

print("\nСписок привітань на цьому тижні:\n ")

i=0
for birthday in upcoming_birthdays:
    if birthday:
        print(f"{birthday["name"]}, день народження {birthday["r_b"]} : привітати {birthday["birthday"].date()}\n")
        i=i+1