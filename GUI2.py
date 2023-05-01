from tkinter import *
from PIL import ImageTk
import PIL.Image


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# frame class

# 시작 화면
class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.option_add('*Font','NanumGothic 11')
        Label(self, text="[ 버튼을 누르면 분석 결과로 이동합니다 ]",
              font=('NanumGothic', 16, "bold")).pack(side="top", fill="x", pady=8)
        
        # 위치 조정용 라벨
        Label(self).pack(side='top', pady=20)
        
        L1 = Label(self)
        L2 = Label(self)
        L1.pack(side='top')
        L2.pack(side='bottom')
        
        # 버튼 생성
        b1 = Button(L1, text="    사고 유형 분석    ",
                  command=lambda: master.switch_frame(page1))
        b2 = Button(L1, text=" 사고 도로 위치 분석  ",
                  command=lambda: master.switch_frame(page2))
        b3 = Button(L1, text="   사고 시간대 분석   ",
                  command=lambda: master.switch_frame(page3))
        b4 = Button(L2, text="    위반 법규 분석    ",
                  command=lambda: master.switch_frame(page4))
        b5 = Button(L2, text=" 지역별 사고비율 분석 ",
                  command=lambda: master.switch_frame(page5))
        
        # 버튼 위치 지정
        b1.pack(side='left', padx=30, pady=50)
        b2.pack(side='left', padx=30, pady=50)
        b3.pack(side='left', padx=30, pady=50)
        b4.pack(side='left', padx=30, pady=50)
        b5.pack(side='right', padx=30, pady=50)


# 분석 1
class page1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # 위젯 생성
        Label(self, text="PM 사고 유형 분석",
              font=('NanumGothic', 16, "bold")).pack(side="top", fill="x", pady=8)
        b_back = Button(self, text="  뒤로 가기  ",
                  command=lambda: master.switch_frame(StartPage))
        
        
        self.img1 = ImageTk.PhotoImage(PIL.Image.open("1.png"))
        lb1 = Label(self, image=self.img1, background='white')
        
        # 위젯 배치
        lb1.pack(side='left', padx=5, pady=5)
        
        
        b_back.pack(side='right', padx=10, pady=10)



# 분석 2
class page2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # 위젯 생성
        Label(self, text="PM 사고 도로 위치 분석",
              font=('NanumGothic', 16, "bold")).pack(side="top", fill="x", pady=8)
        b_back = Button(self, text=" 뒤로 가기 ",
                  command=lambda: master.switch_frame(StartPage))
        
        
        self.img2 = ImageTk.PhotoImage(PIL.Image.open("2.png"))
        lb2 = Label(self, image=self.img2, background='white')
        
        # 위젯 배치
        lb2.pack(side='left', padx=5, pady=5)
        
        
        b_back.pack(side='right', padx=10, pady=10)

# 분석 3
class page3(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # 위젯 생성
        Label(self, text="PM 사고 시간대별 분석",
              font=('NanumGothic', 16, "bold")).pack(side="top", fill="x", pady=8)
        b_back = Button(self, text=" 뒤로 가기 ",
                  command=lambda: master.switch_frame(StartPage))
        
        
        self.img3 = ImageTk.PhotoImage(PIL.Image.open("3.png"))
        lb3 = Label(self, image=self.img3, background='white')
        
        # 위젯 배치
        lb3.pack(side='left', padx=5, pady=5)
        
        
        b_back.pack(side='right', padx=10, pady=10)
        
# 분석 4
class page4(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # 위젯 생성
        Label(self, text="PM 사고 법규위반별 분석",
              font=('NanumGothic', 16, "bold")).pack(side="top", fill="x", pady=8)
        b_back = Button(self, text=" 뒤로 가기 ",
                  command=lambda: master.switch_frame(StartPage))
        
       
        self.img4 = ImageTk.PhotoImage(PIL.Image.open("4.png"))
        lb4 = Label(self, image=self.img4, background='white')
        
        # 위젯 배치
        lb4.pack(side='left', padx=5, pady=5)
        b_back.pack(side='right', padx=10, pady=10)

# 분석 5
class page5(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # 위젯 생성
        Label(self, text="지역별 PM 사고 비율",
              font=('NanumGothic', 16, "bold")).pack(side="top", fill="x", pady=8)
        b_back = Button(self, text=" 뒤로 가기 ",
                  command=lambda: master.switch_frame(StartPage))
        
        
        self.img5 = ImageTk.PhotoImage(PIL.Image.open("5.png"))
        lb5 = Label(self, image=self.img5, background='white')

        # 위젯 배치
        lb5.pack(side='left', padx=5, pady=5)
        b_back.pack(side='right', padx=10, pady=10)
        

# main
if __name__ == "__main__":
    app = SampleApp()
    app.title("PM Accident Analyzer")
    app.geometry('1000x600')
    
    app.mainloop()
