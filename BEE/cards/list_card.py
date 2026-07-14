from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Signal, Qt


class ListCard(QWidget):

    confirmed = Signal(list)  # sends the whole items list

    def __init__(self, title, items):
        super().__init__()

        # --- title ---
        title_lbl = QLabel(title)
        title_lbl.setStyleSheet("font-size:15px; font-weight:bold; color:white; background:transparent; border:none;")

        self.items = items

        # --- item rows ---
        items_layout = QVBoxLayout()
        items_layout.setSpacing(6)

        for item in items:
            row = QHBoxLayout()

            name_lbl  = QLabel(item["item"])
            price_lbl = QLabel(f"₹{item['price']}")

            name_lbl.setStyleSheet("color:#cccccc; font-size:13px; background:transparent; border:none;")
            price_lbl.setStyleSheet("color:#cccccc; font-size:13px; background:transparent; border:none;")

            row.addWidget(name_lbl)
            row.addStretch()
            row.addWidget(price_lbl)

            items_layout.addLayout(row)

        # --- continue button ---
        continue_btn = QPushButton("Continue")
        continue_btn.clicked.connect(self._on_continue)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(continue_btn)
        btn_row.addStretch()

        # --- main layout ---
        layout = QVBoxLayout()
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)
        layout.addWidget(title_lbl)
        layout.addLayout(items_layout)
        layout.addLayout(btn_row)
        self.setLayout(layout)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
        QWidget {
            background-color: rgba(0,0,0,255);
            border: 2px solid rgba(80,80,80,100);
            border-radius: 10px;
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

    def _on_continue(self):
        self.confirmed.emit(self.items)
        #it should use playwright to automate the process.