from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import Signal, Qt


class NotificationBubble(QWidget):

    dismissed = Signal()# it is manly used to create custo signals.
    proceed = Signal()

    def __init__(self, title, message):

        super().__init__()

        self.title = QLabel(title)
        self.message = QLabel(message)
        self.button = QPushButton("Dismiss")
        self.button2n = QPushButton("Proceed")

        self.title.setStyleSheet("""
        font-size:15px;
        font-weight:bold;
        color:white;
        background:transparent;
        border:none;
        """)

        self.message.setStyleSheet("""
        color:white;
        background:transparent;
        border:none;
        """)

        self.message.setWordWrap(True)

        self.button.clicked.connect(self.dismissed.emit)# this fires the signal to elemts tp collect it 
        self.button2n.clicked.connect(self.proceed.emit)

        buttonLayout = QHBoxLayout()

        buttonLayout.addStretch()# to make the btn at center.
        buttonLayout.addWidget(self.button2n)
        buttonLayout.addWidget(self.button)
        buttonLayout.addStretch()# to make the btn at center.

        layout = QVBoxLayout()

        layout.setContentsMargins(12,10,12,10)
        layout.setSpacing(8)

        layout.addWidget(self.title)
        layout.addWidget(self.message)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)
        self.setAttribute(Qt.WA_StyledBackground, True)
        #QWidget by default does NOT paint its own background or border from stylesheets. It just ignores them silently — that's why your border wasn't showing.
        # setAttribute sets a property on the widget. Qt.WA_StyledBackground is that property — it tells Qt "yes, actually render this widget's stylesheet."

        self.setStyleSheet("""
        QWidget{

            background-color:rgba(0,0,0,255);

            border:2px solid rgba(80,80,80,100);

            border-radius:10px;

        }

        QPushButton{

            background:#2d89ef;

            color:white;

            border-radius:6px;

            padding:6px;

        }

        QPushButton:hover{

            background:#4da3ff;

        }
        """)