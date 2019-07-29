# python-ui-instagram-auto

<h1 align="center">
  <br>
  <a href="http://jikao.herokuapp.com/"><img src="https://user-images.githubusercontent.com/43984584/62023622-a7700980-b20c-11e9-9e98-1a7bec09756d.png" alt="Markdownify" width="400"></a>
  <br>
  
  <br>
</h1>

<h1 align="center"> Instagram 좋아요 프로그램 
</p>

# Overview

- 파이썬의 Selenium, pyqt 모듈을 활용해서 인스타그램의 좋아요를 자동을 해주는 프로그램 입니다.

## Spec

- 언어: 파이썬(3.7)
- 모듈: Selenium, pyqt
- 크롬드라이버
  - Mac: Chrome/74.0.3729.169
  - Windows: 75
- Miniconda 설치 필요

## 사용법 - Mac

-

## 사용법 - Windows

1. miniconda 설치 합니다.

   <img src =  "https://user-images.githubusercontent.com/43984584/62024015-519c6100-b20e-11e9-82da-8a20f292913a.png">
   - https://docs.conda.io/en/latest/miniconda.html
   - Python 3.7 본인의 PC 맞는 bit를 설치한다(해당프로그램은 64bit)
    <img src = "https://user-images.githubusercontent.com/43984584/62024666-d1c3c600-b210-11e9-8bb5-3ea3a28f0286.png">

2. 환경설정

   <img src = "https://user-images.githubusercontent.com/43984584/62010278-f9c91000-b1a3-11e9-8448-1fdd470f81a7.png">

- Windows 10 기준
  1. [검색]에서 시스템(제어판)을 검색하여 선택합니다.
  2. 고급 시스템 설정 링크를 누릅니다.
  3. 환경 변수를 누릅니다. 시스템 변수 섹션에서 PATH 환경 변수를 찾아 선택합니다. 편집을 누릅니다. PATH 환경 변수가 존재하지 않을 경우 새로 만들기를 누릅니다.
  4. 시스템 변수 편집(또는 새 시스템 변수) 창에서 PATH 환경 변수의 값을 지정합니다. 확인을 누릅니다. 확인을 눌러 나머지 창을 모두 닫습니다.
- 환경 설정 및 설치확인 방법: 윈도우키 > cmd > `python --version` 입력 > 3.7을 확인 합니다.

3. pyqt 설치

   - 윈도우키 > cmd > `pip install pyqt5-sip` > 엔터 > `pip install pyqt5` 엔터

4. 아래의 URL을 접속 > `disk.zip` 다운로드 > 압축을 풀고 `app.py` 파일을 실행 시킵니다.
   - https://github.com/jihyunjeongme/python-ui-instagram-auto_win/tree/master/dist

## 기타 문의

- 블로그 : https://stophyun.tistory.com/
- 이메일: stophyuni@gmail.com
- Github: jihyunjeong.me@gmail.com
- 궁금한 사항은 이메일로 부담없이 보내주세요.
