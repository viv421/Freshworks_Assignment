import freshworkscode as code 
#import the main file("freshworkscode" is the name of the file I have used) as a library 
code.create("Vivek",50)#Creating a key with key_name("Vivek"),value("50") and with no Time-to-Live property
code.create("Domakuntla",70,180) #Creating a key with key_name("Domakuntla"),value("70") and with Time-to-Live property value("180" seconds)
code.read("Vivek")#Returns the value of the respective key in JSON object format 'key_name:value'('Vivek:50' in this case)
code.read("Domakuntla")#Returns the value of the respective key in JSON object format("Domakuntla:70") if the Time-to-live IS NOT EXPIRED,Otherwise throws an Error
code.create("Domakuntla",50)#Returns an ERROR since the key_name("Domakuntla") already exists in the database
code.delete("Vivek")#Deletes the key and its value("Vivek")from the database(memory is also deallocated and freed)
#Storing data using multiple threads 
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))#t1=Thread(target=(create),args=("Viv",20,60)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))#t1=Thread(target=(read or delete),args=("Viv"))
t2.start()
t2.sleep()
#Throws "invalidkey" error if key_length is greater than 32 or key_name contains any numeric,special characters etc.
#Throws "key does not exist" error if key_name is not typed correctly or already deleted.
#Throws "File memory limit reached" error if file the memory exceeds 1GB


