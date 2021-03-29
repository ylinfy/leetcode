import os
import sys
import time
import random
import calendar


year_dir = "2021"
level_dirs = [os.path.join(year_dir, x) for x in os.listdir(year_dir)]
# print(level_dirs)
problem_dirs = [os.path.join(x, p) for x in level_dirs for p in os.listdir(x)]
# print(problem_dirs)
print("共完成了%d题" % len(problem_dirs))
print("0308还剩余：217000")

names = []
names4 = []
done = []
jz_done = []

for p in problem_dirs:
    # 记录做过的所有题
    p_name = p.split('/')[-1]
    if 'jz' in p_name: jz_done.append(int(p_name[2:6]))
    else: done.append(int(p_name))

    # 记录未完成四遍的题
    t_name = os.listdir(p)
    if len(t_name) >= 5: continue
    if len(t_name) == 4:
        names4.append([p, t_name])
    else:
        names.append([p, t_name])

# 排序names,以names的第二维进行排序
times = sorted(names, key=lambda x:x[1])
times4 = sorted(names4, key=lambda x:x[1])
print("\n上月附近三天题目：")
day = time.localtime()[2]
threedays = [(day + x) or 31 for x in [-1, 0, 1]]
cur_days = [(2 - len(str(x))) * '0' + str(x) for x in threedays]
# print(cur_days)

# 上个月份
mon = time.localtime()[1] - 1 or 12
last_mon = (2 - len(str(mon))) * '0' + str(mon) 
last_mon_three_days = [last_mon + cday for cday in cur_days]
# print(last_mon_three_days)

# 求上个月同一天
for p, n in times4:
    if n[-1][:4] in last_mon_three_days:
        print("{0:<22s}{1}".format(p, n))

print("上周待完善题目详情：")
for p, n in times:
    if len(n) < 3: continue
    print("{0:<22s}{1}".format(p, n))

print("\n今天复习题目详情：")
for p, n in times:
    if len(n) > 2: continue
    print("{0:<22s}{1}".format(p, n))

