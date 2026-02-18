import datetime
from datetime import datetime, date, timedelta


#-------- Початок фуункції кого з колег потрібно привітати----
def get_upcoming_birthdays(user) ->list: #/ user - словник 
    now=datetime.now().date()

#---------приведення user до типу Datetime--------------------
    birthday=datetime.strptime(user["birthday"],"%Y.%m.%d").date()

#--------визначення дня народження колеги в поточномуу році----
    user_birthday_this_year=({"name":user["name"],"birthday":datetime(now.year,birthday.month,birthday.day)})

#-------перевірка чи ДР ве минув---------------------------
    if user_birthday_this_year["birthday"].date()<now:
        print(f"\nДень народження {user_birthday_this_year['name']} в цьому році минув")
        user_birthday_next_year=({"name":user["name"],"birthday":datetime(now.year+1,birthday.month,birthday.day)})
        print(f"Наступний день народження {user_birthday_next_year["birthday"].date()}")

#------- Якщо наступний ДР у субботу, переноситься на поенділок----------
        if user_birthday_next_year["birthday"].weekday()==5:
           new_date_next_year=user_birthday_next_year["birthday"].date()+timedelta(days=2)
           congratulattion_date=({"name":user["name"],"birthday":datetime(new_date_next_year.year,new_date_next_year.month,new_date_next_year.day),"r_b":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})
           print(f"Привітання {congratulattion_date["birthday"].date()}\n")
           
#------- Якщо наступний ДР у неділю, переноситься на поенділок----------
        if user_birthday_next_year["birthday"].weekday()==6:
           new_date_next_year=user_birthday_next_year["birthday"].date()+timedelta(days=1)
           congratulattion_date=({"name":user["name"],"birthday":datetime(new_date_next_year.year,new_date_next_year.month,new_date_next_year.day),"r_b":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})
           print(f"Привітання {congratulattion_date["birthday"].date()}\n")

#-------визначення семи днів та дати привітання --------------
    if 0<= (user_birthday_this_year["birthday"].date() - now).days <=7:
        congratulattion_date=user_birthday_this_year
        congratulattion_date["r_b"]=user["birthday"]

#------- якщо ДР припадає на суботу +2 дні-----------
        if user_birthday_this_year["birthday"].weekday()==5:
           new_date=user_birthday_this_year["birthday"].date()+timedelta(days=2)
           congratulattion_date=({"name":user["name"],"birthday":datetime(now.year,new_date.month,new_date.day),"r_b":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})

#------- якщо ДР припадає на неділю +1 день-----------
        if congratulattion_date["birthday"].weekday()==6:
            new_date=user_birthday_this_year["birthday"].date()+timedelta(days=1)
            congratulattion_date=({"name":user["name"],"birthday":datetime(now.year,new_date.month,new_date.day),"r_b":datetime.strptime(user["birthday"],"%Y.%m.%d").date()})
        return(congratulattion_date) #---- повернення списку словників

if __name__ == "__main__":
#-------------інформація про ім'я користувача та його день народження------
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

    #--------Визначення поточної дати системи--------------------



#-------- виклик функцїї обчислення-----------------
upcoming_birthdays=[get_upcoming_birthdays(user_birthday) for user_birthday in users]

#----------виведення кого з колег потрібно привітати--------
print("\nСписок привітань на цьому тижні:\n ")
for birthday in upcoming_birthdays:
    if birthday:
        print(f"{birthday["name"]}, день народження {birthday["r_b"]} : привітати {birthday["birthday"].date()}\n")
