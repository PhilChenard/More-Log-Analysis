file_path = 'assignment_3.py'

fileDict = {}
fileDict2 = {}

print('FILE A -->  ')
file1 = open('Log-A.strace')
lines = file1.readlines()

count = 0
term = ' clone('
line_number = "Error"

stat_pid = None
stat_line_num = None
stat_line = None

line_num = 1

for line in lines:
		if 'stat(' in line:
			stat_line_num = line_num
			idx = line.find(' ')
			stat_pid = line[0:idx]
			stat_line = line

		elif 'clone(' in line:
			clone_line_num = line_num 
			idx = line.find(' ')
			clone_pid = line[0:idx]

			clone_line = line

			if clone_pid == stat_pid:
				print(str(stat_line_num) + '\t' + stat_line)
				print(str(clone_line_num) + '\t' + clone_line)

				stat_pid = None
				stat_line_num = None
				stat_line = None

		line_num += 1


print(' FILE B -->  ')
file2 = open('Log-B.strace')
lines2 = file2.readlines()

term = 'clone('

stat_pid2 = None
stat_line_num2 = None
stat_line2 = None

count2 = 0
line_number = "Error"

line_num2 = 1


for line in lines2:
	if 'stat(' in line:
		stat_line_num2 = line_num2
		idx = line.find(' ')
		stat_pid2 = line[0:idx]
		stat_line2 = line

	elif 'clone(' in line:
		clone_line_num2 = line_num2
		idx = line.find(' ')
		clone_pid2 = line[0:idx]
		clone_line2 = line

		if clone_pid2 == stat_pid2:
			print(str(stat_line_num2) + '\t' + stat_line2)
			print(str(clone_line_num2) + '\t' + clone_line2)

			stat_pid2 = None
			stat_line_num2 = None
			stat_line2 = None

	line_num2 += 1

print('Output C ')
file3 = open('Log-B.strace')
lines3 = file3.readlines()

line_num = 0


kw_found = [True, True, True]
pids = [16959, 16959, 16959]
line_nums = [583, 586, 587]
line_strs = ['16959 open("." ... ommitted', '16959 getdents(3</home/user/test> ... ommitted', '16959 close(3</home/user/test>)']

for line in lines:
	line_num += 1

	if 'open(' in line:
		kw_found = True
		idx = line.find(' ')
		pids[0] = line[0:idx]

		line_nums[0] = line_num
		line_strs[0] = line


	elif 'getdents(' in line:
		if kw_found[0]:
			idx = line.find(' ')
			pid = line[0:idx]

			if pid == pids[0]:
				kw_found[1] = True
				pids[1] = pid
				line_nums[1] = line_num
				line_strs[1] = line


	elif 'close(' in line:
		if kw_found[0] and kw_found[1]:
			pid = pid_from_line(line)
			if pid == pids[0] and pid == pids[1]:
				kw_found[2] = True
				pids[2] = pid
				line_nums[2] = line_num
				line_strs[2] = line

				print(line_num, line)
	if kw_found[0] and kw_found[1] and kw_found[2]:
		print(kw_found)
		pass





		


