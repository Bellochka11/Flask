import threading


counter = 0

# борьба за ресурсы потоки считают каунт 

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f"Значение счетчика: {counter:_}")


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join() # ждем пока очередной поток завершится

print(f"Значение счетчика в финале: {counter:_}")