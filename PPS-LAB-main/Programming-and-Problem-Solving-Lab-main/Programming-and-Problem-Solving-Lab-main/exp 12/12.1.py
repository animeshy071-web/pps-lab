n = int(input())
Ph = {}

for i in range(n):
    cmd = input().split()
    
    if cmd[0] == "ADD":
        Ph[cmd[1]] = cmd[2]
        
    elif cmd[0] == "REMOVE":
        Ph.pop(cmd[1], None)
        
    elif cmd[0] == "DISPLAY":
        if len(Ph) == 0:
            print("No contacts")
        else:
            for name in sorted(Ph):
                print(f"{name}: {Ph[name]}")