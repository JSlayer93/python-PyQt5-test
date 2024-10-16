import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QGridLayout, QWidget

# creating Mainwindow class to display window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # customizing window placement to be center
        self.setGeometry(450, 400, 1000, 800)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        # setting up window title to test
        self.setWindowTitle('test')
        # defining questions, answers and right answers for test
        self.questions = [
            "What is the capital of France?", 
            "Which planet is known as the Red Planet?", 
            "Who wrote 'To Kill a Mockingbird'?", 
            "What is the largest ocean on Earth?"
        ]
        self.right_answers = ["Paris", "Mars", "Harper Lee", "Pacific Ocean"]
        self.answers = {
            0: ["London", "Berlin", "Paris", "Madrid"],
            1: ["Earth", "Venus", "Mars", "Jupiter"],
            2: ["J.K. Rowling", "Harper Lee", "Jane Austen", "Mark Twain"],
            3: ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]
        }
        # defining number to know in which question i am on
        self.number = 0
        # definging points to know how much user got right
        self.points = 0

        # creating question label(text)
        self.question = QLabel(self.questions[0], self)
        
        # creating answer buttons
        self.answer_1 = QPushButton(self.answers[0][0], self)
        self.answer_2 = QPushButton(self.answers[0][1], self)
        self.answer_3 = QPushButton(self.answers[0][2], self)
        self.answer_4 = QPushButton(self.answers[0][3], self)
        
        # calling initUI function in mainwindow class
        self.initUi()

    # defining initUi to cusomize UI
    def initUi(self):
        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # adding grid layout to question label and answer buttons
        self.grid = QGridLayout()
        self.grid.addWidget(self.question, 3, 2)
        self.grid.addWidget(self.answer_1, 6, 1)
        self.grid.addWidget(self.answer_2, 6, 2)
        self.grid.addWidget(self.answer_3, 6, 3)
        self.grid.addWidget(self.answer_4, 6, 4)
        
        # customizing question label
        self.question.setStyleSheet("font-size: 25px")
        
        # customizing answer buttons
        self.answer_1.setStyleSheet("background-color: blue")
        self.answer_2.setStyleSheet("background-color: yellow")
        self.answer_3.setStyleSheet("background-color: purple")
        self.answer_4.setStyleSheet("background-color: green")        

        central_widget.setLayout(self.grid)
        
        # calling on_click function when button is clicked
        self.answer_1.clicked.connect(self.on_click)
        self.answer_2.clicked.connect(self.on_click)
        self.answer_3.clicked.connect(self.on_click)
        self.answer_4.clicked.connect(self.on_click)
        
    # this funtion runs when u click answer button
    def on_click(self):
        sender = self.sender()  # Get the button that was clicked
        if sender.text() == self.right_answers[self.number] and self.number != len(self.questions) - 1:
            self.number += 1 #adding one to number to know i am on next question
            self.points += 1 #adding on to pints to know i earned point
            # changing answer texts to next answers
            self.answer_1.setText(self.answers[self.number][0])
            self.answer_2.setText(self.answers[self.number][1])
            self.answer_3.setText(self.answers[self.number][2])
            self.answer_4.setText(self.answers[self.number][3])
            # changing question text
            self.question.setText(self.questions[self.number])
        elif self.number != len(self.questions) - 1:
            # changing answer texts to next answers
            self.number += 1
            self.answer_1.setText(self.answers[self.number][0])
            self.answer_2.setText(self.answers[self.number][1])
            self.answer_3.setText(self.answers[self.number][2])
            self.answer_4.setText(self.answers[self.number][3])
            # changing question text
            self.question.setText(self.questions[self.number])
        else:
            if sender.text() == self.right_answers[self.number]: self.points += 1
            # disabling buttons when done every question
            self.answer_1.setDisabled(True)
            self.answer_2.setDisabled(True)
            self.answer_3.setDisabled(True)
            self.answer_4.setDisabled(True)
            # changing questing text to show how much points use got
            self.question.setText(f"you got {self.points} points")
    
    
# defining main function to show window
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
# this code is just saying that if code is moduled don't run and only run when u actually run the code
if __name__ == '__main__':
    main()    