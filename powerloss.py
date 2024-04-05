import sys
import pathlib

nums = []
gcodes = pathlib.Path('/home/pi/printer_data/gcodes/')

with open(gcodes / sys.argv[2]) as gfile:
    ulines = []
    gcode = ''
    i = 0
    for line in gfile.readlines():
        ulines.append(line)
        if line.startswith(f';Z:{sys.argv[1]}'):
            nums.append(i)
        i += 1

num = nums[0]
preserve_line = 0
for uline in ulines:
    if 'POWER_PANIC_PRESERVE' in uline:
        break
    preserve_line += 1
if preserve_line >= len(ulines) - 1:
    preserve_line = 200

print(preserve_line, len(ulines), nums, num)
final = '\n'.join(ulines[0:preserve_line]) + '\n'.join(ulines[num:])
with open(gcodes / ('RECOVER-SOFT-'+str(sys.argv[2])), 'w') as file:
    file.write(final)
