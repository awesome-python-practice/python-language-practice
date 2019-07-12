# -*- coding: utf-8 -*-
from googletrans import Translator
import csv
import sys

# csv_file_name = 'translation-source.csv'
# des_file_name = 'translation-result.csv'
if len(sys.argv) < 3:
    print('usage: python3 translate.py src.csv dest.csv')
    exit(1)

csv_file_name = sys.argv[1]
des_file_name = sys.argv[2]
des_file = open(des_file_name, mode='w+')

translator = Translator()

with open(csv_file_name, encoding='utf-8') as csv_file_name:
    csv_reader = csv.reader(csv_file_name, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            des_file.write(row[0] + ',' + row[1] + '\n')
            line_count += 1
        else:
            if len(row) < 2:
                continue
            cause = translator.translate(row[0]).text
            count = row[1]
            des_file.write(cause + ',' + count + '\n')
            line_count += 1
    print('Processed ', line_count, ' lines.')
