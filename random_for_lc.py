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
print("待完善题目详情：")

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
for p, n in times:
    print("{0:<20s}{1}".format(p, n))


# 抽取题号(待优化, 可能投到已经做过的)
print("\n正在进行剑指offer系列...")
choices = []
for i in range(69):
    if i < 4 or i in [15]: continue
    if i not in jz_done:
        choices.append(i)
print("还剩余题号：", choices)
print("还剩余题数量：", len(choices))
print("今天抽中的题号：剑指%d" % random.choice(choices))

# 统计
# print(calendar.monthcalendar(2021,3))

