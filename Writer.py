import time
import csv


def write_log(data):
    file = 'log_' + time.strftime("%y%m%d%H%M%S") + '.csv'
    with open(file, 'w') as csvfile:
        csv.writer(csvfile, delimiter=';', lineterminator='\n').writerows(data)

    return file
