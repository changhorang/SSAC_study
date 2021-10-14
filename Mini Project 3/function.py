import cv2
import numpy as np
from tkinter import *
from PIL import ImageTk
from PIL import Image

# 함수 모음
# 밝기 조절
def on_bright():
    global img # 밖에있는 img를 갖고 옴
    
    img = Image.fromarray(img)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.add(img, 10)
    imgtk = ImageTk.PhotoImage(image=img)
    
    label.config(image=imgtk)
    label.image = imgtk


# 흑백 처리
def gray_scale():
    global img

    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    
    label.config(image=imgtk)
    label.image = imgtk
    # canvas = Canvas(window, width=512, height=512)
    # img2can = canvas.create_image(256, 256, image=imgtk)
    # canvas.pack(expand=True, fill=BOTH)



# 모자이크 기능
def mosaic():
    global img, start
    rate = 15 # 모자이크에 사용할 축소 비율 (1/rate)
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if (start):
        x,y,w,h = cv2.selectROI('mini-photoshop', img, False) # 관심영역 선택
        if w and h:
            roi = img[y:y+h, x:x+w]   # 관심영역 지정
            roi = cv2.resize(roi, (w//rate, h//rate)) # 1/rate 비율로 축소
            # 원래 크기로 확대
            roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
            img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)


def mosaic_start():
    global start
    start = True

start = False

# reset 기능
def reset():
    global img
    img = cv2.imread(f'data/{name}.jpg')
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (512, 512))
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    
    label.config(image=imgtk)
    label.image = imgtk

# save 기능
def save():
    global img
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite('data/new_img.jpg', img)

### drawing 기능 구현 ###
x1, y1, x2, y2 = 0, 0, 0, 0

# line 그리기
def xy(event):
    global x1, y1
    x1, y1 = event.x, event.y

def draw_line(event):
    global x1, y1, x2, y2
    x2, y2 = event.x, event.y
    canvas.create_line(x1, y1, x2, y2, width=3, fill='red')