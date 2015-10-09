import csv

csvfile = open('e:/test.csv', 'w', newline='')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [('jack2', 28, '151511111'),
        ('张芳2', 11, '112222222')]
writer.writerows(data)
csvfile.close()

print('执行成功!')