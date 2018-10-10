import time
import threading
from queue import Queue
from pymongo import MongoClient
import requests
import json


class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
        db = MongoClient()
        con = db['mongo_builder']
        self.col = con['asset_api']

    def run(self):
        while True:
            exestat = self._queue.get()
            if isinstance(exestat, str) and exestat == 'quit':
                break
            print(exestat, "started.....")

            head = {'Content-Type': 'application/json', 'Accept': 'application/json'}

            asset_req = self.col.find_one({'quoteHeader.srsId': 'SRS_ID'})

            del asset_req['_id']

            asset_req = json.dumps(asset_req, indent=5)

            #print(asset_req)
            print(exestat,"is Entering API GATEWAY now")

            req_url = 'http://prbk-pa001sap4v/Insurance.Quoting2/api/Quotes/Process'

            response = requests.post(req_url, data=asset_req, headers=head)

            send_q = time.time()

            print("Response  from API Gateway...........", response.status_code)
            do_resp = response.json()
            do_resp = json.dumps(do_resp, indent=5)

            print(do_resp)

            recv_q = time.time()
            print("Thread spin up time (in seconds): {}".format(recv_q - send_q))

            print(exestat, 'task completed...')

        print('Thread is now exiting...')


def Producer():
    exec_mode = [
        'exec1','exec2',
        'exec3','exec4',
        'exec5','exec6',
        'exec7','exec8',
        'exec9','exec10',

        # etc..
    ]
    queue = Queue()
    worker_threads = build_worker_pool(queue, 10)
    start_time = time.time()

    # Add the urls to process
    for exec in exec_mode:
        queue.put(exec)
    # Add the poison pillv
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()


    print('Done! Time taken: {}'.format(time.time() - start_time))


def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    Producer()
