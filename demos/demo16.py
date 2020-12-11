# import time  # 引入time模块
# ticks = time.time()
# print(ticks)  # 1607665703.6253812

# # 获取当前时间
# import time
# localtime = time.localtime(time.time())
# print("本地时间为 :", localtime) # 本地时间为 : time.struct_time(tm_year=2020, tm_mon=12, tm_mday=11, tm_hour=14, tm_min=0, tm_sec=46, tm_wday=4, tm_yday=346, tm_isdst=0)

# # 获取格式化的时间
# import time
# localtime = time.asctime(time.localtime(time.time()))
# print("本地时间为 :", localtime) # 地时间为 : Fri Dec 11 14:04:49 2020

# # 格式化日期
# import time
# # 格式化成YYYY-MM-DD HH:mm:ss形式
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ) # 2020-12-11 14:09:10

# 获取某月日历
import calendar
cal = calendar.month(2020, 12)
print(cal)

# December 2020
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31







