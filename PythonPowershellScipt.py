import threading
import time
import subprocess
import sys

class PowerShellScipts:
    
    def __init__(self, *args) -> None:
        self.address = args
    
    def _run(self,address):
        cmd = ["PowerShell", "-ExecutionPolicy", "Unrestricted", "-File", ".\\PsiphonVpnDownloadInstall.ps1"]
        ec = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        print(f"{ec.stdout.decode('utf-8')}")
    
    # IO Bound: using multithreading
    def thread_run(self) -> None:
        threads = []
        for i in self.address:
            Connection = threading.Thread(target=self._run, args=(i,))
            threads.append(Connection)
            Connection.start()
            
        for i in threads:
            i.join()
            
    def process_run(self):
        pass
            
        
if __name__ == "__main__":
    ps = PowerShellScipts("30")
    ps.thread_run()
