H, M = map(int, input().split())
C = int(input())

total_minutes = H * 60 + M + C

end_H = (total_minutes // 60) % 24
end_M = total_minutes % 60

print(end_H, end_M)