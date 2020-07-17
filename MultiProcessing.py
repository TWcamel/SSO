'''
如果我們有許多的工作要分給多個 CPU 核心做運算，
最簡單的方式就是使用佇列的方式，讓多個 CPU 
可從佇列中取得尚未處理的工作來處理：

If we have a lot of work to be divided into multiple CPU cores to do calculations,
The easiest way is to use a queue to allow multiple CPUs
You can get the unprocessed work from the queue to handle:
'''


from test_SSO import SSO
import time
import threading
# import queue

evt = threading.Event()

# Worker 類別，負責處理資料
class Worker(threading.Thread):
    def __init__(self, worker_id):
        threading.Thread.__init__(self)
        self.worker_id = worker_id

    def run(self):
        
        # 處理資料，並把結果存進SSO_results
        for dice_i in range(N_HANDLE):
            SSO_results.append(SSO(10,3,10))
            evt.wait()      # 等待主執行緒
            print("Worker %d" % (self.worker_id) , 'in dice %s\n' % dice_i)
            
            # print("Worker %d: %s" % (self.worker_id, SSO_results[dice_i]) , 'in dice %s\n' % dice_i)
            # print(SSO_results)
            
        

if __name__ == "__main__":
    N_SSO = 2
    # 一個Woker可以同時處理的SSO數目
    N_HANDLE = 2
    SSO_results = []
    
    # 建立 Worker
    workers = [Worker(worker_id=i) for i in range(N_SSO)] 
    # 讓 Worker 開始處理資料
    for worker in workers:
        worker.start()
        time.sleep(1)   # 主執行緒休眠1秒
        evt.set()       # 主執行緒設置事件(roll out)
    # 等待所有 Worker 結束
    worker.join()

    print("Done.")
