import os
import sys
import random
import csv
from PyQt5 import QtWidgets, QtGui

class DatasetApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dataset App')
        self.setGeometry(100, 100, 1300, 550)
        self.folderpath = None

        self.browse_button = self.create_button('Выбрать папку с датасетом', self.browse_dataset_folder, 20, 20)
        self.create_annotation_button = self.create_button('Создать аннотацию', self.create_annotation, 20, 60)
        self.create_annotation_button.setEnabled(False)

        self.next_class1_button = self.create_button('Следующий класс 1', self.get_next_class1, 20, 100)
        self.next_class2_button = self.create_button('Следующий класс 2', self.get_next_class2, 20, 140)

        self.image_label = self.create_label(250, 20, 1000, 500)

    def create_button(self, text, on_click, x, y):
        button = QtWidgets.QPushButton(text, self)
        button.setGeometry(x, y, 200, 30)
        button.clicked.connect(on_click)
        return button

    def create_label(self, x, y, width, height):
        label = QtWidgets.QLabel(self)
        label.setGeometry(x, y, width, height)
        label.setScaledContents(True)
        return label

    def browse_dataset_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с исходным датасетом')
        if self.folderpath:
            self.create_annotation_button.setEnabled(True)
            self.next_class1_button.setEnabled(True)
            self.next_class2_button.setEnabled(True)

    def create_annotation(self):
        if self.folderpath:
            self.create_annotations(['rose', 'tulip'])

    def create_annotations(self, class_names):
        with open('annotations.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Absolute Path', 'Relative Path', 'Label'])

            for class_name in class_names:
                class_path = os.path.join(self.folderpath, class_name)
                for root, _, files in os.walk(class_path):
                    for file in files:
                        if file.endswith('.jpg'):
                            absolute_path = os.path.join(root, file)
                            relative_path = os.path.relpath(absolute_path, self.folderpath)
                            writer.writerow([absolute_path, relative_path, class_name])

    def get_next_instance(self, class_label):
        class_files = [f for f in os.listdir(os.path.join(self.folderpath, class_label)) if f.endswith('.jpg')]
        if class_files:
            random.shuffle(class_files)
            return os.path.join(self.folderpath, class_files.pop())  # ОШИБКА: не указываем подпапку class_label
        else:
            return None

    def get_next_class1(self):
        if self.folderpath:
            next_instance = self.get_next_instance('rose')
            if next_instance:
                pixmap = QtGui.QPixmap(next_instance)
                self.image_label.setPixmap(pixmap)

    def get_next_class2(self):
        if self.folderpath:
            next_instance = self.get_next_instance('tulip')
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