import threading
import time

sem = threading.Semaphore(2)

def worker(name):
    sem.acquire()
    print(f"{name} entered critical section")
    time.sleep(1)
    sem.release()
    print(f"{name} exited critical section")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(f"Worker {i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
