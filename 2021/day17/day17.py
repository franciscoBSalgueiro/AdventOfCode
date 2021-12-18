import re
with open("input.txt", "r") as file:
    target=re.search(r"x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", file.read())

target_x = (int(target.group(1)), int(target.group(2)))
target_y = (int(target.group(3)), int(target.group(4)))

if target_y[0]<target_y[1]:
    target_y = (target_y[1], target_y[0])

print(target_x)
print(target_y)

tot_max_alt = 0
total = 0
for i in range(-400,400):
    for j in range(-400,400):
        max_alt=0
        pos_x, pos_y = 0, 0
        vel_x, vel_y = i, j
        vel_ini = (vel_x, vel_y)
        while pos_y>target_y[1] or vel_y>0:
            pos_x += vel_x
            pos_y += vel_y
            if vel_x>0:
                vel_x -= 1
            if vel_x<0:
                vel_x += 1
            vel_y = vel_y-1
            max_alt = max(max_alt,pos_y)
            if target_x[0]<=pos_x<=target_x[1] and target_y[0]>=pos_y>=target_y[1]:
                total += 1
                if max_alt>tot_max_alt:
                    tot_max_alt  = max_alt
                    
                    print("Passou com velocidade inicial ",vel_ini)
                break
print(tot_max_alt)
print(total)