from PyQt6.QtWidgets import (QApplication, QWidget,
                              QLabel, QVBoxLayout)
from PyQt6.QtCore import Qt

app = QApplication([])
win = QWidget()

win.setWindowTitle("Fun programm")
win.resize(600, 500)

text = QLabel("Hello, World!")
main_line = QVBoxLayout()

main_line.addWidget(text, alignment = Qt.AlignmentFlag.AlignCenter)

win.setLayout(main_line)

win.show()
app.exec()