import time
from threading import Thread


def addition_operator(work_id, start, end, result):
    print(f'work id : {work_id}')
    total = 0
    for i in range(start, end):
        total += i
        result.append(total)
    return


result_list = list()
thread1 = Thread(target=addition_operator, args=(1, 0, 100000000, result_list))
thread1.start()
start_time = time.perf_counter()
start_time5 = time.process_time()  # It does include time elapsed during sleep and is system-wide.

thread1.join()  # 쓰레드가 작업을 마칠 때까지 기다림
print(f'result : {sum(result_list)}')
end_time = time.perf_counter()
end_time5 = time.process_time()

print(f'쓰레드 작업 실행 시간 (초) : {end_time - start_time}')
print(f'프로세스 실행 시간 : {end_time5 - start_time5}')

"""
work id : 1
result : 166666666666666650000000
쓰레드 작업 실행 시간 (초) : 11.9352351
프로세스 실행 시간 : 11.9375
"""
