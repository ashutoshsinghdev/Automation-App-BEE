from PySide6.QtWidgets import QHBoxLayout

from cards.notification_bubble import NotificationBubble
from cards.input_card import InputCard 
from cards.list_card import ListCard  
from cards.payment_card import PaymentCard  

class ChatManager:

    def __init__(self, chatLayout):

        self.chatLayout = chatLayout


    def add_notification(self, title, message):

        row = QHBoxLayout()

        bubble = NotificationBubble(title, message)#this will give us an output card.

        row.addWidget(bubble)

        row.addStretch()

        self.chatLayout.addLayout(row)# adding this layout with our card in main vertical layout.

        bubble.dismissed.connect(bubble.deleteLater)#this collects the signla, syntax signal.connect,and delets the whole bubble.
        bubble.dismissed.connect(row.deleteLater)
        bubble.proceed.connect(lambda:self.profun(bubble,row))#this collects the signal and calls inown function for it .

    def profun(self,bubble,row):
        print("open payment")


#input card:-
    def add_input_card(self, title, placeholder="Type here..."):
        row = QHBoxLayout()
        card = InputCard(title, placeholder)
        row.addWidget(card)
        row.addStretch()
        self.chatLayout.addLayout(row)
        return card    

#list card:-

    def add_list_card(self, title, items):
        row = QHBoxLayout()
        list_card = ListCard(title, items)
        row.addWidget(list_card)
        row.addStretch()
        self.chatLayout.addLayout(row)
        return list_card
    

#PaymentCard:-
    def add_payment_card(self, person, amount, upi):
        row = QHBoxLayout()
        pay_card = PaymentCard(person, amount, upi)
        row.addWidget(pay_card)
        row.addStretch()
        self.chatLayout.addLayout(row)
        return pay_card                  # return so mainwindow can connect signals
        



        # the payment card stores the pay ment amoubt in a json files mainly in details file as room paymet or tiffiment paymet after we enter it for the first time , and load it from next time in the line text only and even for firts time it should load the name and upiid in the line text from details along with it shows the date of due.

        # and the notification should also have one more btn proceed.if clicked give payment cards or list card.
        # also payment card will be 2.

        #note we can use thes custom signal to feed input ot the playwright through excuter.as these signal can emit different type of valuesthat can be colleced by the excuter.