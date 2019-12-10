from datetime import *

def main():
    # myDate = datetime(2019, 12, 10).isoweekday()
    # # myDate.isoweekday()
    # print(myDate)

    # next_day = datetime(2019, 12, 10) + 1
    # print(next_day)

    a = 2019
    b = 12
    c = 10
    abc = str(a) + str(b) + str(c)
    # abc = int(abc)
    print("abc = " + abc)
    print(type(abc))

    x = str(((datetime.strptime(abc, "%Y%m%d")) + timedelta(days=-1)).strftime("%Y%m%d"))
    # x = datetime.strptime(abc, "%Y%m%d")
    # x2 = x + timedelta(days=-1)
    # x3 = str(x2.strftime("%Y%m%d"))
    new_year = x[:4]
    new_month = x[4:6]
    new_day = x[6:]
    print("x = " + str(x))
    # print("x2 = " + str(x2))
    # print("x3 = " + x3)
    # print(type(x3))
    print("new_year = " + new_year)
    # print(type(new_year))
    print("new_month = " + new_month)
    # print(type(new_month))
    print("new_day = " + new_day)
    # print(type(new_day))

if __name__ == '__main__':
    main()