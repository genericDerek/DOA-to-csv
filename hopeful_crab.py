### Testing idea
import sys


name = "real_35min_trial1"
path = "/Users/Guest/Downloads/"



input = path+name+".txt"
with open(input) as infile:
    raw_data = infile.readlines()
print raw_data[0]
is_down = False
flick_time = 0
press = 19
event_code = 32
flick_code = 75
time_elapsed = 0
num_flicks = 0
flick_list = []
events = []


for line in raw_data:
    line = line.strip()
    parts = line.split(' ')
    #print parts[0]
    if parts[0] == 'KeyDown':
        #print 'Keydown'
        is_down = True
        if int(parts[1]) == event_code:
            events.append([time_elapsed, num_flicks])
            time_elapsed += press
        elif int(parts[1]) == flick_code:
            num_flicks += 1
            flick_list.append([num_flicks, time_elapsed, flick_time])
            time_elapsed += flick_time
            flick_time = press
        else:
            print "Houston, we have a problem  ",
            print str(parts[1])
            flick_time += press
    elif parts[0] == 'KeyUp':
        is_down = False
    elif parts[0] == 'Pause':
        if is_down == False:
            flick_time += int(parts[1])

interval = 1000
running = 0
flicks = 0
per_unit_time = []
for line in flick_list:
    running += int(line[2])
    while running >= interval:
        print str(running)
        running = running - interval
        per_unit_time.append(flicks)
        flicks = 0
    flicks += 1

e_destin = path + name + '_events.txt'
with open(e_destin,"w") as efile:
    efile.write("Time_elapsed,Flick_number,\n")
    for piece in events:
        for p in piece:
            p = str(p)
            efile.write(p)
            efile.write(',')
        efile.write('\n')
    efile.write('\nFlicks per '+str(interval/100)+'s\n')
    for inter in per_unit_time:
        efile.write(str(inter)+'\n')
    #print piece
o_destin = path + name + '_flicks.txt'
with open(o_destin,'w') as ofile:
    ofile.write("Number,Time_elapsed,Flick_duration,\n")
    for bit in flick_list:
        #print bit
        for b in bit:
            b = str(b)
            #print b
            ofile.write(b)
            ofile.write(',')
        ofile.write('\n')
print 'Does this work?'


print per_unit_time
sys.exit()

