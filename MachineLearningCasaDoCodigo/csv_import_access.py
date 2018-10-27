import csv

def load_data():
    data = []
    markers = []
    
    file = open('csv/access.csv', 'r')
    reader = csv.reader(file)

    next(reader)
    for acessou_home, acessou_como_funciona, acessou_contato, comprou in reader:
        data.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
        markers.append(int(comprou))

    return data, markers

#print(load_data())

