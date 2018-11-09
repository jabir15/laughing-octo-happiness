import csv

fields = ['name', 'full_address', 'college_district', 'college_pincode', 'college_url' ]
for row in csv.reader(open('index.csv')):
    print(fields,row)
