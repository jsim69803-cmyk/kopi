kakao = ["가나", "다라", "마바", "사아 ", "자차"]
temp = kakao[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
print(kakao)
kakao[3]= kakao[4]
kakao[4] = temp
print(kakao)