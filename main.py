from datetime import datetime as dt
import datetime

today = dt.today().year


def info(num): # Store the info in 2D and return list
    two = []
    while (num != 0):
        name = input("Enter name: ")
        date1 = input("Enter date:")
        date1 = date1.split('-')
        date2 = datetime.date(int(date1[-1]), int(date1[-2]), int(date1[-3]))
        two = two + [[name, date2]]
        num -= 1
    return two


def age(date):#return age
    return today - date.year


def name_age_list(name, date):#return 2D List [name,age]

    two_dim_ageL = two_dim_list + [[name, age(date)]]
    return two_dim_ageL


def age_list(list_dates):#
    age_list1 = []
    for i in range(0, num):
        age_list1 = age_list1 + [today - list_dates[i].year]
    return age_list1


def splitLists(list2D):
    listname = []
    listage = []
    for i in range(0, num):
        listname = listname + [list2D[i][0]]
        listage = listage + [list2D[i][1]]
    return  listname,listage


def oldest(list2D:list):
    listname,listage=splitLists(list2D)
    listage = age_list(listage)
    max_age = max(listage)
    max_index = listage.index(max_age)
    return listname[max_index]


def oldest_order(list2d):# print order list from the oldest
    ListName,ListAge=splitLists(list2d)
    ListAge=age_list(ListAge)
    OrderList=[]
    for i in range(num):
        max_age = max(ListAge)
        max_index = ListAge.index(max_age)
        OrderList.append([ListName[max_index],ListAge[max_index]])
        del ListName[max_index]
        del  ListAge[max_index]
    return OrderList


def SunBirth(List2D): #people who born on sunday
    SunList=[]
    for i in range(num):
        if List2D[i][1].strftime('%A')=="Sunday":
            SunList.append(List2D[i][0])
    print(f"These guys born on Sunday {SunList}")


def print_info(name, date):
    print(f"{name} is {age(date)} years old and she/he was born on {date.strftime('%A')}")


if __name__ == '__main__':#main
    num = int(input("Enter number of person:"))
    two_dim_list = info(num)
    for i in range(0, num):
        print_info(two_dim_list[i][0], two_dim_list[i][1])
        two_dim_ageL = name_age_list(two_dim_list[i][0], two_dim_list[i][1])
    print(f"The youngest one is {oldest(two_dim_list)}")
    print(f"Total People:{num}")
    # EXTRA Qs
    print(oldest_order(two_dim_ageL))
    two_dim_list.reverse()
    SunBirth(two_dim_list ) #SunBirth must be here since its Datatime.datatime type
    for i in range(num):
       two_dim_list[i][1]=two_dim_list[i][1].strftime('%Y %m %d')
    print(two_dim_list)
    # SunBirth(two_dim_list) DATES IN STR





