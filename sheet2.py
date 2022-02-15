#This is facebook_process_10_2021_detail_report.csv extension

import csv


with open ('facebook_process_10_2021_detail_report.csv') as file:

    reader=csv.reader(file)

    for row in reader:
        print(row)