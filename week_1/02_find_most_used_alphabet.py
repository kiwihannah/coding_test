def find_max_occurred_alphabet(string):
    alpha_arr = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        idx_arr = ord(char.upper()) - ord("A")
        alpha_arr[idx_arr] += 1

    for abc in alpha_arr:
        most_used_idx = 0;
        if most_used_idx < abc:
            most_used_idx = abc

        return chr(alpha_arr[most_used_idx]+65)

    return alpha_arr


print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet("best of best sparta"))
