import random
import time


class RandDT(object):
    def __init__(self, start='2018-09-15 07:00:00', end=time.strftime('%Y-%m-%d %H:%M:%S'),
                 limit=lambda x: 0 <= x <= 7):
        self.start = start
        self.end = end
        self.limit = limit

    def get_rand_datetime(self, count=1):
        start_sec = time.mktime(time.strptime(self.start, '%Y-%m-%d %H:%M:%S'))
        end_sec = time.mktime(time.strptime(self.end, '%Y-%m-%d %H:%M:%S'))
        i = 0
        while i < count:
            secs = random.randrange(start_sec, end_sec)
            tm = time.gmtime(secs)
            if self.limit(tm.tm_hour):
                # 在限制时段内，过滤掉
                continue
            else:
                # 在预定时间内，计数加一，返回当前时段
                i += 1
                yield '%d-%02d-%02d %02d:%02d:%02d' % (
                    tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)

    def get_sorted_rand_datetime(self, count=10):
        datetimes = list(self.get_rand_datetime(count))
        return sorted(datetimes)


if __name__ == '__main__':
    rdt = RandDT()
    for i in rdt.get_sorted_rand_datetime(7):
        print(i)
