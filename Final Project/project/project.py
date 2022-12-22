import tkinter as tk
from tkinter import *
import csv
from PIL import Image, ImageTk
from urllib.request import urlopen
import requests
import random

class ImgError(Exception):
    pass


def main():
    request()
    tkinter_window()

def request():
    try:
        rand_num = random.randint(1,20)
        call = requests.get(f'https://api.rawg.io/api/games?key=8df316f0b3c24b95930962bc1b183eb8&page={rand_num}&page_size=1').json()
#page=1&page_size=1

        result_list = call['results']

        with open('groups.csv', 'w') as csvfile:
            fieldnames = ['name', 'image']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in result_list:
                writer.writerow({'name': item['name'], 'image': item['background_image']})
        return 'y'
    except:
        return f'Server not available, try again in a few minutes'


def resizer(im,new_width):
    try:
        width, height = im.size
        imgratio = height/width
        new_height = int(imgratio*new_width)
        resized_img = im.resize((new_width,new_height))
        return resized_img
    except:
        raise ImgError


def tkinter_window():
    window = tk.Tk()

    window.geometry('1000x800')
    window.title('Video Game Picture Guessing Game')

    heading = tk.Label(window, text='Guess the game!', font=('Arial', 22))
    heading.pack()

    with open('groups.csv', 'r') as csvfile:
        for row in csv.DictReader(csvfile):
            imgurl = urlopen(row['image'])
            img = Image.open(imgurl)
            resized = resizer(img,800)
            photo = ImageTk.PhotoImage(resized)
            image_area = tk.Label(image=photo)
            image_area.image = photo
            image_area.pack(padx=20,pady=20)

    def click():
        answer = entry.get()
        correct_answer = row['name']
        if answer == correct_answer:
            image_area.destroy()
            entry.destroy()
            button.destroy()
            message.destroy()
            correct = tk.Label(window, text='Correct!', font=('Arial', 22))
            correct.pack(padx=300,pady=300)
        else:
            image_area.destroy()
            entry.destroy()
            button.destroy()
            message.destroy()
            incorrect = tk.Label(window, text=f'Correct answer: \n {correct_answer}', font=('Arial', 22))
            incorrect.pack(padx=300,pady=300)

    message = tk.Label(window, text='Please type the name exactly with any capital letters, spaces or puctuation', font=('Arial', 13))
    message.pack()
    entry = tk.Entry(window)
    entry.pack(pady=5)
    button = tk.Button(window, text='Submit Answer', command=click)
    button.pack()

    window.mainloop()
    return 'running'

if __name__ == '__main__':
    main()