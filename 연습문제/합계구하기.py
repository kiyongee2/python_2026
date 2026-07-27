
n = int(input("정수를 입력하세요: "))

total = 0
for i in range(1, n + 1):
    print(i, end=" ")
    total += i
print(f"\n1부터 {n}까지의 합은 {total}입니다.")