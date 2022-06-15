from flask import Flask, render_template, request, redirect,url_for
import requests

app = Flask(__name__)
 
@app.route('/', methods=['GET','POST'])
def main():
    
    with open("C:\\web\\donggri_web\\static\\story_img\\story1.txt","r", encoding="UTF-8") as f:
        lines = f.read().splitlines()
    print(lines)     

    return render_template('fairytale.html',storyli=lines)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

