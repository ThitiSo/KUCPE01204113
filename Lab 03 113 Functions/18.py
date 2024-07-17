def read_hour():
    return  int(input("Enter hour: "))
def read_minute():
    return int(input("Enter minute: "))
def read_second():
    return int(input("Enter second: "))
def to_seconds(h,m,s):
    return h*3600+m*60+s
def time_elapsed(start_time, finish_time):
    remain=finish_time-start_time
    hours=remain//3600
    minute= (remain-hours*3600)//60
    second= remain%60
    return f"{hours} hours {minute} minutes {second} seconds."