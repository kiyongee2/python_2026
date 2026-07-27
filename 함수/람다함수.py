
# 람다 함수
# 람다 함수는 익명함수라고도 불리는 함수입니다.
# 람다 함수는 def 키워드로 함수를 정의하는 대신, lambda 키워드를 사용하여 함수를 정의합니다.
# 람다 함수는 일반적으로 한 줄로 작성되며, 간단한 연산이나 함수를 표현하는 데 사용됩니다.  

# 람다 함수의 기본 문법은 다음과 같습니다.
# lambda 매개변수: 표현식
# 람다 함수는 일반적으로 함수를 인자로 전달하거나, 간단한 연산을 수행하는 데 사용됩니다.
# 람다 함수의 예제
# 두 수의 합을 구하는 람다 함수
add = lambda x, y: x + y
result = add(3, 5)
print(result) # 8

# map() 함수와 람다 함수를 함께 사용하여 리스트의 각 요소에 2를 곱하는 예제
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) # [2, 4, 6, 8, 10]

# filter() 함수와 람다 함수를 함께 사용하여 리스트에서 짝수만 필터링하는 예제
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6]