var num = 1;
var filelist = ["이야기1","이야기2","이야기3","이야기4","이야기5","이야기6","이야기7","이야기8"]

function changePic(idx) { ///idx라는 매개변수를 사용한 changePic 이름의 함수 생성
  if (idx) {
    if (num>=8) return; //num이 maxnum일때 num++ 이전에 강제종료 
    num++; //다음 버튼을 누르면 idx값이 1이 되어 num의 값이 1만큼 증가
  } else {
    if (num <= 1) return; //num이 0일때 num-- 이전에 강제종료
    num--; //이전 버튼을 누르면 idx값이 0이 되어 num의 값이 1만큼 감소
  }
  var imgTag = document.getElementById("photo");
  var file_url = "../static/story_img/"+ num + ".png" ;
  imgTag.setAttribute("src", file_url ); //id값이 photo인 이미지태그 선택 후,//src 속성값을 수정 
  document.getElementById("story").textContent= filelist[num-1];     //id값이 imgname인 값 선택 후, 내용 수정      
}
