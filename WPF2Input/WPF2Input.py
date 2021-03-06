﻿import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WPF2Input.xaml')  
        self.label.Content = "Enter your name"
        self.textBox.Text = ""
    
    def button_Click(self, sender, e):
        userName = self.textBox.Text
        self.label.Content = ("Welcome " + userName.capitalize() + " it's nice to meet you")
    
if __name__ == '__main__':
    Application().Run(MyWindow())
