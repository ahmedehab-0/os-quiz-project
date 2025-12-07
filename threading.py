import threading

def print_numbers():
    for i in range(5):
        print("Number:", i)

t = threading.Thread(target=print_numbers)
t.start()
t.join()
