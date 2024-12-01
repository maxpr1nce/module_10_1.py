import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)  # Пауза в 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Вызов функции 4 раза
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

# Функция для многопоточной записи
def threaded_write_words(word_count, file_name):
    write_words(word_count, file_name)

# Измерение времени выполнения
start_time = time.time()

# Создание потоков
threads = []
threads.append(threading.Thread(target=threaded_write_words, args=(10, "example5.txt")))
threads.append(threading.Thread(target=threaded_write_words, args=(30, "example6.txt")))
threads.append(threading.Thread(target=threaded_write_words, args=(200, "example7.txt")))
threads.append(threading.Thread(target=threaded_write_words, args=(100, "example8.txt")))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения потоков
for thread in threads:
    thread.join()

# Измерение завершения времени выполнения
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.2f} секунд")