import csv

class CSVFileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        data = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    def write_csv(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

csv_manager = CSVFileManager('data.csv')

data = csv_manager.read_csv()
for row in data:
    print(row)

new_data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30], ['Charlie', 35]]
data.extend(new_data)

csv_manager.write_csv(data)
