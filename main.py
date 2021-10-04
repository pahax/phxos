import os
import pyaudio#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio https://www.youtube.com/watch?v=8DmM40QC1pc
import wave
from time import sleep

text = open("pasword.txt","r", encoding = 'UTF-8')
ps = text.read()
text.close()

def dfs():
    print("самоуничтожение через:")
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    os.remove("main.py")

def delete_file_system():
    while True:
        if ps == '0' + '\n':
            dfs()
            break
        else:
            nps = str(input(">>>Введите пароль: ")) + '\n'
            if nps == ps:
                dfs()
                break
            else:
                print('Неверный пароль')
            
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
    print("•text чтобы открыть текст\n•rename чтобы переименовать\n•createD чтобы создать директорию\n•createF чтобы создать текстовой файл\n•deleteD чтобы удалить директорию\n•deleteF чтобы удалить текстовой файл\n•ls чтобы посмотреть что начодится в директории\n•password чтобы изменить пароль\n•Delete pass чтобы удалить пароль\n•calculator чтобы открыть калькулятор\n•input audio чтобы записать аудио\n•close чтобы закрыть файловую систему")

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
    while True:
        print(">>>Для выхода введите exit")
        cat = input(">>>Введите расширение:")
        textf = "1"
        if cat == "r":
            way = str(input(">>>Введите путь: "))
            text = open("main/" + way ,"r", encoding = 'UTF-8')
            txt = text.read()
            print(txt)
        elif cat == "a":
            way = str(input(">>>Введите путь: "))
            text = open("main/" + way ,"r", encoding = 'UTF-8')
            txt = text.read()
            print(">>>Для выхода введите esc")
            print(txt)
            text.close()
            while True:
                textf = str(input(">>>Введите текст: "))
                if textf == "esc":
                    break
                else:
                    text = open("main\\" + way ,"a", encoding = 'UTF-8')
                    print(textf, file = text)
                    text.close()
        elif cat == "w":
            way = str(input(">>>Введите путь: "))
            text = open("main\\" + way ,"w", encoding = 'UTF-8')
            textf = str(input(">>>Введите текст: "))
            print(textf, file = text)
            text.close()
        elif cat == "exit":
            break

def main():
    print("/\     /\ ")
    print("  • _ •  ")
    print("Введите help для справки")
    while True:
        main = input(">>>")
    
        while main == "help":
            helpme()
            break
        
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
        
        while main == "delete file system":
            delete_file_system()
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