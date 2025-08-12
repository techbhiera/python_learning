import time


wait_time =1
max_retries=5
count=0

while count<max_retries:
    print("count",count + 1,"wait time" ,wait_time)
    time.sleep(wait_time)
    wait_time*=2
    count+=1