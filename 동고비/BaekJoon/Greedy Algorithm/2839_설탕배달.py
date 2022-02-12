N = int(input())
answer = 0

while N >= 0:
  if N % 5 == 0:
    answer += N // 5
    print(answer)
    break
  elif N < 3:
    print(-1)
    break

  N -= 3
  answer += 1
