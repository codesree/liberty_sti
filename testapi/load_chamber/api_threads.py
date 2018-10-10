import time
import threading
from queue import Queue
from multiprocessing.dummy import Pool as threadpool



"""
def sleeper(i):
    print("Thread",i,"sleeps for 5 seconds")
    print("Thread",i,"woke up")


for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()
"""


class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self.queue.get()
            # Checks if the current message is
            # the "Poison Pill"
            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            # "Processes" (or in our case, prints) the queue item
            print("I'm a thread, and I received !!", msg)
        # Always be friendly
        print('Bye byes!')



def Producer():
  # Queue is used to share items between
  # the threads.
  queue = Queue()

  # Create an instance of the worker
  worker = Consumer(queue)
  # start calls the internal run() method to
  # kick off the thread
  worker.start()

  # variable to keep track of when we started
  start_time = time.time()
  # While under 5 seconds..
  while time.time() - start_time < 5:
    # "Produce" a piece of work and stick it in
    # the queue for the Consumer to process
    print("time calc: ",time.time() - start_time)
    queue.put('something at %s' % time.time())
    # Sleep a bit just to avoid an absurd number of messages
    time.sleep(2)

  # This the "poison pill" method of killing a thread.
  queue.put('quit')

  # wait for the thread to close down
  worker.join()

if __name__ == '__main__':
    Producer()













