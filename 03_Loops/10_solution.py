import time
wait_time = 1
total_retries = 5
attempts = 0

while attempts <= total_retries:
    print("Attempts: ", attempts + 1 , "- Wait time: ",wait_time)
    attempts +=1
    time.sleep(wait_time)
    wait_time = wait_time * 2
