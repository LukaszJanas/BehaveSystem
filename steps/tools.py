'''

There are included a useful tools/functions which are necessary for performed a steps for tests.

Developed by:
Inż. Janas Łukasz

Last changes:
14.05.2023 

'''

import time
import matplotlib.pyplot as plt
import datetime

def check_if_file_is_empty(name="results.txt"):
    try:
        with open(name, 'r') as file:
            inside = file.read()
            if inside == '':
                return True
            else:
                return False
    except FileNotFoundError:
        return True

def write_to_file(val, type, name="results.txt"):
    if check_if_file_is_empty(name):
        with open(name, 'a') as file:
            file.write(f'Czas\t\t\t\t\t{type}\n')
    
    with open(name, 'a') as file:
        file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")}\t\t{val}\n')

def plot_from_txt_file(name="results.txt"):
    time = []
    values = []
    
    with open(name, 'r') as file:
        line = file.readlines()
        type = line[0].strip().split('\t\t\t\t')[1]
        for lines in line[1:]:
            columns = lines.strip().split('\t\t')
            time.append(datetime.datetime.strptime(columns[0], '%Y-%m-%d %H:%M:%S'))
            values.append(float(columns[1]))
    
    plt.plot(time, values)
    plt.xlabel('Czas')
    plt.ylabel(type)
    plt.title('Wykres w czasie')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()