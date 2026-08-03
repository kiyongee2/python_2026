
terms = {
  "CPU": "중앙처리장치", 
  "RAM": "주기억장치"
}

while True:
  word = input("검색할 용어: ")
  # print(terms.get(word, "정의된 단어가 없습니다."))
  if word == "종료":
    print("프로그램을 종료합니다.")
    break
  elif word in terms:
    print(terms.get(word))
  else:
    print("정의된 단어가 없습니다.")
