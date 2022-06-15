import cv2
import numpy as np
import os
import shutil
 
def image_resize(img_url:str):
    print(f'img_url: {img_url}')
    src1 = cv2.imread('C:\\web\donggri_web\\static\\sorce\\wallpaper.jpg') #배경
    src2 = cv2.imread(img_url) #글자파일 읽기
    
    src2=cv2.resize(src2, (700, 200)) #글씨 작게 수정

    rows, cols,_ = src2.shape
    roi = src1[200:rows+200,150:cols+150] #로고파일 필셀값을 관심영역(ROI)으로 저장함.
    
    gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
    ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
    mask_inv = cv2.bitwise_not(mask)
    
    src1_bg = cv2.bitwise_and(roi,roi,mask=mask) #배경에서만 연산 = src1 배경 복사
    src2_fg = cv2.bitwise_and(src2,src2, mask = mask_inv) #로고에서만 연산

    dst = cv2.bitwise_or(src1_bg, src2_fg) #src1_bg와 src2_fg를 합성    
    src1[200:rows+200,150:cols+150] = dst #src1에 dst값 합성
    s_url = "C:\\web\\donggri_web\\static\\download\\add.jpg"
    cv2.imwrite(s_url,src1)
    return s_url



if __name__ == '__main__':
    shutil.move('C:\\Users\\ns2ju\\Downloads\\Paint.jpg', 'C:\\web\\donggri_web\\static\\sorce\\Paint.jpg')
    
    if os.path.exists('C:\\web\\donggri_web\\static\\sorce\\Paint.jpg'):
        print('yes')
        image_resize('C:\\web\\donggri_web\\static\\sorce\\Paint.jpg')
    else:
        print('NO')

