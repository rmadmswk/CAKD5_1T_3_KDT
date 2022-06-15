# from flask import Flask, session, render_template, request, jsonify, escape
from flask import Flask, render_template, request, redirect,url_for
import shutil
import kakao
import image_add
import os
import time 

app = Flask(__name__)
 
@app.route('/', methods=['GET','POST'])
def main(): 
    if os.path.exists('C:\\Users\\ns2ju\\Downloads\\Paint.jpg'):
        os.remove('C:\\Users\\ns2ju\\Downloads\\Paint.jpg')
    image_path = 'C:\\web\\donggri_web\\static\\sorce\\Paint.jpg'
     
    if request.method == 'POST':
        time.sleep(2)
        shutil.move('C:\\Users\\ns2ju\\Downloads\\Paint.jpg', image_path)
        image_path = image_add.image_resize(image_path)
        ori_spell , corr_spell = kakao.ocr_main(image_path)  
        print(f"ori_spell: {ori_spell}, corr_spell: {corr_spell}")    
        return render_template('printing.html',ori_spell=ori_spell,corr_spell=corr_spell)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
         
     
    

