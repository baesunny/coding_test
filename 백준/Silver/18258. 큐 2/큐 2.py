import sys
from collections import deque

queue = deque()

input = sys.stdin.read
commands = input().splitlines()[1:]
result = []

for cmd in commands:
    if 'push' in cmd:
        queue.append(cmd.split()[1])
    elif cmd == 'pop':
        result.append(queue.popleft() if queue else -1)
    elif cmd == 'size':
        result.append(len(queue))
    elif cmd == 'empty':
        result.append(0 if queue else 1)
    elif cmd == 'front':
        result.append(queue[0] if queue else -1)
    elif cmd == 'back':
        result.append(queue[-1] if queue else -1)

print('\n'.join(map(str, result)))