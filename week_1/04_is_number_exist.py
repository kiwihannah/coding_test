# 점근 표기법: 알고리즘의 효율성을 평가하는 방법

def is_number_exist(number, array):
    for num in array:
        if number == num:
            return True
    return False


print("정답 = True 현재 풀이 값 =", is_number_exist(3,[3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", is_number_exist(7,[6,6,6]))
print("정답 = True 현재 풀이 값 =", is_number_exist(2,[6,9,2,7,1888]))