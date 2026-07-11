import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QLabel,QHBoxLayout
from ui_mainWindow import Ui_MainWindow
from PySide6.QtCore import Qt,QTimer
from datetime import datetime


#setteing up the UI:-

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  
# Create chat layout
        self.chatLayout = QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.chatLayout)
        self.chatLayout.setContentsMargins(10,10,10,10)
        self.chatLayout.setSpacing(5)
        
        #when send btn clicked or enter pressed in chat layout:-
        self.Sendbtn.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.send_message)

     #to store chats in ram:-
        # Current chat (stored only while the app is running)
        self.currentMessages = []
# Start with an empty chat area
        self.clear_chat()
# No conversation has been saved yet
        self.isNewChat = True
    
#to change the pg:-
        self.settings.clicked.connect(self.open_settings)
        self.pushButton_3.clicked.connect(self.open_details)
        self.newChat.clicked.connect(self.open_newChat)
        self.chatHis.clicked.connect(self.open_chatHis)
        self.dashboard.clicked.connect(self.open_dashboard)
#to display the details data(function calling).
        self.load_details()

#to write the details data(making the connection and calling the function in case of action):-
        self.lineEdit_2.returnPressed.connect(self.save_username)#they run intially only and estable just the connection bw signal and slot .

        #also lineedit->json->label
        
        self.lineEdit_3.returnPressed.connect(self.save_userupi)
        self.lineEdit_4.returnPressed.connect(self.save_landLordName)
        self.lineEdit_5.returnPressed.connect(self.save_landLordUpi)
        self.lineEdit_8.returnPressed.connect(self.save_landLordNo)
        self.lineEdit_6.returnPressed.connect(self.save_tiffineName)
        self.lineEdit_7.returnPressed.connect(self.save_tiffineUpi)
        self.lineEdit_9.returnPressed.connect(self.save_tiffineNo)
#loading the chat history:-
        self.load_chat_titles()

#chat_his_btn:-

        self.chatBtn1.clicked.connect(lambda: self.load_chat(0))
        self.chatBtn2.clicked.connect(lambda: self.load_chat(1))
        self.chatBtn3.clicked.connect(lambda: self.load_chat(2))
        self.chatBtn4.clicked.connect(lambda: self.load_chat(3))
#to stop the copy of chats in histoery:-
        self.loadedChatIndex = None
#to open the pg:-

    def open_settings(self):
        self.stackedWidget.setCurrentWidget(self.page_4)
    def open_details(self):
        self.stackedWidget.setCurrentWidget(self.page_5)
    def open_newChat(self):
        # Save current conversation if it has messages
        self.save_current_chat()
    # Start a fresh conversation
        self.currentMessages = []
        self.loadedChatIndex = None
        self.stackedWidget.setCurrentWidget(self.page)
        self.clear_chat()
        self.lineEdit.clear()
        self.isNewChat = True
    def open_chatHis(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
    def open_dashboard(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
  
#To display the details data from json into the lables:-
    def load_details(self):
        with open("details.json", "r") as file:
            data = json.load(file)

        self.label_21.setText(data["username"])
        self.label_22.setText(data["user_upi"])
        self.label_23.setText(data["landlordname"])
        self.label_26.setText(data["landloard_upi"])
        self.label_24.setText(data["landlord_no"])
        self.label_28.setText(data["tiffinename"])
        self.label_27.setText(data["tiffine_upi"])
        self.label_25.setText(data["tiffine_no"])#.setText sets the text.


# to write the detailes data in json from the lineedits:-    

    def save_username(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["username"] = self.lineEdit_2.text()#.text display the text.
                    # to set key value to a key we use variable["keyname"]=value.

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.lineEdit_3.setFocus()
        self.load_details()


    def save_userupi(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["user_upi"] = self.lineEdit_3.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.lineEdit_4.setFocus()
        self.load_details()

    def save_landLordName(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["landlordname"] = self.lineEdit_4.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)
        
        self.lineEdit_5.setFocus()
        self.load_details()
    
    def save_landLordUpi(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["landloard_upi"] = self.lineEdit_5.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.lineEdit_8.setFocus()
        self.load_details()
   
    def save_landLordNo(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["landlord_no"] = self.lineEdit_8.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.lineEdit_6.setFocus()
        self.load_details()
   
    def save_tiffineName(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["tiffinename"] = self.lineEdit_6.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.lineEdit_7.setFocus()
        self.load_details()
    
    def save_tiffineUpi(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["tiffine_upi"] = self.lineEdit_7.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.lineEdit_9.setFocus()
        self.load_details()
    
    
    def save_tiffineNo(self):

        with open("details.json", "r") as file:
            data = json.load(file)

        data["tiffine_no"] = self.lineEdit_9.text()

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)

        self.load_details()

# To show the chat on scroll area and to store them in json:-
    def send_message(self):
        text = self.lineEdit.text()
        self.add_message(text,"user")#we are wrting user bcz text always comes from user.
        reply=self.get_ai_reply(text)
        self.add_message(reply,"ai")#we are wrting ai bcz reply always comes from ai.

        self.currentMessages.append({
              "sender":"user",
              "text":text,
              "time": datetime.now().strftime("%H:%M")
            })

        self.currentMessages.append({
            "sender":"ai",
             "text":reply,
             "time": datetime.now().strftime("%H:%M")
            })#this whole thing is getting saved in just our ram.
        
       
        self.lineEdit.clear()

     
   #add msg function:-
    def add_message(self,text,sender):
        row=QHBoxLayout()
        labelCh = QLabel(text)
        labelCh.setWordWrap(True)
        labelCh.setContentsMargins(12, 8, 12, 8)
        #css for the bubble:-
        if sender == "user":

            labelCh.setStyleSheet("""
            QLabel{
            background-color: rgba(255, 255, 255,25);
            border-radius:2px;
            border:2px solid rgba(255,255,255,100);
            padding:5px;
            font-size:14px;
        }
    """)
            row.addStretch()
            row.addWidget(labelCh)
            labelCh.adjustSize()

        else:

            labelCh.setStyleSheet("""
            QLabel{
            background-color:rgba(0, 0, 0, 255);
            border-radius:2px;
            border:2px solid rgba(80, 80, 80, 100);
            padding:5px;
            font-size:14px;
        }
    """)
        
            row.addWidget(labelCh)
            labelCh.adjustSize()#here it make the labe height and width adjust according to the text insdie the lable.
            row.addStretch()

        labelCh.setTextInteractionFlags(Qt.TextSelectableByMouse|
        Qt.TextSelectableByKeyboard)    
        self.chatLayout.addLayout(row)
        self.lineEdit.setFocus()
        
        #used for auto scroll:-
        self.scrollAreaWidgetContents.adjustSize()#here it tell the final height of scrollareawdgit after adjust all the child element accorddly.
        QApplication.processEvents()

        self.chatBox.verticalScrollBar().setValue(
        self.chatBox.verticalScrollBar().maximum()
        )

        #ai replay:-
    def get_ai_reply(self,text):
        return "Hello Ashutosh!"
    
    #load chat his titles:-
    def load_chat_titles(self):

        with open("chatHistory.json", "r") as file:
            data = json.load(file)

        chats = data["chats"]

        self.chatBtn1.setText(chats[0]["title"])
        self.chatBtn2.setText(chats[1]["title"])
        self.chatBtn3.setText(chats[2]["title"])
        self.chatBtn4.setText(chats[3]["title"])

    #clear the whole chat history from chatbox when new btn clicked or app starts for the first time.

    def clear_layout(self, layout):
        while layout.count():#returns the number of items inside the layout.and all no give true val excep 0.
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())
                item.layout().deleteLater()#delete the empty layout itself.aand it runs after recurive call.
#calling clear chat:-
    def clear_chat(self):
        self.clear_layout(self.chatLayout)#chatlayout==vertical layout.

    #saving current chats:-
    def save_current_chat(self):
        # Don't save an empty conversation
        if not self.currentMessages:
            return

        with open("chatHistory.json", "r") as file:
            data = json.load(file)

        title = self.currentMessages[0]["text"]
        if len(title) > 25:
            title = title[:25] + "..."    

            #same same chat history bug:-
        chat = {
        "title": title,
        "messages": self.currentMessages#it is a list that have collecton of chats between user and ai inform of dicnotires , currentmessages=[{},{},{}]
        }
        if self.loadedChatIndex is None:#means new chat.
        
            data["chats"].insert(0, chat)  #this data ={chats:[{},{},{}]}
            data["chats"] = data["chats"][:4]
        else:
            data["chats"][self.loadedChatIndex] = chat

        with open("chatHistory.json", "w") as file:
            json.dump(data, file, indent=4)

        self.load_chat_titles()
        self.currentMessages = []
        self.loadedChatIndex = None
#class event:-
    def closeEvent(self, event):

        self.save_current_chat()

        event.accept()
#chat_history_btn_function:-
    def load_chat(self, index):
        with open("chatHistory.json", "r") as file:
            data = json.load(file)
        chats = data["chats"]
    # If this slot is empty, do nothing
        if len(chats[index]["messages"]) == 0:
            return
    # Go to chat page
        self.stackedWidget.setCurrentWidget(self.page)
    # Remove current messages from the screen
        self.clear_chat()
    # Start a fresh temporary list
        self.currentMessages = []
    # Load every saved message
        for msg in chats[index]["messages"]:
            self.add_message(msg["text"], msg["sender"])
            self.currentMessages.append(msg)#this will give a list of massages and append it to the curentmessages.

        self.loadedChatIndex = index    

#to run the application:-
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())


#1we will add later that new text and also when the app load we get msg window without any text.
#2also we will add that when we click thoses chat history btns we will get to msg box with those chats loaded.