# Reference
# https://wikidocs.net/book/2165
# https://wikidocs.net/35492
# 쿠키 관련 로직 추가 할것: https://testmanager.tistory.com/163

import sys,os
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import time
import datetime
import random
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
 
        self.btn1 = QPushButton("&Like", self)

        self.lbl1 = QLabel("ID", self)
        self.lbl1.move(30, 40)

        self.lbl2 = QLabel("PW", self)
        self.lbl2.move(30, 70)

        self.lbl3 = QLabel("Tag1", self)
        self.lbl3.move(30, 100)

        self.lbl4 = QLabel("Tag2", self)
        self.lbl4.move(30, 130)

        self.lbl5 = QLabel("Tag3", self)
        self.lbl5.move(30, 160)

        self.lbl6 = QLabel("UserName", self)
        self.lbl6.move(30, 190)

        self.lbl7 = QLabel("LikeCount", self)
        self.lbl7.move(30, 220)

        # self.lbl8 = QLabel("TimelinLike", self)
        # self.lbl8.move(30, 250)

        self.qle1 = QLineEdit(self)
        self.qle1.move(100, 40)

        self.qle2 = QLineEdit(self)
        self.qle2.setEchoMode(QLineEdit.Password)

        self.qle2.move(100, 70)

        self.qle3 = QLineEdit(self)
        self.qle3.move(100, 100)

        self.qle4 = QLineEdit(self)
        self.qle4.move(100, 130)

        self.qle5 = QLineEdit(self)
        self.qle5.move(100, 160)

        self.qle6 = QLineEdit(self)
        self.qle6.move(100, 190)

        self.qle7 = QLineEdit(self)
        self.qle7.move(100, 220)

        # self.qle8 = QLineEdit(self)
        # self.qle8.move(100, 250)

        self.setWindowTitle("Instagram Auto Program")
        # x, y, width, height
        self.setGeometry(800, 400, 300, 260)
        self.show()

        # 버튼에 기능을 할당하는 코드
        self.btn1.clicked.connect(self.printTextEdit)
        # self.initUI()

    def printTextEdit(self):
        self.instagramStart()

    def instagramStart(self):
        # ======== 1. Setting Options =======
        self.options = webdriver.ChromeOptions()

        # Chrome을 안 띄우고 수행하고 싶으면 아래 주석을 해제(리눅스 서버에서 작업시 headless 추천, 디버깅시는 headless 주석처리)
        # options.add_argument("headless")

        # Chrome 설정 : 진짜 유저가 작업하는 것처럼 보이도록 설정
        self.options.add_argument("window-size=1920x1080")
        self.options.add_argument("disable-gpu")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
        )
        self.options.add_argument("lang=ko_KR")

        # ======= 2. Setting id, password, hashtag ======

        id = self.qle1.text()
        password = self.qle2.text()
       

        important_hash_tags = [self.qle3.text(), self.qle4.text(), self.qle5.text()]
        important_hash_tags_count = int(self.qle7.text())
        # important_hash_tags_count = 116

        # timeline_like_count = int(self.qle8.text())

        hash_tags = [self.qle3.text(), self.qle4.text(), self.qle5.text()]
        hash_tags_count = 500

        # ======== 3. InstaJob Class ======
        print("browser loading..")
        global browser
        browser = webdriver.Chrome(
            # "/Users/jihyun/Documents/GitHub/instagram-auto-like-with-Python/chromedriver_74",
            "/Users" + "/" + self.qle6.text() + "/Downloads/Instagram_auto/chromedriver_76",
            # "/Users/jihyun/Downloads/Instagram_auto/chromedriver_74",
            # os.getcwd() + "/chromedriver_74",
            # sys.path[1] + "/chromedriver_74",
            options=self.options,
        )

        
        ## 주석 처리
        browser.execute_script(
            "Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})"
        )
        browser.execute_script(
            "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})"
        )
        browser.execute_script(
            "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = \
            function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) \
            {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};"
        )

        # 쿠키 로직 추가 (2019.09.16)
        browser.get("https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?utm_source=chrome-ntp-icon")
        time.sleep(60)

        browser.get("https://instagram.com/")
        # pickle.dump(browser.get_cookies(), open("cookies.pkl","wb"))

        time.sleep(3.5)

        ######## 임시 주석
        # # 로그인
        # login_link = browser.find_element_by_css_selector(
        #     "p.izU2O"
        # ).find_element_by_css_selector("a")
        # login_link.click()
        # time.sleep(3.5)

        # username_input = browser.find_elements_by_css_selector("input._2hvTZ")[0]
        # username_input.send_keys(id)
        # time.sleep(2 + random.random() * 0.3)
        # password_input = browser.find_elements_by_css_selector("input._2hvTZ")[1]
        # password_input.send_keys(password)
        # time.sleep(1)
        # password_input.submit()
        # time.sleep(60)
        
        ### 임시 주석
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            for i in range(timeline_like_count):
                time.sleep(1.5)

                browser.find_elements_by_css_selector(
                    "span.fr66n > button > span"
                    # "span.glyphsSpriteHeart__outline__24__grey_9.Szr5J"
                )[0].click()

                time.sleep(1.5)

        except Exception as e:
            print("Error! ", e)
            # slacker.chat.post_message("#general", text="raise timeline like error")
            pass

        for hash_tag in hash_tags:
            try:
                print(hash_tag + " 좋아요 작업을 시작합니다")
                browser.get("https://www.instagram.com/explore/tags/" + quote(hash_tag))
                time.sleep(5 + random.random() * 1.2)
                element = browser.find_elements_by_css_selector("div._9AhH0")[9]
                element.click()
                time.sleep(5 + random.random() * 1.2)

                if any(e in hash_tag for e in important_hash_tags):
                    count_number = important_hash_tags_count
                else:
                    count_number = hash_tags_count

                for i in range(1, count_number):
                    print(i,"/",count_number)
                    # print(count_number)
                    try:
                        # 좋아요 해쉬태그 지정
                        like = browser.find_element_by_css_selector(
                            "span.fr66n > button > span"
                            # "span.glyphsSpriteHeart__outline__24__grey_9.Szr5J"
                        )
                        # 좋아요 해쉬태그 클릭
                        like.click()

                        # 다음 포스팅으로 넘어가기전 대기
                        time.sleep(4.5 + random.random() * 1.2)

                        # 다음 포스팅으로 넘어감
                        browser.find_element_by_css_selector(
                            "span.glyphsSpriteHeart__outline__24__grey_9.Szr5J"
                        ).click()

                        time.sleep(4.5 + random.random() * 1.3)
                    except:
                        browser.find_element_by_css_selector(
                            "a.HBoOv.coreSpriteRightPaginationArrow"
                        ).click()
                        time.sleep(4 + random.random() * 1.2)

            except NoSuchElementException as e:
                print("NoSuch Error", e)
                pass

            except Exception as e:
                print("Error! ", e)

            # 로직 다돌 고 나오는 것 추가 할것

        browser.quit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
