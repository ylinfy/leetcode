import os
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
done = []
jz_done = []

for p in problem_dirs:
    # 记录做过的所有题
    p_name = p.split('/')[-1]
    if 'jz' in p_name: jz_done.append(int(p_name[2:6]))
    else: done.append(int(p_name))

    # 记录未完成四遍的题
    t_name = os.listdir(p)
    if len(t_name) >= 4: continue
    names.append([p, t_name])

times = sorted(names, key=lambda x:x[1])
print("\n待完善题目详情：")
for p, n in times:
    if len(n) < 3: continue
    print("{0:<22s}{1}".format(p, n))

print("\n今天复习题目详情：")
for p, n in times:
    if len(n) > 2: continue
    print("{0:<22s}{1}".format(p, n))

