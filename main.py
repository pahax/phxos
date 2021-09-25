import os
import pyaudio
import wave

text = open("pasword.txt","r", encoding = 'UTF-8')
ps = text.read()
text.close()

def inputaudio():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)['name'])
    
    inddevice = int(input(">>>Введите индекс микрофона: "))
    recsec = int(input(">>>Введите количество секунд: "))
    namefile = str(input(">>>Введите имя файла: "))
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = recsec
    WAVE_OUTPUT_FILENAME = namefile
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=inddevice, 
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    os.replace(namefile, "main/" + "muzic/" + namefile)

def calc():
    operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    + для сложения
    - для вычитания
    * для умножения
    / для деления
    ''')
    number_1 = int(input('>>>Введите своё первое число: '))
    number_2 = int(input('>>>Введите своё второе число: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Вы ввели недействительный оператор, пожалуйста, запустите программу еще раз.')

def password():
    text = open("pasword.txt" ,"w", encoding = 'UTF-8')
    textf = str(input(">>>Введите новый пароль: "))
    print(textf, file = text)
    text.close()
    
def passwordD():
    text = open("pasword.txt" ,"w", encoding = 'UTF-8')
    print("0", file = text)
    text.close()

def deleteD():
    way ='main/' + str(input(">>>Введите путь: "))
    name = str(input(">>>Введите имя: "))
    os.rmdir(way + name)

def deleteF():
    way ='main/' + str(input(">>>Введите путь: "))
    name = str(input(">>>Введите имя: "))
    os.remove(way + name)

def helpme():
    print()

def createF():
    way = str(input(">>>Введите путь: "))
    name = str(input(">>>Введите имя: "))
    ctext = open("main/" + way + "/" + name, "w", encoding = 'UTF-8')
    ctext.close()
    
def replace():
    way = str(input(">>>Введите путь: "))
    way2 = str(input(">>>Введите куда переместить: "))
    os.replace("main/" + way, "main/" + way2)

def look():
    cd = 'main/' + str(input('>>>Введите путь: '))
    print(os.listdir(cd))
    
def createD():
    way = str(input(">>>Введите путь: "))
    os.chdir("main/" + way)
    os.mkdir(str(input('>>>Введите название: ')))
    os.chdir("C:\pythonfs")#изменить здесь на место куда кинули этот проект
    
def rename():
    way = str(input(">>>Введите путь: "))
    way = way + "/"
    name = str(input(">>>Введите имя: "))
    name2 = str(input(">>>Введите переименнованое имя файла: "))
    os.rename("main/" + way + name, "main/"+ way + name2)

def text():
    way = str(input(">>>Введите путь: "))
    text = open("main/" + way ,"r", encoding = 'UTF-8')
    txt = text.read()
    print(txt)
    text.close()
    text = open("main\\" + way ,"a", encoding = 'UTF-8')
    textf = str(input(">>>Введите текст: "))
    print(textf, file = text)
    text.close()

def main():
    while True:
        main = input(">>>")
    
        while main == "help":
            helpme()
        
        while main == "text":
            text()
            break
        
        while main == "rename":
            rename()
            break
        
        while main == "replace":
            replace()
            break
            
        while main == "createD":
            createD()
            break
        
        while main == "ls":
            look()
            break
        
        while main == "deleteF":
            deleteF()
            break
        
        while main == "deleteD":
            deleteD()
            break
        
        while main == "createF":
            createF()
            break
        
        while main == "password":
            password()
            break
        
        while main == "Delete pass":
            passwordD()
            break
        
        while main == "calculator":
            calc()
            break
        
        while main == "input audio":
            inputaudio()
            break
        
        if main == "close":
            break

if ps == '0' + '\n':
    main()
else:
    while True:
        nps = str(input(">>>Введите пароль: ")) + '\n'
        if nps == ps:
            main()
            break
        else:
            print('Неверный пароль')