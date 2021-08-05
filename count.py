import os
import sys

def sortFiles(path):
    nums = os.listdir(path)
    nums.sort()
    return nums

root = "2021"
problem_nums = sortFiles(root)

print("================ Finished ================")
for d in problem_nums:
    date_nums = sortFiles(os.path.join(root, d))
    if len(date_nums) >= 5:
        print("{:<27s} - {}".format(d, date_nums))

print("\n========== Next Month (Weekend) ==========")
for d in problem_nums:
    date_nums = sortFiles(os.path.join(root, d))
    if len(date_nums) == 4:
        print("{:<27s} - {}".format(d, date_nums))

print("\n========== Next Week (Weekend) ===========")
for d in problem_nums:
    date_nums = sortFiles(os.path.join(root, d))
    if len(date_nums) == 3:
        print("{:<27s} - {}".format(d, date_nums))

print("\n========== This Week (Workdays) ==========")
for d in problem_nums:
    date_nums = sortFiles(os.path.join(root, d))
    if len(date_nums) < 3:
        print("{:<27s} - {}".format(d, date_nums))

print("\n共完成%d道题" % len(problem_nums))


