import threading
import time

def io_bound_task(name, delay):
    print(f"Task {name} starting...")
    time.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")

# Using threads
threads = []
start_time = time.time()

for i in range(5):
    thread = threading.Thread(target=io_bound_task, args=(f"Thread-{i+1}", 5))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"Total time taken with threads: {end_time - start_time:.2f} seconds")

start_time = time.time()

print("\n")
print("----------------------------")
print("\n")

for i in range(5):
    io_bound_task(f"Sequential-{i+1}", 5)

end_time = time.time()

print(f"Total time taken without threads: {end_time - start_time:.2f} seconds")
