import threading

ucounter = 0
counter = 0

def unsafer():
    global ucounter
    for _ in range(1000):
        ucounter += 1

lock = threading.Lock()

def safer():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

uthreads = []
for _ in range(100):
    t = threading.Thread(target = unsafer)
    uthreads.append(t)
    t.start()

for t in uthreads:
    t.join()

print("Unsafe counter:", ucounter)

sthread = []
for _ in range(100):
    t = threading.Thread(target = safer)
    sthread.append(t)
    t.start()

for t in sthread:
    t.join()

print("Safer Counter:", counter)