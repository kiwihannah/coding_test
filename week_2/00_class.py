# 비슷하거나 동일한 개념의 자료를 다룰 때 클래스를 활용해보자
class Person:
    def __init__(self, param_name):
        print("hihihi", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")


person_1 = Person("유재석")
print(person_1.name)  # 유재석
person_1.talk()  # 안녕하세요 저는 유재석 입니다

person_2 = Person("박명수")
print(person_2.name)  # 박명수
person_2.talk()  # 안녕하세요 저는 박명수 입니다