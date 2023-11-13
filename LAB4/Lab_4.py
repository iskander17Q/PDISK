import os
import sys
import random
import csv
from PyQt5 import QtWidgets, QtGui

# Папка, куда будет создан файл-аннотации
annotation_folder = 'C:\\Users\\admin\\Desktop\\UTM\\PD\\lab_4\\'
annotation_file = os.path.join(annotation_folder, 'annotation.csv')

# Функция для создания аннотации
def create_annotation_file(source_folder, class_name):
    with open('annotations.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['C:\\Users\\admin\\Desktop\\UTM\\PD\\lab_3\\dataset2', '..\\lab_2\\dataset', 'rose'])

        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.jpg'):
                    absolute_path = os.path.join(root, file)
                    relative_path = os.path.relpath(absolute_path, annotation_folder)
                    label = os.path.basename(absolute_path)
                    writer.writerow([absolute_path, relative_path, label])

def get_next_instance(class_label, dataset_path):
    class_files = [f for f in os.listdir(dataset_path) if f.startswith(class_label)]
    if class_files:
        random.shuffle(class_files)
        return os.path.join(dataset_path, class_files.pop())
    else:
        return None



class DatasetApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Определите интерфейс

        self.setWindowTitle('Dataset App')
        self.setGeometry(100, 100, 1300, 550)
        self.folderpath = None  # Переменная для хранения пути к папке с исходным датасетом

        # Кнопка для выбора папки с исходным датасетом
        self.browse_button = QtWidgets.QPushButton('Выбрать папку с датасетом', self)
        self.browse_button.setGeometry(20, 20, 200, 30)
        self.browse_button.clicked.connect(self.browse_dataset_folder)

        # Кнопка для создания файла аннотации
        self.create_annotation_button = QtWidgets.QPushButton('Создать аннотацию', self)
        self.create_annotation_button.setGeometry(20, 60, 200, 30)
        self.create_annotation_button.setEnabled(False)  # По умолчанию отключена
        self.create_annotation_button.clicked.connect(self.create_annotation)

        # Кнопки для получения следующего экземпляра
        self.next_class1_button = QtWidgets.QPushButton('Следующий класс 1', self)
        self.next_class1_button.setGeometry(20, 100, 200, 30)
        self.next_class1_button.setEnabled(False)  # По умолчанию отключена
        self.next_class1_button.clicked.connect(self.get_next_class1)

        self.next_class2_button = QtWidgets.QPushButton('Следующий класс 2', self)
        self.next_class2_button.setGeometry(20, 140, 200, 30)
        self.next_class2_button.setEnabled(False)  # По умолчанию отключена
        self.next_class2_button.clicked.connect(self.get_next_class2)

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(250, 20, 1000, 500)  # Изменили размеры здесь
        self.image_label.setScaledContents(True)

    def browse_dataset_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с исходным датасетом')
        if self.folderpath:
            self.create_annotation_button.setEnabled(True)
            self.next_class1_button.setEnabled(True)
            self.next_class2_button.setEnabled(True)

    def create_annotation(self):
        if self.folderpath:
            create_annotation_file(self.folderpath, 'rose')
            create_annotation_file(self.folderpath, 'tulip')
            pass

    def get_next_class1(self):
        if self.folderpath:
            next_instance = get_next_instance('rose', self.folderpath)
            if next_instance:
                pixmap = QtGui.QPixmap(next_instance)
                self.image_label.setPixmap(pixmap)

    def get_next_class2(self):
        if self.folderpath:
            next_instance = get_next_instance('tulip', self.folderpath)
            if next_instance:
                pixmap = QtGui.QPixmap(next_instance)
                self.image_label.setPixmap(pixmap)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DatasetApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()