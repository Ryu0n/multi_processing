"""
프로세스 간 통신
"""

from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection


def f(conn: Connection):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe(duplex=True)
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # [42, None, 'hello']
    p.join()
