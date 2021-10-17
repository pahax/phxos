import os, os.path, wave, pyautogui, keyboard, random
import pyaudio#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio https://www.youtube.com/watch?v=8DmM40QC1pc
from time import sleep
from PIL import Image
from colorama import Fore, Back, Style


text = open("pasword.txt","r", encoding = 'UTF-8')
ps = text.read()
text.close()

def stone():
    a = ["камень", "ножници", "бумага"]
    qw = input("Введите камень, ножници или бумага\n")
    rd = a[random.randint(0, len(a) - 1)]
    if (qw == "камень" and rd == "бумага") or (qw == "ножници" and rd == "камень") or (qw == "бумага" and rd == "ножници"):
        print(rd)
        print("Ты проиграл")
    elif (qw == "камень" and rd == "ножници") or (qw == "ножници" and rd == "бумага") or (qw == "бумага" and rd == "камень"):
        print(rd)
        print("Ты выйграл")
    elif (qw == "камень" and rd == "камень") or (qw == "ножници" and rd == "ножници") or (qw == "бумага" and rd == "бумага"):
        print(rd)
        print("Ничья")

def numbers():
    a = random.randint(5,30)
    x = 50
    while a != 0:
        if a % 2 == 0 and x % 2 == 0:
            print(str(a))
            z = str(input("Ваше число чётное: введите -1 или /2  "))
            if z == "-1":
                a -= 1
                x -= 1
            elif z == "/2":
                a = a / 2
                x -= 1
            else:
                print("Введите -1 или /2")
        elif a % 2 == 1 and x % 2 == 0:
            print(str(a))
            z = str(input("\nВаше число нечётное: введите -1  "))
            if z == "-1":
                a -= 1
                x -= 1
            else:
                print("Введите -1")
        elif a % 2 == 0 and x % 2 == 1:
            b = random.randint(1,2)
            if b == 1:
                a = a / 2
                x -= 1
            else:
                a -= 1
                x -= 1
        elif a % 2 == 1 and x % 2 == 1:
            a -= 1
            x -= 1
    if x % 2 == 0:
        print("Ты проиграл")
    else:
        print("Ты выйграл")

def games():
    iaia = str(input(">>>Введите название игры: "))
    if iaia == "snake":
        os.system('python snake.py')
    elif iaia == "stone":
        stone()
    elif iaia == "number":
        numbers()

def hotkey():
    while True:
        if  keyboard.is_pressed("shift + t"):
            text()
        if  keyboard.is_pressed("shift + h"):
            heplmehk()
        if keyboard.is_pressed("shift + r + n"):
            rename()
        if keyboard.is_pressed("shift + r + p"):
            replace()
        if keyboard.is_pressed("shift + c + d"):
            createD()
        if keyboard.is_pressed("shift + l"):
            look()
        if keyboard.is_pressed("shift + d + f"):
            deleteF()
        if keyboard.is_pressed("shift + d"):
            deleteD()
        if keyboard.is_pressed("shift + c + f"):
            createF()
        if keyboard.is_pressed("shift + p"):
            password()
        if keyboard.is_pressed("shift + p + d"):
            passwordD()
        if keyboard.is_pressed("shift + c + a"):
            os.system('python mm.py')
        if keyboard.is_pressed("shift + i + a"):
            inputaudio()
        if keyboard.is_pressed("shift + g"):
            games()
        if keyboard.is_pressed("shift + i"):
            image()
        if keyboard.is_pressed("shift + s"):
            name = input("Введите имя файла")
            pyautogui.screenshot(name)
            os.replace(name, "main/images/screenshots/" + name)
        if keyboard.is_pressed("esc"):
            break
        

def heplmehk():
    pass

def image():
    while True:
        qween = input(Back.RED + ">>>Введите что сделать с файлом: ")
        if qween == "open":
            way ='main/' + str(input(Back.RED + ">>>Введите путь: "))
            name = str(input(Back.RED + '>>>Введите название: '))
            if os.path.exists("main/" + way) == True:
                image = Image.open(way + name)
                image.show()
            else:
                print(Fore.RED + "\n>>>Этого файла не существует\n")
                print(Style.RESET_ALL)
        elif qween == "convert":
            way ='main/' + str(input(Back.RED + ">>>Введите путь: "))
            name = str(input(Back.RED + '>>>Введите название: '))
            tatras = Image.open(way + name)
            tatras.save(way + str(input(Back.RED + '>>>Введите название: ')), str(input(Back.RED + '>>>Введите расширение: ')))
            os.remove(way + name)
            if os.path.exists(way + name) == True:
                image = Image.open(way + name)
                image.show()
            else:
                 print(Fore.RED + "\n>>>Этого файла не существует\n")
                 print(Style.RESET_ALL)


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
    print(Back.RED)
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

def password():
    while True:
        if ps == '0' + '\n':
            while True:
                text = open("pasword.txt" ,"w", encoding = 'UTF-8')
                textf = str(input(">>>Введите новый пароль: "))
                print(textf, file = text)
                text.close()
                break
            break
        else:
            nps = str(input(">>>Введите пароль: ")) + '\n'
            if nps == ps:
                while True:
                    text = open("pasword.txt" ,"w", encoding = 'UTF-8')
                    textf = str(input(">>>Введите новый пароль: "))
                    print(textf, file = text)
                    text.close()
                    break
                break
            else:
                print('Неверный пароль')
    
def passwordD():
    text = open("pasword.txt" ,"w", encoding = 'UTF-8')
    print("0", file = text)
    text.close()

def deleteD():
    way ='main/' + str(input(">>>Введите путь: "))
    name = str(input(">>>Введите имя: "))
    if os.path.exists(name and way) == True:
        os.rmdir(way + name)
    else:
        print(Fore.RED + "\n>>>Файл не найден")
        print(Style.RESET_ALL)

def deleteF():
    way ='main/' + str(input(">>>Введите путь: "))
    name = str(input(">>>Введите имя: "))
    if os.path.exists(name and way) == True:
        os.remove(way + name)
    else:
        print(Fore.RED + "\n>>>Файл не найден")
        print(Style.RESET_ALL)

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
    if os.path.exists(way and way2) == True:
        os.replace("main/" + way, "main/" + way2)
    else:
        print(Fore.RED + "\n>>>Файл не найден")
        print(Style.RESET_ALL)

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
    if os.path.exists(name and way) == True:
        name2 = str(input(">>>Введите переименнованое имя файла: "))
        os.rename("main/" + way + name, "main/"+ way + name2)
    else:
        print(Fore.RED + "\n>>>Файл не найден\n")
        print(Style.RESET_ALL)

def text():
    while True:
        print(">>>Для выхода введите exit")
        cat = input(">>>Введите расширение:")
        textf = "1"
        if cat == "r":
            way = str(input(">>>Введите путь: "))
            if os.path.exists("main/" + way) == True: 
                text = open("main/" + way ,"r", encoding = 'UTF-8')
                txt = text.read()
                print(txt)
            else:
                print(Fore.RED + "\n>>>Файл не найден\n")
                print(Style.RESET_ALL)
        elif cat == "a":
            way = str(input(">>>Введите путь: "))
            if os.path.exists("main/" + way) == True:
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
            else:
                print(Fore.RED + "\n>>>Файл не найден")
                print(Style.RESET_ALL)
        elif cat == "w":
            way = str(input(">>>Введите путь: "))
            if os.path.exists("main/" + way) == True: 
                text = open("main\\" + way ,"w", encoding = 'UTF-8')
                textf = str(input(">>>Введите текст: "))
                print(textf, file = text)
                text.close()
            else:
                print(Fore.RED + "\n>>>Файл не найден\n")
                print(Style.RESET_ALL)
        elif cat == "exit":
            break

def main():
    print("/\     /\ ")
    print("  • _ •  ")
    print("Введите help для справки")
    while True:
        a = keyboard.is_pressed('shift + s')
        
        if a:
            keyboard.write("")
            keyboard.press_and_release('enter')
            pyautogui.screenshot("screenshot.png")
            name = pyautogui.screenshot("screenshot.png")
            os.replace(name, "main/images/screenshots/" + name)
        
        main = input(Back.CYAN + ">>>")
        
        while main == "hk":
            print(Style.RESET_ALL)
            hotkey()
            break
        
        while main == "help":
            print(Style.RESET_ALL)
            helpme()
            break
        
        while main == "text":
            print(Style.RESET_ALL)
            text()
            break
        
        while main == "rename":
            print(Style.RESET_ALL)
            rename()
            break
        
        while main == "replace":
            print(Style.RESET_ALL)
            replace()
            break
            
        while main == "createD":
            print(Style.RESET_ALL)
            createD()
            break
        
        while main == "ls":
            print(Style.RESET_ALL)
            look()
            break
        
        while main == "deleteF":
            print(Style.RESET_ALL)
            deleteF()
            break
        
        while main == "deleteD":
            print(Style.RESET_ALL)
            deleteD()
            break
        
        while main == "createF":
            print(Style.RESET_ALL)
            createF()
            break
        
        while main == "password":
            print(Style.RESET_ALL)
            password()
            break
        
        while main == "Delete pass":
            print(Style.RESET_ALL)
            passwordD()
            break
        
        while main == "calculator":
            print(Style.RESET_ALL)
            os.system('python mm.py')
            break
        
        while main == "input audio":
            print(Style.RESET_ALL)
            inputaudio()
            break
        
        while main == "games":
            print(Style.RESET_ALL)
            games()
            break
        
        while main == "delete file system":
            print(Style.RESET_ALL)
            delete_file_system()
            break
        
        while main == "image":
            print(Style.RESET_ALL)
            image()
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