# CAKD5_1팀_3차_KDT
# 3차 프로젝트 - 아동 기초 언어 능력 향상을 위한 AI 솔루션
※ 22.07.01 카카오 OCR API 지원 중지
- 프로젝트 기간 - 22.05.09 ~ 22.06.13
- 팀원 - 이동연, 김기연, 김재경, 용지영, 정현우, 최지원
- 사용라이브러리 - colab, vscode
- 사용언어 - python, flask, html
- 맡은 일 - 최적의 OCR 라이브러리 구성, Back-end 동화 솔루션 알고리즘 구현, 사업 구현 가능성 조사
# 순서
- 타겟층(6~8세)를 가르치는 유치원,초등학교 교사 16명을 상대로 설문조사 및 솔루션이 필요한 이유 확립
- 필요한 라이브러리 OCR,TTS,Py-hanspell,Konlpy를 우리가 사용할 수 있게 조정
- 웹 구현
# 아쉬운점
- 한국어 OCR 라이브러리(tesseract,EasyOCR,OCR-Kor,kakao API)를 우리가 사용할 수 있게 변경했지만, 파인튜닝은 하지 못함
- OCR 라이브러리들이 모두 AI허브 어린이용 손글씨가 포함된 손글씨 데이터를 사용했는데, 결과값이 제일 좋았던게 kakao API였고, 
- 필요한 어린이 손글씨 데이터를 구하지 못했고, 증식을 통해 늘려보려 했지만 짧은 시간안에 결과를 낼 수 있을지 확신 할 수 없어 못함
- 솔루션을 개발하기 위해 라이브러리를 조사하면서 찾은 rq transformer를 사용하지 못해 자유로운 솔루션에서 형식을 추가하면서 기술력과 내용이 약해짐 
# rq transformer : 테디베어
![image](https://user-images.githubusercontent.com/83449928/175809593-840ac6fe-c3d3-4f1b-8a74-a7526661f514.png)
# 배운점
- kakao OCR 라이브러리 document를 통해 구성하는 모델과 진행방식 파악
- 글자 탐지 모델 : RCNN, single shot detector, East, yolo
- 글자 인식 모델 : CNN, RNN, CTC
- kakao OCR,TTS,Py-hanspell,Konlpy 라이브러리 

메뉴
![image](https://user-images.githubusercontent.com/83449928/175809653-4c20a6e1-7db1-4ad5-b848-c90535e6aad1.png)
동화 OCR 입력창
![image](https://user-images.githubusercontent.com/83449928/175809661-4417cd51-5df1-41e9-9fa5-3cc61a10c2e6.png)
결과
![image](https://user-images.githubusercontent.com/83449928/175809673-c6ccb250-b5e7-4324-9f53-37d56d858a10.png)
반복을 통해 내용 전개

그림 일기 OCR 입력창
![image](https://user-images.githubusercontent.com/83449928/175809731-a24e6c4a-65ec-48c6-a534-95776f9704e2.png)
결과
![image](https://user-images.githubusercontent.com/83449928/175809852-841a54b9-047f-444a-a4b8-e80aa5de413c.png)
