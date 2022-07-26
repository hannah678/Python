#파이썬 터틀 모듈 가져오기
import turtle

# 그림을 그리기 위해서 캔버스(그리는 공간)을 불러온다.
t = turtle.Pen()

# 캔버스의 마우스 형태를 거북이 모향으로 바꾼다. 
t.shape("turtle")

# 펜의 색상을 파란색으로 설정
t.pencolor("blue")

#해당 방향으로 픽셀만큼 선 그리기
t.forward(100)

#거북이 방향바꾸기
t.right(90)
t.forward(100)

t.right(90)
t.forward(100)

t.right(90)
t.forward(100)