import multiprocessing

# процессы могут выполняться на разных ядрах компьютера (4)
# каждый процесс боролся за ресурсы

counter = multiprocessing.Value('i', 0) # 'i' целое число  0 - начальное значение многопроцессорная переменная целого типа


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock(): #на время операции прибавления блокируем значение переменной в текущем виде
            cnt.value += 1
    print(f"Значение счетчика: {cnt.value:_}")


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter, ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Значение счетчика в финале: {counter.value:_}")