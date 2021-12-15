with open("input.txt", "r") as file:
    linhas=file.readlines()

# Part 1

horizontal = 0
vertical = 0

for i, l in enumerate (linhas):
    if "forward" in l:
        horizontal+= int(l.replace("forward",""))
    if "down" in l:
        vertical+= int(l.replace("down",""))
    if "up" in l:
        vertical-= int(l.replace("up",""))
        
print(horizontal*vertical)

# Part 2

horizontal = 0
vertical = 0
aim = 0

for i, l in enumerate (linhas):
    if "forward" in l:
        vertical+= int(l.replace("forward",""))
        horizontal+= int(l.replace("forward",""))*aim
    if "down" in l:
        aim+=int(l.replace("down",""))
    if "up" in l:
        aim-=int(l.replace("up",""))

print(horizontal*vertical)