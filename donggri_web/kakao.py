import json
import requests
import sys
import cv2
from hanspell import spell_checker


def kakao_ocr(image_path: str):
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'
    headers = {'Authorization': "KakaoAK " + "635e11243e3d9903a61094ae4ec459dc"}

    # print(f"image_path :{image_path}")
    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".JPG", image)[1]
    data = jpeg_image.tobytes()

    return requests.post(API_URL, headers=headers, files={"image": data})

def ocr_main(image_url:str):
    image_path = image_url
    output = kakao_ocr(image_path).json()
    # outputdata = json.dumps(output, ensure_ascii=False,sort_keys=True, indent=2)
    # print(output['result'][0]['recognition_words'][0])
    ocr_spell = output['result'][0]['recognition_words'][0]
    corr_spell = check_spell(ocr_spell)
    return ocr_spell , corr_spell
    # print(output['recognition_words'])
    # print("[ocr] output:\n{}\n".format(json.dumps(output,ensure_ascii=False,sort_keys=True, indent=2)))
    # #받은 데이터 array로 변환
    # outputdata2 = json.loads(outputdata)
    

def check_spell(ocr_spell:str):
    # print(ocr_spell)
    spelled_sent = spell_checker.check(ocr_spell)
    hanspell_sent = spelled_sent.checked
    # print(hanspell_sent)
    return hanspell_sent

class KakaoTTS:
    
   def __init__(self, text, API_KEY="635e11243e3d9903a61094ae4ec459dc"):
      self.resp = requests.post(
         url="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
         headers={
            "Content-Type": "application/xml",
            "Authorization": f"KakaoAK {API_KEY}"
         },
         data=f"<speak><voice name='WOMAN_DIALOG_BRIGHT'>{text}</voice></speak>".encode('utf-8')
      )

   def save(self, filename="output.mp3"):
      with open(filename, "wb") as file:
         file.write(self.resp.content)
         
 
if __name__ == "__main__":
    tts = KakaoTTS("텍스트")
    tts.save("C:\\web\\donggri_web\\static\\story_sound\\output.mp3")
    # ocr_main()

