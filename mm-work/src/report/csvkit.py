import csv, os
'''
读取csv file
'''
def readCsv(path, mode='r'):
    result = [];
    if os.path.isfile(path):
        csvfile = open(path, mode, newline='')
        reader = csv.reader(csvfile)
        count = 0;
        for row in reader:
            if count > 0 :
                result.append(row);
            count += 1
            #print (','.join(row))
        
    return result

'''
写入csv file
'''
def writeCsv(path, mode='w', title=[], data=[]):
    csvfile = open(path, 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(title)

    writer.writerows(data)
    csvfile.close()



    