import random
import time


# File name: New_Eng.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

"""

# Getting data from file
filename='./eng-rus.txt'
s = open(filename).read()
lines = [line.strip() for line in open(filename)]

print(lines)

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

word_list=column4
word_meaning=column3
example_list=column1
example_meaning=column2
real_example=column5

"""


word_list=[]
word_meaning=[]
example_list=[]
example_meaning=[]
real_example=[]
word_list = ['уму непостижимо', 'журнальная/ багажная полка', 'мучиться от боли/чувства вины и т. д.', 'ломать себе голову', 'раздобыть, добиться, наделать', 'вешалка для полотенец', 'полка для верхней одежды', 'яма для барбекю', 'дурное предчувствие', 'приспособление', 'мед. учреждение', 'возвращаться к чему-либо ', 'изменение порядка, возвращение к прежнему состоянию', 'размалывать кофе', 'измельчитель кофе', 'точильный камень ', 'скрежетать зубами', 'мучить, изводить', 'ежедневная изнурительная работа', 'смять сигаретный окурок в перелнице', 'застопориться / остановиться', 'переходить к делу/ к сути', 'в полнейшем беспорядке', 'товар', 'Его признали невиновным (на суде)', 'Он/она взмолилась', 'молить о пощаде/ жалости / сострадании', 'ссылаться не неосведомленность', 'защищать кого-либо/чьи-либо интересы в суде', 'показать/ проявить смелость в сложной ситуации', 'перед лицом сложной ситуации', 'тележка в супермаркете', 'тележка для багажа', 'трамвай', 'не в себе, помешанный, спятивший', 'совершенно безумный', 'колокольня', 'глупая идея', 'коллектив', 'харизма, притягательная сила', 'харизматический, притягательный', 'пятна краски', 'прилежный / усердный сдудент', 'раскаиваться', 'искреннее раскаяние', 'промокать (тряпочкой, промокашкой)', 'стирать / вычеркивать из памяти воспоминания', 'заслонять солнце', 'чернильные пятна', 'пятно на репутации', 'еда на вынос', 'обновлять / подписывать / брать в аренду', 'аренда ч-л', 'подписать 3-х годичный контракт об аренде', 'возродить надежду, возвратить жизненные силы', 'взять в аренду офисное пространство', 'предоставить землю в аренду ', 'киль', 'падать (в обморок)', 'водопроводчик', 'водопровод', 'существует огромное кол-во слухов / слухи множатся', 'после 2-х лет застоя', 'фондовый рынок находится в состоянии застоя', 'хандрить', 'полагаться на себя, заботиться о себе', 'смочь отбиться от нападающих / грабителей', 'парировать вопросы', 'крыло автомобиля']
word_meaning = ['the mind boggles / it boggles the mind', 'a magazine/luggage rack', 'to be racked with pain/guilt, etc', 'to rack your brain/brains', 'to rack up sth', '? towel ? rail / rack', 'a coat rack', 'a barbecue pit', 'a sense of foreboding', 'facility', 'medical facility', 'to revert to sth/doing sth', 'reversion', 'to grind coffee', 'a coffee grinder', 'a stone for grinding knives and scissors', 'to grind your teeth', 'to grind sb down', 'the daily grind', 'to grind a cigarette butt into the ashtray', 'to grind to a halt', 'to cut to the chase', 'in complete disarray', 'commodity', 'He pleaded not guilty to', 'he/she pleaded (with)', 'to plead for mercy', 'to plead ignorance', "to plead sb's case/cause", 'to show courage in adversity', 'in the face of adversity', 'a supermarket trolley', 'a luggage trolley', 'trolley', 'off your trolley', 'as mad as a hatter', 'belfry', 'daft idea', "collective [k?'lekt?v], group, body", 'сharisma / k??r?zm? /', 'charismatic', 'flecks of paint', 'a diligent student', 'repent', 'sincerely repentant', 'blot', 'to blot out memories of', 'blots out the sun', 'ink blots', 'blot on reputation', 'takeaway', 'renew / sign / take a lease', 'a lease of / on sth', 'to sign a three-year lease', 'give sb/sth a new lease of life', 'to lease some office space', 'to lease the land to a local company', 'keel', 'keel over', 'plumber', 'plumbing', 'rumours abound about …', 'after two years in the doldrums', 'the stock market is in the doldrums', 'in the doldrums / ?d?ldr?mz /', 'fend for yourself', 'to managed to fend off attackers / muggers', 'to fend off questions about', 'fender']
example_list = ['the mind boggles / it boggles the mind', 'rack', 'be racked with pain/guilt, etc', 'rack your brain/brains', 'rack up sth', '? towel ? rail / rack', 'a coat rack', 'pit', 'foreboding', 'facility', 'facility', 'revert to sth/doing sth', 'reversion', 'grind', 'grind', 'grind', 'grind your teeth', 'grind sb down', 'grind', 'grind', 'grind to a halt', 'cut to the chase', 'disarray', 'commodity', 'plead', 'plead', 'plead', 'plead', "plead sb's case/cause", 'adversity', 'adversity', 'trolley', 'trolley', 'trolley', 'off your trolley', 'as mad as a hatter', 'belfry', 'daft', "collective [k?'lekt?v], group, body", 'сharisma / k??r?zm? /', 'charismatic', 'fleck', 'diligence', 'repent', 'repentance', 'blot', 'blot sth out', 'blot', 'blot', 'a blot on sth', 'takeaway', 'renew / sign / take a lease', 'a lease of / on sth', 'lease  / li?s /', 'give sb/sth a new lease of life', 'lease / li?s /', 'lease / li?s /', 'keel', 'keel over', 'plumber', 'plumbing', 'abound', 'in the doldrums / ?d?ldr?mz /', 'in the doldrums / ?d?ldr?mz /', 'in the doldrums / ?d?ldr?mz /', 'fend for yourself', 'fend sb/sth off', 'fended off questions about', 'fender']
example_meaning = ['the mind boggles / it boggles the mind', 'полка, вешалка, стойка', 'be racked with pain/guilt, etc', 'rack your brain/brains', 'rack up sth', 'вешалка для полотенец', 'полка для верхней одежды', 'яма', 'дурное предчувствие', 'приспособление', 'учреждение', 'возвращаться к чему-либо ', 'изменение порядка, возвращение к прежнему состоянию', 'молоть, размалывать', 'молоть, размалывать', 'точить, оттачивать ', 'скрежетать зубами', 'мучить, изводить', 'изнурительная, однообразная работа', 'молоть, размалывать', 'застопориться / остановиться', 'переходить к делу/ к сути', 'беспорядок', 'товар', '(не) признавать себя виновным (на суде)', 'умолять', 'умолять', 'оправдываться, ссылаться на что-либо', 'защищать кого-либо/чьи-либо интересы в суде', 'трудность, напасть', 'трудность, напасть', 'тележка', 'тележка', 'трамвай', 'не в себе, помешанный, спятивший', 'совершенно безумный', 'колокольня', 'глупый', 'коллектив', 'харизма, притягательная сила', 'харизматический, притягательный', 'пятнышко, крапинка', 'усердие ', 'раскаиваться', 'раскаяние', 'промокать (тряпочкой, промокашкой)', 'стирать, вычеркивать из памяти', 'заслонять', 'пятно, клякса', 'пятно', 'еда на вынос', 'обновлять / подписывать / брать в аренду', 'аренда ч-л', 'контракт об аренде', 'возродить надежду, возвратить жизненные силы', 'сдавать/брать в аренду', 'сдавать/брать в аренду', 'киль', 'падать (в обморок)', 'водопроводчик', 'водопровод', 'существовать в большом количестве', 'период застоя', 'период застоя', 'хандрить', 'полагаться на себя, заботиться о себе', 'отражать, парировать', 'парировать вопросы', 'крыло автомобиля']
real_example = ['The mind boggles at the stupidity of some people. / The paperwork you have to fill out just boggles the mind.', '-', 'Afterwards, he was racked with guilt and shame.', '-', "He's racked up debts of over thirty thousand pounds. / They racked up a nine-game winning streak.", '-', '-', '-', 'We waited for news of the men with a sense of foreboding.', 'This phone has a memory facility.', 'a new medical facility', 'For a while I ate low-fat food but then I reverted to my old eating habits. / For a while I ate low-fat food but then I reverted to my old eating habits.', '-', 'Could you grind some coffee for me?', '-', '-', '-', 'Living alone in London really ground me down.', 'The work has become a grind to them.', 'He paused and ground his cigarette butt into the ashtray.', 'If something grinds to a halt, it stops moving or making progress: Traffic slowly ground to a halt', '-', 'The house was in complete disarray . / papers in disarray on the desk', '-', 'He pleaded not guilty to five felony charges.', '"You must believe me!"" she pleaded. / He pleaded with her to come back."', '-', "You'll just have to plead ignorance (= say you did not know) .", '-', 'She showed a great deal of courage in adversity .', 'We remained hopeful in the face of adversity.', '-', '-', '-', '-', '-', '-', "That's a daft idea .", '-', '-', '-', 'His shirt was covered in flecks of paint. / a black beard with flecks of gray', '-', '-', 'His apology was sincerely repentant.', '-', "I've tried to blot out memories of my relationship with Dieter. / He tried to blot out the memory of that night.", 'If smoke or cloud blots out the sun, it prevents it from being seen / Black clouds blotted out the sun.', '-', 'The financial scandal was a blot on his reputation.', '-', '-', '-', 'We signed a three-year lease when we moved into the house.', 'The operation has given her a new lease of life.', 'We want to lease some office space in the centre of town.', 'The council eventually leased the land to a local company.', '-', 'He said he felt dizzy and then just keeled over. / Rob looked as if he were ready to keel over.', '-', '-', 'Rumours abound about a possible change of leadership.', 'After two years in the doldrums, profits are finally rising.', 'The stock market has been in the doldrums for most of this year.', '-', 'When you go away to college, you have to learn to fend for yourself. / You’ll have to fend for yourself while I’m gone.', 'They managed to fend off their attackers with rocks and sticks. / Mrs. Spector tried to fend off the other mugger', 'She fended off questions about her marriage.', '-']

num=[]
for i in range(0,len(word_list)):
    num.append(i)

print(word_list)
print(word_meaning)
print(example_list)
print(example_meaning)
print(real_example)

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

        def show_statistics():
            statistics_label.text = 'Right Answers: ' + str(right_answers_stat) + '   ' + 'Wrong Answers: ' + str(wrong_answers_stat)
        def show_result(my_answer, right_answer):
            if right_answer != -1:
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
                right_answers_stat += 1
                show_result(my_answer, right_answer)
            else:   
                wrong_answers_stat += 1
                show_result(my_answer, right_answer)
              
        new_question('1','2','3','4')

        return superBox
    
if __name__=="__main__":
    New_EngApp().run()

