import csv
import datetime
import numpy
import sys

var = sys.argv[1]


with open(var) as f:
   reader = csv.reader(f,delimiter=';')
   n= 0
   days = []
   data = [['Product', 'Sales', 'Quantity', 'Profit'],]
   profit = 0
   max_sales = 0
   max_sales_prod =""
   max_quantity = 0
   max_quantity_prod= ""
   max_profit = 0
   max_profit_prod = ""
   min_sales = 9999999999999999
   min_sales_prod = ""
   min_quantity = 9999999999999999
   min_quantity_prod = ""
   min_profit = 9999999999999999
   min_profit_prod = ""


   for row in reader:

       n +=1
       if n ==1:
           continue
       row[20]= float(row[20].replace(',', '.'))
       row[19]= float(row[19].replace(',', '.'))
       row[18]= float(row[18].replace(',', '.'))
       row[17]= float(row[17].replace(',', '.'))
       profit += row[20]
       if row[17] > max_sales:
           max_sales = row[17]
           max_sales_prod = row[15]
       elif row[17] < min_sales:
           min_sales = row[17]
           min_sales_prod = row[15]
       if row[18] >  max_quantity:
           max_quantity = row[18]
           max_quantity_prod = row[15]
       elif row[18]< min_quantity:
           min_quantity =row[18]
           min_quantity_prod = row[15]
       if row[20] > max_profit:
           max_profit = row[20]
           max_profit_prod = row[15]
       elif row[20] < min_profit:
           min_profit = row[20]
           min_profit_prod = row[15]
       a = row[3].split("/")
       b = row[2].split("/")
       aa = datetime.datetime(int(a[2]),int(a[0]),int(a[1]))
       bb = datetime.datetime(int(b[2]),int(b[0]),int(b[1]))
       cc = aa - bb
       days.append(cc.days)
       data.append([row[15],row[17],row[18],row[20]])


avdays = numpy.mean(days)
std = numpy.std(days)


print(int(profit))
print(max_sales_prod)
print(max_quantity_prod)
print(max_profit_prod)
print(min_sales_prod)
print(min_quantity_prod)
print(min_profit_prod)
print(avdays)
print(std)
with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
