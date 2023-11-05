import os
import csv

# Указать путь к корневой директории датасета
dataset_root = 'C:\\Users\\foris\\Desktop\\PD-git\\PDISK\\LAB2\\dataset'
project_root = 'C:\\Users\\foris\\Desktop\\PD-git\\PD\\LAB3\\'

# Создать\\открыть файл аннотации
with open('annotations.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['C:\\Users\\foris\\Desktop\\PD-git\\PDISK\\LAB2\\dataset', '..\\LAB2\\dataset', 'rose'])

    for root, dirs, files in os.walk(dataset_root):
        for file in files:
            if file.endswith('.jpg'):
                absolute_path = os.path.join(root, file)
                relative_path = os.path.relpath(absolute_path, project_root)
                label = os.path.basename(root)
                writer.writerow([absolute_path, relative_path, label])