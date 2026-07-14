import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
#to run the application:-
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
