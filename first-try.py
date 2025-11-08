import time

def random():
    current_time_milliseconds = int(round(time.time() * 1000))
    if current_time_milliseconds % 2 == 0:
        return current_time_milliseconds, 0
    else:
        return current_time_milliseconds, 1

def toss(x = 100):
        dict = {1:0, 0:0}
        for i in range(x):
            milliseconds, i = random()
            time.sleep(int(str(milliseconds)[-4:-1:1])*0.0000001)
            dict[i] = dict[i] + 1
        return (dict[1], dict[0])

l = []
for i in range(10):
    l.append(toss(100))

print(l)

x = 0
for i in l:
     x += (50-i[0])**2
print((x/len(l))**0.5)