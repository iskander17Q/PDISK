Создание файла-аннотации CSV для датасета

import os
import csv

# Папка, куда будет создан файл-аннотации
annotation_folder = 'C:\\Users\\admin\\Desktop\\UTM\\PD\\lab_4\\'
annotation_file = os.path.join(annotation_folder, 'annotation.csv')

# Функция для создания аннотации
def create_annotation_file(source_folder, class_name):
    with open(annotation_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['C:\\Users\\admin\\Desktop\\UTM\\PD\\lab_3\\dataset2', '..\\lab_2\\dataset', class_name])

        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.jpg'):
                    absolute_path = os.path.join(root, file)
                    relative_path = os.path.relpath(absolute_path, annotation_folder)
                    label = os.path.basename(absolute_path)
                    writer.writerow([absolute_path, relative_path, label])
