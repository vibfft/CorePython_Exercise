import multiprocessing as m
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)
        
processes = []
num_processes = os.cpu_count()

for i in range(num_processes):
    p = m.Process(target=square_numbers)
    print(f"Add to queue => PID: {p.pid}")
    processes.append(p)
    
for p in processes:
    print(f"Start PID: {p.pid}")
    p.start()
    
for p in processes:
    print(f"Join PID: {p.pid}")
    p.join()
    
print("end main")