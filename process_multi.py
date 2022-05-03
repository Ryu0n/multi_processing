"""
multiprocess
여러개의 프로세스를 생성하여 각각에 메모리 공간을 할당하여 병렬처리
"""

import time
from tqdm import tqdm
from multiprocessing import Process, Queue


def addition_operation(work_id, start, end, result):
    print(f'work id : {work_id}')
    total = 0
    for i in tqdm(range(start, end)):
        # print(f'work id : {work_id}, i : {i}')
        total += i
        result.put(total)
    return


if __name__ == '__main__':
    result_list = Queue()
    process1 = Process(target=addition_operation, args=(1, 0, 100000000 // 2, result_list))
    process2 = Process(target=addition_operation, args=(2, 100000000 // 2, 100000000, result_list))
    start_time = time.perf_counter()
    start_time5 = time.process_time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    total = 0
    qsize = result_list.qsize()
    while qsize > 0:
        total = total + result_list.get()
        qsize = qsize - 1

    print(f'result : {result_list}')
    end_time = time.perf_counter()
    end_time5 = time.process_time()

    print(f'쓰레드 작업 실행 시간 (초) : {end_time - start_time}')
    print(f'프로세스 실행 시간 : {end_time5 - start_time5}')
