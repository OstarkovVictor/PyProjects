import calendar
import math



counter_days, counter_season1, counter_season2, counter_season3, counter_season4, sum_season1, sum_season2, sum_season3, sum_season4= 0, 0, 0, 0, 0, 0.00, 0.00, 0.00, 0.00

import sys
in_params = sys.stdin.readline().strip()
for day_iter in range(int(in_params)):

    array_in_dates = []
    counter_days, counter_season1, counter_season2, counter_season3, counter_season4= 0, 0, 0, 0, 0
    in_date = sys.stdin.readline().strip()
    array_in_dates=(in_date.split())



    array_in_dates[1] = array_in_dates[1].split(".")

    array_in_dates[2] = array_in_dates[2].split(".")



    earn_in_period = float(array_in_dates[0])
    start_day = int(array_in_dates[1][0])
    start_month = int(array_in_dates[1][1])
    finish_day = int(array_in_dates[2][0])
    finish_month = int(array_in_dates[2][1])


    for month_iter in range(start_month, finish_month + 1):
        days_in_month = calendar.monthrange(2022, month_iter)
        if (month_iter == finish_month):
            days_in_month = (0, finish_day)

        for day_iter in range(start_day, days_in_month[1] + 1):
            counter_days+=1

            if (month_iter == 1) or (month_iter == 2) or (month_iter == 3):
                counter_season1+=1
            if (month_iter == 4) or (month_iter == 5) or (month_iter == 6):
                counter_season2+=1
            if (month_iter == 7) or (month_iter == 8) or (month_iter == 9):
                counter_season3+=1
            if (month_iter == 10) or (month_iter == 11) or (month_iter == 12):
                counter_season4+=1



        start_day = 1

    earn_in_period = float(((math.floor((earn_in_period / counter_days) * 100))))

    sum_season1 += (earn_in_period * counter_season1)
    sum_season2 += (earn_in_period * counter_season2)
    sum_season3 += (earn_in_period * counter_season3)
    sum_season4 += (earn_in_period * counter_season4)
print((sum_season1 / 100))
print((sum_season2 / 100))
print((sum_season3 / 100))
print((sum_season4 / 100))