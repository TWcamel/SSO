'''
如果我們有許多的工作要分給多個 CPU 核心做運算，
最簡單的方式就是使用佇列的方式，讓多個 CPU 
可從佇列中取得尚未處理的工作來處理：
'''


from SSO import OOP_SSO
import time
import threading

# Worker 類別，負責處理資料
class Worker(threading.Thread):
    def __init__(self, worker_id):
        threading.Thread.__init__(self)
        self.worker_id = worker_id
        self.SSO = OOP_SSO(N_sol=12, N_iter=100, N_var=10, Cg=0.8,
                           Cp=0.5, Cw=0.2, VarMax=5, VarMin=-5, CPUTime=20)

    def run(self):
        # 處理資料
        for dice_i in range(N_DICE):
            SSO_results.append(self.SSO.dice())    
            print("Worker %d: %0.2f" % (self.worker_id, SSO_results[dice_i]) , 'in dice %s\n' % dice_i)
            print(SSO_results)
        print('************************','braek','****************************')    
        # time.sleep(1)

if __name__ == "__main__":
    N_SSO = 2
    # 一個Woker可以同時處理的SSO數目
    N_DICE = 3
    SSO_results = []
    
    # 建立 Worker
    workers = [Worker(worker_id=i) for i in range(N_SSO)] 
    i=0
    # 讓 Worker 開始處理資料
    for worker in workers:
        print('-----------------',i,'------------------')
        worker.start()
        i+=1
        
        
        
    # 等待所有 Worker 結束並加入主線呈
    worker.join()

    print("Done.")
