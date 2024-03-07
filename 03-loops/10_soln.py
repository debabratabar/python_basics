import time
no_of_retry = 0
max_retry=5
wait_time=1

while no_of_retry < max_retry:
    print(f"Retry {no_of_retry+1} | Wait time {wait_time}")
    time.sleep(wait_time)
    wait_time*=2
    no_of_retry+=1

print("END OF EXPONENTIAL BACKOFF STREATEGY")