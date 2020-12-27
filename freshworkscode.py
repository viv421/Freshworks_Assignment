import threading 
from threading import*
import time
Dict={} #Dictionary to store the data
#Create operation 
def create(key,value,timeout=0):
    if key in Dict:
        print("Error: This key already exists") 
    else:
        if(key.isalpha()):
            if len(Dict)<(1024*1020*1024) and value<=(16*1024*1024): #Constraints for file size less than 1GB and JSON object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #Constraints for input key_name capped at 32chars
                    Dict[key]=l
            else:
                print("Error: Memory limit exceeded!! ")
        else:
            print("Error: Invalid key_name!! key_name must contain only alphabets or numbers")
#Read operation
def read(key):
    if key not in Dict:
        print("Error: given key does not exist in database. Please enter a valid key") 
    else:
        b=Dict[key]
        if b[1]!=0:
            if time.time()<b[1]: #Checking the expiry time
                str1=str(key)+":"+str(b[0]) #Return the value in JSON Object format
                return str1
            else:
                print("Error: Time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#Delete operation

def delete(key):
    if key not in Dict:
        print("Error: given key does not exist in database. Please enter a valid key")
    else:
        b=Dict[key]
        if b[1]!=0:
            if time.time()<b[1]: #Checking the expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")


