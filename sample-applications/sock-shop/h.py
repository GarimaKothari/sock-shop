import subprocess
import time
print("1.Apply cpu hog")
print("2.Apply memory hog")
i=int(input("Enter the choice: "))    
if(i==1):
   print("select the microservice")
   print("1.catalogue")
   print("2.orders")
   p=int(input("Enter the choice: "))
   if(p==1):
     o=subprocess.run('kubectl apply -f chaos/catalogue/catalogue-cpu-hog.yaml',shell=True,capture_output=True)
     print(o.stdout.decode())
     time.sleep(20)
     o1=subprocess.run('kubectl describe chaosengine catalogue-cpu-hog -n litmus',shell=True,capture_output=True)
     print(o1.stdout.decode())
   elif(p==2):
      o=subprocess.run('kubectl apply -f chaos/orders/orders-cpu-hog.yaml',shell=True,capture_output=True)
      print(o.stdout.decode())
      time.sleep(20)
      o1=subprocess.run('kubectl describe chaosengine orders-cpu-hog -n litmus',shell=True,capture_output=True)
      print(o1.stdout.decode())
elif(i==2):
    print("select the microservice")
    print("1.catalogue")
    print("2.orders")
    p=int(input("Enter the choice: "))
    if(p==1):
     o=subprocess.run('kubectl apply -f chaos/catalogue/catalogue-memory-hog.yaml',shell=True,capture_output=True)
     print(o.stdout.decode())
     time.sleep(20)
     o1=subprocess.run('kubectl describe chaosengine catalogue-memory-hog -n litmus',shell=True,capture_output=True)
     print(o1.stdout.decode())
    elif(p==2):
       o=subprocess.run('kubectl apply -f chaos/orders/orders-memory-hog.yaml',shell=True,capture_output=True)
       print(o.stdout.decode())
       time.sleep(20)
       o1=subprocess.run('kubectl describe chaosengine orders-memory-hog -n litmus',shell=True,capture_output=True)
       print(o1.stdout.decode())



