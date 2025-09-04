import sys
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    A, B = map(int, input().split())
    results.append(A + B)

print('\n'.join(map(str, results)))