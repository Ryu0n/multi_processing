"""
싱글 쓰레드와 실행시간의 차이가 거의 없음
why ? GIL (Global Interpreter Locking)

* 멀티 쓰레드 *
하나의 쓰레드가 CPU 작업을 마치고 I/O 작업을 실행하는 동안 다른 쓰레드가 CPU 작업을 동시에 실행할 수 있다.
CPU 작업이 적고 I/O 작업이 많은 병렬처리 프로그램에서 효과를 볼 수 있다.
"""


import time
from tqdm import tqdm
from threading import Thread


def addition_operator(work_id, start, end, result):
    print(f'work id : {work_id}')
    total = 0
    for i in tqdm(range(start, end)):
        # print(f'work id : {work_id}, i : {i}')
        total += i
        result.append(total)
    return


result_list = list()
thread1 = Thread(target=addition_operator, args=(1, 0, 100000000//2, result_list))
thread2 = Thread(target=addition_operator, args=(2, 100000000//2, 100000000, result_list))

thread1.start()
start_time = time.perf_counter()
start_time5 = time.process_time()  # It does include time elapsed during sleep and is system-wide.
thread2.start()

thread1.join()  # 쓰레드가 작업을 마칠 때까지 기다림
thread2.join()
print(f'result : {sum(result_list)}')
end_time = time.perf_counter()
end_time5 = time.process_time()

print(f'쓰레드 작업 실행 시간 (초) : {end_time - start_time}')
print(f'프로세스 실행 시간 : {end_time5 - start_time5}')

"""
work id : 1
work id : 2
result : 104166667916666650000000
쓰레드 작업 실행 시간 (초) : 12.217602099999999
프로세스 실행 시간 : 12.21875
"""
