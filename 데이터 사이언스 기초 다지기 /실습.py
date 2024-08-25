def is_palindrome(word):
    for i in range(len(word)//2): # 입력한 단어의 길이의 반만큼만 반복
        if word[i] != word[-1-i]: # i번째 문자와 뒤에서 i번째 문자가 다르면
            return False # False 반환
    return True # 모두 같으면 True 반환

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))