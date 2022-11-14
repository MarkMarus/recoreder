import csv

with open('data/profiles_main.txt', 'w') as f: f.write('')
with open('data/transactions.csv', 'w') as f: csv.writer(f).writerow(['ID', 'Name', 'Sum', 'Date', 'Time'])