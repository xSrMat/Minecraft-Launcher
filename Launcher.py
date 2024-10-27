import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import * 

import minecraft_launcher_lib as mc
import subprocess

# Get the Minecraft Directory of your System
minecraft_directory = mc.utils.get_minecraft_directory()

class MinecraftLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Personal_Projects/Minecraft-Launcher/Icon.png"))
        self.setWindowTitle("Minecraft Launcher")
        self.setGeometry(800, 300, 400, 500)
        self.LauncherName = QLabel("MINECRAFT LAUNCHER V1.0", self)
        self.username = QLabel("Username: ", self)
        self.username_input = QLineEdit(self)
        self.welcome = QLabel(self)
        self.get_username_button = QPushButton("Set Username", self)
        self.get_play_button = QPushButton("Play", self)
        self. setWindowFlag(Qt. WindowMaximizeButtonHint, False)
        self.selected_username = None  
        self.initUI()
        
    def initUI(self):
        
        vbox = QVBoxLayout()
        #Username
        vbox.addWidget(self.LauncherName)
        vbox.addWidget(self.username)
        vbox.addWidget(self.username_input)
        vbox.addWidget(self.welcome)
        
        #Buttons
        vbox.addWidget(self.get_username_button)
        vbox.addWidget(self.get_play_button)
        
        self.setLayout(vbox)
        
        #Username
        self.LauncherName.setAlignment(Qt.AlignCenter)
        self.username.setAlignment(Qt.AlignCenter)
        self.username_input.setAlignment(Qt.AlignCenter)
        self.welcome.setAlignment(Qt.AlignCenter)
        
        #Username
        self.LauncherName.setObjectName("LauncherName")
        self.username.setObjectName("username")
        self.username_input.setObjectName("username_input")
        self.welcome.setObjectName("welcome")
        
        #Buttons
        self.get_username_button.setObjectName("get_username_button")
        self.get_play_button.setObjectName("get_play_button")
        
        self.setStyleSheet("""
                           
                           QWidget {
                            background-color: #3b3a30;
                           }
                           
                           QLabel{
                               color: #ffffff;
                               font-size: 20px;
                           }
                           
                           QLabel#username{
                               color: #ffffff;
                               font-weight: bold;
                               font-size: 20px;
                           }
                           QLabel#LauncherName{
                               color: #ffffff;
                               font-weight: bold;
                               font-size: 25px;
                           }
                           
                           QPushButton{
                               color: #ffffff;
                               font-family: calibri;
                               font-size: 20px;
                               background-color: #006325
                           }
                           
                           QPushButton#get_play_button{
                               font-weight: bold;
                               font-size: 25px;
                               height: 40px;
                               border-radius: 5px;
                           }
                           
                           QPushButton#get_username_button{
                               font-weight: bold;
                               height: 40px;
                               border-radius: 5px;
                           }
                               
                           
                           QPushButton#get_play_button:hover{
                               background-color: #009437
                               
                               
                           }  
                           QPushButton#get_username_button:hover{
                               background-color: #009437
                               
                           }    

                           
                           QLabel#username{
                               font-size: 20px;
                               font-style: bold;
                               font-family: calibri;
                           }
                           QLineEdit#username_input{
                               background-color: #b2c2bf;
                               font-size: 20px;
                               font-style: bold;
                               font-family: calibri;
                               color: #000000;
                           }
                           """)

        self.get_play_button.hide()
        self.get_username_button.clicked.connect(self.get_minecraftlauncher)
        self.get_play_button.clicked.connect(self.get_minecraftlauncher_play)
        
        
        
    def get_minecraftlauncher(self):
        
        username = self.username_input.text()
        if len(username) < 3 or len(username) > 16:
            self.get_play_button.hide()
            self.welcome.setText("Username must be between 3\nand 16 characters!")
            self.selected_username = None
        else:
            self.selected_username = username
            self.get_play_button.show()
            self.welcome.setText(f"Welcome: {username}")
            
    def get_minecraftlauncher_play(self):
        if not self.selected_username:
            self.welcome.setText("Please set a valid username first!")
            return
        
        setting = {
            "username": self.selected_username,
            "uuid": "15fb7651-17f3-4455-baeb-28ba6e7e4e80",
            "token": "token",
        }


        try:
            minecraft_command = mc.command.get_minecraft_command("1.20.4", minecraft_directory, setting)


            # Start Minecraft
            process = subprocess.Popen(minecraft_command)
            
            # Hide the window
            self.hide()

            # Wait for the player end to play
            process.wait()

            # Show again the window
            self.show()
        except Exception as e:
            self.welcome.setText(f"Error: {str(e)}")


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    minecraft_launcher = MinecraftLauncher()
    minecraft_launcher.show()
    sys.exit(app.exec_())
