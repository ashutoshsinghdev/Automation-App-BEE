from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit
)
from PySide6.QtCore import Signal, Qt
 
 
class InputCard(QWidget):
 
    submitted = Signal(str)   # sends whatever the user typed
 
    def __init__(self, title, placeholder="Type here..."):
        super().__init__()
 
        # --- title ---
        title_lbl = QLabel(title)
        title_lbl.setStyleSheet("font-size:15px; font-weight:bold; color:white; background:transparent; border:none;")
 
        # --- input field ---
        self.field = QLineEdit()
        self.field.setPlaceholderText(placeholder)
        self.field.returnPressed.connect(self._on_submit)   # submit on Enter too
 
        # --- submit button ---
        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self._on_submit)
 
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(submit_btn)
        btn_row.addStretch()
 
        # --- main layout ---
        layout = QVBoxLayout()
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)
        layout.addWidget(title_lbl)
        layout.addWidget(self.field)
        layout.addLayout(btn_row)
        self.setLayout(layout)
 
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
        QWidget {
            background-color: rgba(0,0,0,255);
            border: 2px solid rgba(80,80,80,100);
            border-radius: 10px;
        }
        QLineEdit {
            background: rgba(255,255,255,10);
            color: white;
            border: 1px solid rgba(255,255,255,60);
            border-radius: 6px;
            padding: 6px 10px;
            font-size: 13px;
        }
        QLineEdit:focus {
            border: 1px solid #2d89ef;
        }
        QPushButton {
            background: #2d89ef;
            color: white;
            border-radius: 6px;
            padding: 6px 20px;
            border: none;
        }
        QPushButton:hover { background: #4da3ff; }
        """)
 
    def _on_submit(self):
        text = self.field.text().strip()
        if text:                          # only fire if something was typed
            self.submitted.emit(text)