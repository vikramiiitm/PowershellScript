import threading
import time
import subprocess
import sys
import multiprocessing
from time import perf_counter

class PowerShellScipts:
    """
    Using multithreading and multiprocessing to download software by invoking powershell script.
    """
    
    def __init__(self, data) -> None:
        self.data = data
    
    def powershell_run(self,file, url):
        cmd = ["PowerShell", "-ExecutionPolicy", "Unrestricted", "-File", ".\\PsiphonVpnDownloadInstall.ps1", file, url]
        ec = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        print(f"{ec.stdout.decode('utf-8')}")
        return
    
    # IO Bound: using multithreading
    def thread_download(self) -> None:
        start = perf_counter()
        threads = []
        for file, url in self.data.items():
            print(file, url)
            for i in range(50):
                Connection = threading.Thread(target=self.powershell_run, args=(file+str(i), url))
                threads.append(Connection)
                Connection.start()
            break
            
        for i in threads:
            i.join()

        print(f"Total Time taken: {perf_counter()-start} seconds")


    # CPU Bound: using multiprocessing
    def mprocess_download(self) -> None:
        start = perf_counter()
        process = []
        for file, url in self.data.items():
            for i in range(50):
                print(file, url)
                Connection = multiprocessing.Process(target=self.powershell_run, args=(file+str(i), url))
                process.append(Connection)
                Connection.start()
            break
            
        for i in process:
            i.join()
        print(f"Total Time taken: {perf_counter()-start} seconds")
        
    def normal_download(self)->None:
        start = perf_counter()
        for file, url in self.data.items():
            for i in range(50):
                self.powershell_run(file+str(i), url)
                
        print(f"Total Time taken: {perf_counter()-start} seconds")

            
    def process_run(self):
        pass
            
        
if __name__ == "__main__":
    data = {
            "psiphon":"https://psiphon.ca/psiphon3.exe",
            }
    ps = PowerShellScipts(data)
    # ps.thread_download()
    # ps.mprocess_download()
    ps.normal_download()
    
    # Downloading and installing is fast using multiprocessing, also it's safe afater testing for downlaoding 50 software copies
    # multiprocessing time: ~55 seconds
    # multithreading time: ~59 seconds
    # Sequential time: ~148