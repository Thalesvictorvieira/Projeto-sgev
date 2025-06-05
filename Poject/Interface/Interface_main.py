import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton("Texto botao 1")
botao.setStyleSheet("font-size: 40px; color: red")

botao2 = QPushButton("Texto botao 2")


botao.show()
app.exec()