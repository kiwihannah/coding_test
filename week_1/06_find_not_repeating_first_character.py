def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char # 현재 들어온 문자열 순서에 맞게 반환할 수 있음

    return "_"


print("정답 = d 현재 풀이 값 =", find_not_repeating_first_character("abadabac"))
print("정답 = c 현재 풀이 값 =", find_not_repeating_first_character("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", find_not_repeating_first_character("aaaaaaaa"))
