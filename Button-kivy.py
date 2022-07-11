import random
import time


# File name: New_Eng.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# Getting data from file
filename='./301-310.txt'
s = open(filename).read()
lines = [line.strip() for line in open(filename)]


num=[]
column1=[]
column2=[]
column3=[]
column4=[]
column5=[]
word_list=[]
word_meaning=[]
example_list=[]
example_meaning=[]
real_example=[]


for i in range (0,len(lines)):
    num.append(i)
    line=lines[i].split(chr(9))
    column1.append(line[1])
    column2.append(line[0])
    column3.append(line[3])
    column4.append(line[2])
    column5.append(line[4])


print('num=', num)

word_list=column4
word_meaning=column3
example_list=column1
example_meaning=column2
real_example=column5
print(word_list)
print(word_meaning)




global rand_num
global secret_num

global right_answers_stat
global wrong_answers_stat

right_answers_stat=0
wrong_answers_stat=0


def choose_combination():
    global rand_num
    global secret_num

    right_combination = False

    
    while right_combination==False:
        four_sample_words = []
        four_sample_meaning = []
        rand_num = random.choices(num, k=4)
        secret_num = random.choices(rand_num, k=1)


        for y in range (0,4):
            four_sample_words.append(word_list[rand_num[y]])
            four_sample_meaning.append(word_meaning[rand_num[y]])

        if len(set(four_sample_words)) == len(set(four_sample_meaning)) == 4:
            right_combination = True

            
    return (rand_num, secret_num)



class New_EngApp(App):
    global rand_num
    global secret_num
    global right_answer
    global real_example



    
    
    def build(self, btn1_txt='Answer 1', btn2_txt='Answer 2', btn3_txt='Answer 3', btn4_txt='Answer 4'):
     
        superBox = BoxLayout(orientation ='vertical') 

        q_label = Label(text = 'What is the right translation of this word?', font_size = 18)

        q_word_label = Label(text = 'WORD', font_size = 24, color = 'orange')

        o_text = TextInput(text='Examples:', readonly='True', foreground_color = 'blue', line_height = 1)

        statistics_label = Label(text= 'Statistics...')


        btn1 = Button(text = btn1_txt,
                    font_size = 32, 
                    size_hint =(1, 1))

        btn2 = Button(text = btn2_txt, 
                    font_size = 32, 
                    size_hint =(1, 1)) 

        btn3 = Button(text = btn3_txt, 
                    font_size = 32, 
                    size_hint =(1, 1)) 

        btn4 = Button(text = btn4_txt, 
                    font_size = 32, 
                    size_hint =(1, 1)) 

        btn_next = Button(text ="NEXT", 
                    font_size = 32, 
                    size_hint =(1, 1),
                    background_color = (0.8, 0.8, 0.8, 0.8))

        def change_text_btn1(btn1):
            btn1.text = '1 was Pressed'


        def change_text_btn2(btn2):
            btn2.text = '2 was Pressed'
            
        def change_text_btn3(btn3):
            btn3.text = '3 was Pressed'

        def change_text_btn4(btn4):
            btn4.text = '4 was Pressed'

        def new_q(self):
            new_question('1','2','3','4')

        def btn1_press(self):
            my_answer = 1
            check_result(my_answer)

        def btn2_press(self):
            my_answer = 2
            check_result(my_answer)

        def btn3_press(self):
            my_answer = 3
            check_result(my_answer)

        def btn4_press(self):
            my_answer = 4
            check_result(my_answer)

        def btn_next_press(self):
            new_question()
            
        btn1.bind(on_press=btn1_press)
        btn2.bind(on_press=btn2_press)
        btn3.bind(on_press=btn3_press)
        btn4.bind(on_press=btn4_press)   
        btn_next.bind(on_press=btn_next_press) 

        superBox.add_widget(q_label)
        superBox.add_widget(q_word_label)
        superBox.add_widget(btn1)
        superBox.add_widget(btn2)
        superBox.add_widget(btn3)
        superBox.add_widget(btn4)
        superBox.add_widget(btn_next)
        superBox.add_widget(o_text)
        superBox.add_widget(statistics_label)

        def new_question( btn1_txt='Answer 1', btn2_txt='Answer 2', btn3_txt='Answer 3', btn4_txt='Answer 4'):
            btn1.disabled = False
            btn2.disabled = False
            btn3.disabled = False
            btn4.disabled = False
            btn1.background_color = (1, 1, 1, 1)
            btn2.background_color = (1, 1, 1, 1)
            btn3.background_color = (1, 1, 1, 1)
            btn4.background_color = (1, 1, 1, 1)
            choose_combination()
            q_word_label.text = word_list[secret_num[0]] 
            btn1.text = word_meaning[rand_num[0]]  
            btn2.text = word_meaning[rand_num[1]] 
            btn3.text = word_meaning[rand_num[2]]  
            btn4.text = word_meaning[rand_num[3]]            
            o_text.text = 'Examples:'
            btn_next.disabled = True
            print('NEW_QUESTIONNNNNNNNNN!!!!!!!!!!!!!!!!!!!!')

        def show_statistics():
            statistics_label.text = 'Right Answers: ' + str(right_answers_stat) + '   ' + 'Wrong Answers: ' + str(wrong_answers_stat)
        def show_result(my_answer, right_answer):
            if right_answer != -1:
                print('SHOW_right_answer=', right_answer)
                if my_answer == 1:
                    btn1.background_color = (0, 200/255, 0, 1)
                    btn2.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 2:
                    btn2.background_color = (0, 200/255, 0, 1)
                    btn1.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 3:
                    btn3.background_color = (0, 200/255, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn4.disabled = True
                else:
                    btn4.background_color = (0, 200/255, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn3.disabled = True
                o_text.text = 'Examples: \n' + real_example[secret_num[0]]
                btn_next.disabled = False
                show_statistics()
            else:
                print('NO RIGHT ANSWER SHOW_right_answer=')
                if my_answer == 1:
                    btn1.background_color = (1, 0, 0, 1)
                    btn2.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 2:
                    btn2.background_color = (1, 0, 0, 1)
                    btn1.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 3:
                    btn3.background_color = (1, 0, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn4.disabled = True
                else:
                    btn4.background_color = (1, 0, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn3.disabled = True
                o_text.text = 'Examples: \n' + real_example[secret_num[0]]
                btn_next.disabled = False
                show_statistics()

        def check_result(my_answer):
            global right_answers_stat
            global wrong_answers_stat
            right_answer = -1
            if rand_num[my_answer-1] == secret_num[0]:
                right_answer=my_answer
                print('rand_num[my_answer-1]', rand_num[my_answer-1])
                print('secret_num[0]', secret_num[0])
                print('right_answer=', right_answer)              
                right_answers_stat += 1
                show_result(my_answer, right_answer)
                print('right_answers_stat', right_answers_stat)
            else:
                print('right_answer', right_answer)     
                wrong_answers_stat += 1
                show_result(my_answer, right_answer)
                print('wrong_answers_stat', wrong_answers_stat)


                  
        new_question('1','2','3','4')

        return superBox
    

if __name__=="__main__":
    New_EngApp().run()

