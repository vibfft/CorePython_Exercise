from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)
        
threads = []
num_threads = os.cpu_count()

for i in range(num_threads):
    t = Thread(target=square_numbers)
    print(f"Add to queue => TID: {t.native_id}")
    threads.append(t)
    
for t in threads:
    print(f"Start TID: {t.native_id}")
    t.start()
    
for t in threads:
    print(f"Join TID: {t.native_id}")
    t.join()
    
print("end main")