import csv
import pandas as pd


def readCSV(csv_file_path):
    data = []
    
    with open(csv_file_path,encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            data.append(row)

    return data


def main():
    clients = []

    firstInfo = readCSV('clientes.csv')
    secondaryInfo = readCSV('clientes2.csv')

    for info in firstInfo:
        for obj in secondaryInfo:
    
            if info['id'] == obj['id']:
                clients.append({**obj, **info})

    
    df = pd.DataFrame(clients)

    df.to_excel('resultado.xlsx', index=False)
    
main()