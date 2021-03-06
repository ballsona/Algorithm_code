# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

import sys
n = int(input())

data = [None] * n
stack = []
result = []
count = 1
for i in range(n):
    data[i]= int(sys.stdin.readline())
    #stack값이 count값과 같을때까지.
    while count <= data[i] :
        stack.append(count)
        count +=1
        result.append('+')
    if stack[-1] == data[i]:
        stack.pop()
        result.append('-')
    else :
        print("NO")
        exit(0)
print('\n'.join(result))