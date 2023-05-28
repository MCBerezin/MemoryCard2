#создай приложение для запоминания информации
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question1 =  Question('Как дела?', 'Пока не родила!', 'С кайфом', 'Хорошо', 'отлично')
question_list.append(question1)

question2 =  Question('Братишка, как ты? как ты?', 'Замечательно', 'Отстань', 'Не брат ты мне', 'Хорошо')
question_list.append(question2)

question3 = Question('Я, я мегафон?', 'Да', 'Нет', 'Не знаю', 'Хорошо')
question_list.append(question3)


app = QApplication([])
window = QWidget()


window.setWindowTitle('Memory Card')
window.move(0,0)
window.resize(400, 300)

lb_question1 = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')

qrbutton1 = QRadioButton('Вариант 1')
qrbutton2 = QRadioButton('Вариант 2')
qrbutton3 = QRadioButton('Вариант 3')
qrbutton4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(qrbutton1)
layout_ans2.addWidget(qrbutton2)
layout_ans3.addWidget(qrbutton3)
layout_ans3.addWidget(qrbutton4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты текста')

lb_result = QLabel('Прав ты или нет?')
lb_correct = QLabel('Прав!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)

AnsGroupBox.setLayout(layout_res)

button_ok = QPushButton('Ответить!')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_card = QVBoxLayout()

layout_line1.addWidget(lb_question1)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

layout_line3.addWidget(button_ok)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Ответить')
    button_group = QButtonGroup()
    button_group.addButton(qrbutton1)
    button_group.addButton(qrbutton2)
    button_group.addButton(qrbutton3)
    button_group.addButton(qrbutton4)

    button_group.setExclusive(False)
    qrbutton1.setChecked(False)
    qrbutton2.setChecked(False)
    qrbutton3.setChecked(False)
    qrbutton4.setChecked(False)
    button_group.setExclusive(True)

answer = [qrbutton1, qrbutton2, qrbutton3, qrbutton4]
shuffle(question_list)

def ask():
    global asked_question
    asked_question += 1
    if asked_question == len(question_list):
        asked_question = - 1
        print('Процент правильных ответов', score/asked_question*100)

    ask_question = question_list[asked_question]

    shuffle(answer)
    answer[0].setText(ask_question.right_answer)
    answer[1].setText(ask_question.wrong1)
    answer[2].setText(ask_question.wrong2)
    answer[3].setText(ask_question.wrong3)

    lb_question1.setText(ask_question.question)
    lb_correct.setText(ask_question.question)

    show_question()

    
def check_answer():
    if question_list[0].isChecked():
        lb_result.setText('Правильно')
        show_result()

    if question_list[1].isChecked() or question_list[2].isChecked() or question_list[3].isChecked():
        lb_result.setText('Неверно')
        show_result()


def click_ok():
    if button_ok.text() == 'Ответить':
        check_answer()

    else:
        ask()
        
button_ok.clicked.connect(click_ok)

ask()

window.show()
app.exec_()