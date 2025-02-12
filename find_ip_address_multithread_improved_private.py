#import os module to execute commandline in python
import os

#Import threading
import threading

#import regular expressions
import re

#import datetime
import datetime

from fastapi import FastAPI
import uvicorn

from dateutil.parser import parse
app = FastAPI()

#ip address range
ip = '192.168.179.'



def find_active_address(increment,max_value,array):
    
    while (increment <= max_value):
        
        increment+=1
        #print(increment)
        ip_address = ip+str(increment)
        #print(ip_address)

        response = os.popen(f'ping -n 1 -w 10 {ip_address} | find /i "Reply"').read()
        
        if "Reply" in response:
            valid_address = re.search("192.168.179.\d[0-9]{0,3}", response)
            
            address = valid_address.group()
            array.append(address)

def is_reserved_for_vpn(ip_address):
    ip_address_split = ip_address.split(".")
    if int(ip_address_split[3]) >= 201 and int(ip_address_split[3]) <= 250:
        return True

def is_reserved_for_dhcp_allocation(ip_address):
    ip_address_split = ip_address.split(".")
    if int(ip_address_split[3]) >= 190 and int(ip_address_split[3]) <= 199:
        return True
    
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
    
def sorted_pairs(ip_address_list,value,i,key):
    d = ip_address_list[i]
    for j in range(i - 1, -1, -1): 
        if key(ip_address_list[j]) <= key(d): 
            break
        ip_address_list[j + 1] = ip_address_list[j]
    else: # `key(L[j]) > key(d)` for all `j`
        j -= 1
    ip_address_list[j + 1] = d
    return ip_address_list
    # if "Unknown" in name:
    #    split_address =  address.split()
    # starting_value = split_address[3]
    # j =  



def default_addresses(active_ip_addresses):

    key_pair = {
            'First device':'192.168.179.1',

            }
    
    for key,value in tuple(key_pair.items()):
        for i in range(len(active_ip_addresses)):
            if active_ip_addresses[i] == value:
                pass
            elif is_date(active_ip_addresses[i]):
                key_pair['Time of search'] = active_ip_addresses[i]
            elif is_reserved_for_vpn(active_ip_addresses[i]) == True and is_date(active_ip_addresses[i]) == False:
                key_pair['Reserved for EngVPN '+str(i)] = active_ip_addresses[i]
            elif is_reserved_for_dhcp_allocation(active_ip_addresses[i]) == True and is_date(active_ip_addresses[i]) == False:
                key_pair['Reserved for DHCP Allocation '+str(i)] = active_ip_addresses[i]
            elif active_ip_addresses[i] not in key_pair.values():
                key_pair['Unknown Device '+str(i)] = active_ip_addresses[i]
            # elif is_date(active_ip_addresses[i]) == False:
            #     sorted_pairs(active_ip_addresses[i],value,i,key=lambda x: x['NSHNav Sensor Hub'])

    return key_pair    
# ----------------------------------------------------------------------------------------




#Start all threads ----------------------------------------------------------------------------------------

def MultithreadIPs():
    """Enables the multithreading to be started when the page is refreshed as intended
    """
    connected_ip_address_1 = []
    connected_ip_address_2 = []
    connected_ip_address_3 = []
    connected_ip_address_4 = []
    connected_ip_address_5 = []
    connected_ip_address_6 = []
    connected_ip_address_7 = []
    connected_ip_address_8 = []
    connected_ip_address_9 = []
    connected_ip_address_10 = []
    connected_ip_address_11 = []
    connected_ip_address_12 = []
    connected_ip_address_13 = []
    connected_ip_address_14 = []
    connected_ip_address_15 = []
    connected_ip_address_16 = []
    
    #Average time taken = ~ 8 seconds
    final_ip_array = []


    final_ip_array.append(str(datetime.datetime.now()))
         
    t1 = threading.Thread(target=find_active_address, args=(0,16,connected_ip_address_1), daemon=True)
    t2 = threading.Thread(target=find_active_address, args=(17,33,connected_ip_address_2), daemon=True)
    t3 = threading.Thread(target=find_active_address, args=(34,49,connected_ip_address_3), daemon=True)
    t4 = threading.Thread(target=find_active_address, args=(50,65,connected_ip_address_4), daemon=True)
    t5 = threading.Thread(target=find_active_address, args=(66,81,connected_ip_address_5), daemon=True)
    t6 = threading.Thread(target=find_active_address, args=(82,97,connected_ip_address_6), daemon=True)
    t7 = threading.Thread(target=find_active_address, args=(98,113,connected_ip_address_7), daemon=True)
    t8 = threading.Thread(target=find_active_address, args=(114,129,connected_ip_address_8), daemon=True)
    t9 = threading.Thread(target=find_active_address, args=(130,145,connected_ip_address_9), daemon=True)
    t10 = threading.Thread(target=find_active_address, args=(146,161,connected_ip_address_10), daemon=True)
    t11 = threading.Thread(target=find_active_address, args=(162,177,connected_ip_address_11), daemon=True)
    t12 = threading.Thread(target=find_active_address, args=(178,193,connected_ip_address_12), daemon=True)
    t13 = threading.Thread(target=find_active_address, args=(194,209,connected_ip_address_13), daemon=True)
    t14 = threading.Thread(target=find_active_address, args=(210,225,connected_ip_address_14), daemon=True)
    t15 = threading.Thread(target=find_active_address, args=(226,241,connected_ip_address_15), daemon=True)
    t16 = threading.Thread(target=find_active_address, args=(242,255,connected_ip_address_16), daemon=True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()

    #Join the threads  ----------------------------------------------------------------------------------------
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()

    #Join arrays from separate threads together  ----------------------------------------------------------------------------------------
    final_ip_array += connected_ip_address_1
    final_ip_array += connected_ip_address_2
    final_ip_array += connected_ip_address_3
    final_ip_array += connected_ip_address_4
    final_ip_array += connected_ip_address_5
    final_ip_array += connected_ip_address_6
    final_ip_array += connected_ip_address_7
    final_ip_array += connected_ip_address_8
    final_ip_array += connected_ip_address_9
    final_ip_array += connected_ip_address_10
    final_ip_array += connected_ip_address_11
    final_ip_array += connected_ip_address_12
    final_ip_array += connected_ip_address_13
    final_ip_array += connected_ip_address_14
    final_ip_array += connected_ip_address_15
    final_ip_array += connected_ip_address_16
    #print(final_ip_array)
    return default_addresses(final_ip_array)






# ----------------------------------------------------------------------------------------
@app.get("/")
async def root():
    return{ 
     "ip_addresses": MultithreadIPs()
    } 

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("find_ip_address_multithread_improved:app", host="0.0.0.0", port=8100, reload=True)
