import csv, os, sys, time

# 支付方式
HF  = '话费'
SJ  = '手机'
ZFB = '支付宝'
QT  = '其他'
# 普通费率
CP  = 0.03
# 输出文件title
title = ['商户', '总金额 ', 
         '话费金额 ',   '移动费率', '移动收入',  
         '手机金额',   '移动费率', '移动收入', 
         '支付宝金额 ', '移动费率', '移动收入' , 
         '积分金额 ',  '移动费率', '移动收入' ,
         '移动总收入']

### 读取csv file
def readCsv(path, mode='r'):
    result = [];
    if isCsvFile(path):
        csvfile = open(path, mode, newline='')
        reader = csv.reader(csvfile)
        count = 0;
        for row in reader:
            if count > 0 :
                result.append(row);
            count += 1
            #print (','.join(row))
        
    return result


### 写入csv file
def writeCsv(path, mode='w', title=[], data=[]):
    csvfile = open(path, mode, newline='')
    writer = csv.writer(csvfile)
    writer.writerow(title)
    for one in data:
        writer.writerow(one)
    csvfile.close()

### 是否为csv文件
def isCsvFile(path):
    if os.path.isfile(path) and path.endswith('.csv'):
        return True
    return False    


### 读取配置文件
def readConfig():
    configPath = input('请输入分润配置文件路径(如e:/config.csv)：\n')
    while not isCsvFile(configPath) :
        configPath = input('文件路径错误！请重新输入:\n')
    
    print('开始读取配置...\n')    
    configData = readCsv(configPath)
    config = {}
    for row in configData :
        if row[0] == '':
            continue
        config[row[0]] = row
    return config

### 读取配置文件
def readData():
    dataPath = input('请输入数据文件路径(如e:/data.csv)：\n')
    while not isCsvFile(dataPath) :
        dataPath = input('文件路径错误！请重新输入:\n')
    
    print('开始读取数据...\n')    
    data = readCsv(dataPath)
    result = {}
    for row in data:
        if row[1] == '':
            continue
        if row[1] not in result.keys() :
            result[row[1]] = {}
        result[row[1]][row[2]] = float(row[3])
    return result

### 计算出要输出的数据
def calcData(config, data):
    result = []
    for key in data:
        val = data[key]
        
        one = []
        one.append(key)
        one.append(sum(val.values()))
        #话费
        if HF in val:
            one.append(val[HF])
        else:
            one.append(0)
        
        if key in config:
            one.append(float(config[key][2]))
            one.append(one[2] * one[3])
        else:
            print('配置文件中不存在此商户 %s' % key)
            one.append(0)
            one.append(0)
        #手机
        if SJ in val:
            one.append(val[SJ])
        else:
            one.append(0)
        one.append(CP)
        one.append(one[5] * one[6])
        #支付宝
        if ZFB in val:
            one.append(val[ZFB])
        else:
            one.append(0)
        one.append(CP)
        one.append(one[8] * one[9])
        #积分
        if QT in val:
            one.append(val[QT])
        else:
            one.append(0)
        one.append(CP)
        one.append(one[11] * one[12])
        
        #移动总收入
        one.append(one[4] + one[7] + one[10] + one[13])
        result.append(one)
    return result
################################################################################################

print('欢迎使用硕硕的报表小工具，本工具协助硕硕同学完成商户及收入的报表生成。注意事项：\n')
print('1. 所有输入、输出文件均为csv；')
print('2. 分润配置文件：指商户的分润比例文件，含有[商户名称，话费商户分润，话费移动分润，手机移动分润]4项数据；')
print('3. 数据文件：指使用sql生成的csv文件；\n')

###
config = readConfig();
if len(config) == 0:
    print('读取配置为空，请检查配置文件！')
    sys.exit()
else:
    c = input('读取配置成功，是否展示配置(Y/N):')
    if c == 'y' or c == 'Y':
        for row in config :
            print(config[row]);

print('\n')    
###    
data = readData();
if len(data) == 0:
    print('数据为空，请检查数据文件！')
    sys.exit()
else:
    c = input('读取数据成功，是否展示数据(Y/N):')
    if c == 'y' or c == 'Y':
        for row in data :
            print(row)
            print(data[row]);
            

#计算结果
result = calcData(config, data);
print('\n')
for row in result:
    print(row)
print('\n计算结果共计 %d' % len(result) , '条')

#写入csv
path = './result_' + str(time.time()) + '.csv';
writeCsv(path, 'w', title, result)

print('\n写文件成功，请到 %s查看\n' % os.path.abspath(path))

input('请按任意键退出...')
sys.exit()
