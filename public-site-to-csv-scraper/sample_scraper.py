import csv

with open('quotes_sample.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['quote','author'])
    writer.writerow(['example public record','sample author'])

print('wrote quotes_sample.csv')
