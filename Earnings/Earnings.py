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
Платежи по кварталам
Требуется реализовать метод оценки затрат по кварталам.
Дано счетов за услуги в 2022 год. Каждый счет характеризуется тремя параметрами: ,
, – начало оказание услуги, последний день оказания услуги, размер оплаты.
Необходимо платежи разложить пропорционально дням внутри интервала оказания услуги и
просуммировать по кварталам (деление до копеек необходимо выполнять с округлением вниз, т.е.
сумма по кварталам может быть меньше общей суммы по счетам). Сначала необходимо определить
сумму платежа за один день, а затем округленную сумму прибавить к каждому из дней квартала.
Обратите внимание: 2022 год – не високосный.
Формат ввода
В первой строке находится одно число – количество счетов.
В следующих строках заданы описания счетов: в рублях, ,
. Даты заданы в формате dd.mm (день, месяц).
Формат вывода
Выведите 4 числа, каждое в новой строке, ровно с 2 десятичным знаками – сумма платежей в 1-м, 2-м,
3-м и 4-м кварталах соответственно.
Пример 1
Ввод
4
10 10.02 11.05
10 11.12 23.12
100 24.05 30.06
4342 10.07 12.09
Вывод
5.00
104.04
4342.00
9.88
Пример 2
Ввод
1
1000000 01.01 31.12
Вывод
246574.80
249314.52
252054.24
252054.24
Пример 3
Ввод
n dateFromi
dateFinishi amount
n (1 ≤ n ≤ 10 )
5
n amount (1 ≤ amount ≤ 10 )
6 dateFromi
dateFinishi
2
1000 01.01 01.01
1234 30.06 01.07
Вывод
1000.00
617.00
617.00
0.00
Ограничение памяти
256.0 Мб
Ограничение времени
6 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.tx
