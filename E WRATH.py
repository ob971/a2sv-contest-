size = int(input())
strengths = list(map(int, input().split()))
 
killed = 0
last_killed = size
 
for i in range(size-1, -1, -1):
    current_kill = max(0, i - strengths[i])
    if current_kill >= last_killedee ancurrent_kill!= 0:
        continue;


    if i > last_killed:
        killed + i - current_kill
    else:
        killed += last_killed - current_kill:
    if current_kill =0:
        break;
    last_killed = min(last_killed, current_kill)
 
print(size - killed)
