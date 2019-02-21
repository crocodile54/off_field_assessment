from guizero import App, Window, PushButton, Text, Box, Waffle
from time import sleep, time
from random import randint
from sense_hat import SenseHat
import datetime
s = SenseHat()
score = 0
timelimit = 0
timelimitend = 0

def finalcheck():
    global score
    if score == 5:
        print('passed')
        s.clear(0, 255, 0)

    if score < 5 and score > 1 :
        print('not full marks')
        s.clear(255, 133, 12)

    if score < 2:
        print('failed')
        s.clear(255, 0, 0)
    

def balancetest():
    m = 0
    r = 255, m, 0
    x_values = []
    z_values = []
    global sb, txt, qth, score
    sb.visible=False
    txt.visible=False
    
    stillx = 0.068
    stillz = 0.064
    
    rockx = 0.296
    rockz = 0.228
    
    bigrockx = 0.608
    bigrockz = 0.849

    panacake = Waffle(qth, height=1, width=10, dim=70)

    qth.update()

    for i in range(100):
        raw = s.get_accelerometer_raw()

        x_values.append(raw['x'])
        z_values.append(raw['z'])
        
        sleep(0.2)
        
        if i//10 == i/10:
            t = i/10
            print(t)
            panacake.set_pixel(int(t), 0, r)
            qth.update()
            m = m + 25
            r = 255, m, 0

    for i in range(4):
        panacake.set_all('green')
        qth.update()
        sleep(0.3)
        panacake.set_all('white')
        qth.update()
        sleep(0.3)
        panacake.set_all('green')
        qth.update()
        sleep(0.3)
        panacake.set_all('white')
        qth.update()
        sleep(0.3)
        panacake.set_all('green')
        qth.update()
        sleep(0.3)
        panacake.set_all('white')
        qth.update()
        sleep(0.3)

    panacake.visible=False

    xvalue = max(x_values)-min(x_values)
    zvalue = max(z_values)-min(z_values)

    if xvalue < 0.1 or xvalue < stillx and zvalue < 0.1 or zvalue < stillz:
        print('standing still : passed')
        score = score + 1

    if xvalue > 0.1 and xvalue < 0.4 and zvalue > 0.1 and zvalue < 0.4:
        print('rocking slightly : failed')
        
    if xvalue > 0.4 and zvalue > 0.4:
        print('rocking alot : failed')

    if xvalue > 1 and zvalue > 1:
        print('u fell over')

    print('score is ' + str(score))

    finalcheck()
        
    

def question3():
    global sb, txt, qth
    qth = Window(app, title="Question Three", width=800, height=400)
    qth.show()
    print("start question 3")
    txt = Text(qth, text="Hold the screen out in front of you")
    txt.text_size = 40
    txt.text_color = 'magenta'

    sb = PushButton(qth, text="Begin", padx=240, pady=80, command=balancetest)
    sb.bg ='green'
    sb.text_size = 100
    



def checknumber(lines, x):
    global timelimitend
    global timelimit
    global timel
    global score
    timelimitend = time()
    print('Checking....')
    timel = timelimitend - timelimit
    if int(lines) == x:
        print('correct')
        score = score + 1
        if timel < 5:
            score = score+1
    
    if not int(lines) == x and not int(lines) == 7:
        print('wrong')

    if int(lines) == 7:
        print('no significant answer given')

    print('score is ' + str(score))

    question3()




def questiontwo():
    global timelimit
    qt = Window(app, layout="grid", title="Question Two", width=800, height=400)
    qt.show()
    print("start question 2")

    f1 = Box(qt, width=100, height=400, grid=[0,1])
    f1.border=1
    f1.bg="black"
    
    f2 = Box(qt, width=100, height=400, grid=[1,1])
    f2.border=1
    f2.bg="black"

    f3 = Box(qt, width=100, height=400, grid=[3,1])
    f3.border=1
    f3.bg="black"
    
    f4 = Box(qt, width=100, height=400, grid=[4,1])
    f4.border=1
    f4.bg="black"

    f5 = Box(qt, width=100, height=400, grid=[5,1])
    f5.border=1
    f5.bg="black"

    f6 = Box(qt, width=100, height=400, grid=[6,1])
    f6.border=1
    f6.bg="black"

    f7 = Box(qt, width=100, height=400, grid=[7,1])
    f7.border=1
    f7.bg="black"
    
    f8 = Box(qt, width=100, height=400, grid=[8,1])
    f8.border=1
    f8.bg="black"
 
    bl = [f1,f3,f5,f7]
    x = 0
    for i in range(1,randint(1,4)):
        bl[i-1].bg="yellow"
        x = i
    print(x)

    qt.update()
    sleep(7.35478205493597)

    f1.visible=False
    f2.visible=False
    f3.visible=False
    f4.visible=False
    f5.visible=False
    f6.visible=False
    f7.visible=False
    f8.visible=False

    bo2 = Box(qt, width=800, height=80, grid=[0,1], layout="grid")
    bo2.border=1

    b2pp = Box(qt, width=790, height=100, layout="grid", grid=[0,2])
    b2pp.border=1

    questiotwo = Text(qt, text="How many yellow lines were there?", grid=[0,0])
    questiotwo.text_size = 38

    answer1 = PushButton(b2pp, grid=[0,2], command=checknumber, height=2, width=9, text="One")
    answer1.text_size = 21
    answer1.bg = 'red'
    answer1.update_command(checknumber,args=['1', x])

    answer2 = PushButton(b2pp, grid=[1,2], command=checknumber, height=2, width=9, text="Two")
    answer2.text_size = 21
    answer2.bg = 'orange'
    answer2.update_command(checknumber,args=['2', x])
    
    answer3 = PushButton(b2pp, grid=[2,2], command=checknumber, height=2, width=9, text="Three")
    answer3.text_size = 21
    answer3.bg = 'yellow'
    answer3.update_command(checknumber,args=['3', x])

    answer4 = PushButton(b2pp, grid=[3,2], command=checknumber, height=2, width=9, text="Four")
    answer4.text_size = 21
    answer4.bg = 'green'
    answer4.update_command(checknumber,args=['4', x])

    answer5 = PushButton(b2pp,  grid=[0,3], command=checknumber, height=2, width=9, text="Five")
    answer5.text_size = 21
    answer5.bg = 'brown'
    answer5.update_command(checknumber,args=['5', x])

    answer6 = PushButton(b2pp,  grid=[1,3], command=checknumber, height=2, width=9, text="Six")
    answer6.text_size = 21
    answer6.bg = 'grey'
    answer6.update_command(checknumber,args=['6', x])

    answer7 = PushButton(b2pp,  grid=[2,3], command=checknumber, height=2, width=9, text="Zero")
    answer7.text_size = 21
    answer7.bg = 'purple'
    answer7.update_command(checknumber,args=['0', x])

    answer8 = PushButton(b2pp,  grid=[3,3], command=checknumber, height=2, width=9, text="Dunno")
    answer8.text_size = 21
    answer8.bg = 'blue'
    answer8.update_command(checknumber,args=['7', x])

    timelimit = time()



def checkday(day):
    global score
    global timelimitend
    global timelimit
    timelimitend = time()
    timel = timelimitend - timelimit
    date = datetime.datetime.today().weekday()
    if int(day) == date:
        print ('correct, time is ' + str(timel))
        score = score+1
        if timel < 5:
            score = score+1

    if not int(day) == date and not int(day)==7:
        print('wrong, time is ' + str(timel))

    if int(day) == 7:
        print('no  significant answer given, time is ' + str(timel))

    print('score is ' + str(score))

    questiontwo()
    
def start():
    print('start')
    global timelimit
    
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
    app.update()
    timelimit = time()
    
    

    



app = App(title="Off Field Assessment", height=400, width=800, layout="grid")
button = PushButton(app, grid=[0,0], command=start, text="Start", padx=240, pady=120) 
button.bg = 'green'                                
button.text_size = 100

