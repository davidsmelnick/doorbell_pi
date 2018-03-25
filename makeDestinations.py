import csv

def f():

    numbers = open('numbers.csv')
    numberscsv = csv.reader(numbers,delimiter=',')

    carriers = open('carrier.csv')
    carrierscsv = csv.reader(carriers)

    gateway = {}
    for row in carrierscsv:
        gateway[row[0]] = row[1]
        
    destinations = {}
    destinations['1'] = []
    destinations['2'] = []
    destinations['3'] = []

    for row in numberscsv:
        if row[0] != 'floor':
            destinations[str(row[0])].append(str(row[1]) + '@' + gateway[row[2]])
        
    return destinations
