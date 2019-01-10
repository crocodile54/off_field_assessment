from guizero import App, Window, PushButton, Text, Box
from time import sleep
import datetime

score = 0

def checkday(day):
    global score
    date = datetime.datetime.today().weekday()
    if int(day) == date:
        print ('correct')
        score = score+1

    if not int(day) == date and not int(day)==7:
        print('wrong')

    if int(day) == 7:
        print('no  significant answer given')

    print('score is ' + str(score))

def start():
    print('start')
    sleep(0.5)
    button.hide()

    box = Box(app, width=800, height=80, grid=[0,1], layout="grid")
    box.border=1

    bapp = Box(app, width=790, height=100, layout="grid", grid=[0,2])
    bapp.border=1

    questionone = Text(app, text="What day is it today?", grid=[0,0])
    questionone.text_size = 40
    
    monday = PushButton(bapp, grid=[0,2], command=checkday, height=2, width=9, text="Monday")
    monday.text_size = 21
    monday.bg = 'red'
    monday.update_command(checkday,args='0')
    
    tuesday = PushButton(bapp, grid=[1,2], command=checkday, height=2, width=9, text="Tuesday")
    tuesday.text_size = 21
    tuesday.bg = 'orange'
    tuesday.update_command(checkday,args='1')

    wednesday = PushButton(bapp, grid=[2,2], command=checkday, height=2, width=9, text="Wednesday")
    wednesday.text_size = 21
    wednesday.bg = 'yellow'
    wednesday.update_command(checkday,args='2')

    thursday = PushButton(bapp,  grid=[3,2], command=checkday, height=2, width=9, text="Thursday")
    thursday.text_size = 21
    thursday.bg = 'green'
    thursday.update_command(checkday,args='3')

    friday = PushButton(bapp,  grid=[0,3], command=checkday, height=2, width=9, text="Friday")
    friday.text_size = 21
    friday.bg = 'brown'
    friday.update_command(checkday,args='4')

    saturday = PushButton(bapp,  grid=[1,3], command=checkday, height=2, width=9, text="Saturday")
    saturday.text_size = 21
    saturday.bg = 'grey'
    saturday.update_command(checkday,args='5')

    sunday = PushButton(bapp,  grid=[2,3], command=checkday, height=2, width=9, text="Sunday")
    sunday.text_size = 21
    sunday.bg = 'purple'
    sunday.update_command(checkday,args='6')

    dunno = PushButton(bapp, grid=[3,3], command=checkday, height=2, width=9, text='Dunno?')
    dunno.text_size = 21
    dunno.bg = 'blue'
    dunno.update_command(checkday,args='7')



    



app = App(title="Off Field Assessment", height=400, width=800, layout="grid")
button = PushButton(app, grid=[0,0], command=start, text="Start", padx=240, pady=120) 
button.bg = 'green'                                
button.text_size = 100

