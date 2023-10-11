# 반복문
def fib_loop(n):
    result = [1, 1]

    for i in range(1, n):
        end1 = result[-1]
        end2 = result[-2]

        fib_num = end1 + end2

        result.append(fib_num)
    return  result[-1]



# 재귀
# 어떨 때는 이게 더 직관적일 수 있다.
def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

