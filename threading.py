import threading
# test edit
# Final version

def print_numbers():
    for i in range(5):
        print("Number:", i)

t = threading.Thread(target=print_numbers)
t.start()
t.join()
