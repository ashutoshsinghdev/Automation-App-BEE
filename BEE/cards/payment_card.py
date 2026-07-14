from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout ,QLineEdit
)
from PySide6.QtCore import Signal, Qt


class PaymentCard(QWidget):

    confirmed = Signal(str, int, str)  # name, amount, upi
    cancelled = Signal()

    def __init__(self, person, amount, upi):
        super().__init__()

       

    # --- title ---
        title = QLabel("Rent Payment")
        title.setStyleSheet("font-size:15px; font-weight:bold; color:white; background:transparent; border:none;")

    # --- fields FIRST ---
        self.person_field = QLineEdit(person)
        self.amount_field = QLineEdit(str(amount))
        self.upi_field    = QLineEdit(upi)

    # --- then rows ---
        person_row = QHBoxLayout()
        person_row.addWidget(QLabel("Person :"))
        person_row.addWidget(self.person_field)

        amount_row = QHBoxLayout()
        amount_row.addWidget(QLabel("Amount :"))
        amount_row.addWidget(self.amount_field)

        upi_row = QHBoxLayout()
        upi_row.addWidget(QLabel("UPI :"))
        upi_row.addWidget(self.upi_field)

    

        # --- buttons ---
        pay_btn    = QPushButton("Pay Now")
        cancel_btn = QPushButton("Cancel")

        pay_btn.clicked.connect(self._on_confirm)
        cancel_btn.clicked.connect(self.cancelled.emit)

        btn_row = QHBoxLayout()
        btn_row.addWidget(pay_btn)
        btn_row.addWidget(cancel_btn)

        # --- main layout ---
        layout = QVBoxLayout()
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(8)
        layout.addWidget(title)
        layout.addLayout(person_row)
        layout.addLayout(amount_row)
        layout.addLayout(upi_row)
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
            padding: 6px 16px;
            border: none;
        }
        QPushButton:hover { background: #4da3ff; }
        QPushButton:last-child {
            background: #555;
        }
        QPushButton:last-child:hover { background: #777; }
                           
        QLabel { background: transparent; border: none; color: #cccccc; font-size: 13px; }
        """)
    def _on_confirm(self):
        name   = self.person_field.text().strip()
        amount = self.amount_field.text().strip()
        upi    = self.upi_field.text().strip()
        self.confirmed.emit(name, int(amount) if amount.isdigit() else 0, upi)#this could be given as new input.