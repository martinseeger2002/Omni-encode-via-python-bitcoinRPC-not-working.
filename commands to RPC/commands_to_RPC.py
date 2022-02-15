import time


from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'user'
rpc_password = 'password'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))


##converts image.jpeg to b64 byte string
import base64
with open("image.jpeg", "rb") as file_to_string:
    data_b = base64.b64encode(file_to_string.read())
    file_to_string.close
    data = str(data_b)[2:]  ##this removes the "b'" from the begining of the byte string.

##splits b64 bytes into 255 data packets
n = 255
data_list = [data[index : index + n] for index in range(0, len(data), n)]

##adds to RPCcommands.txt
def add_to_output_txt():
    f = open('arguments.txt', 'a+')
    arguments_str = str(arguments)
    f.write(str(arguments_str+'\n\n'))
    f.close()

##creates RPCcommands.txt
f = open('arguments.txt', 'w+')
f.close()

## set user varialbles here.
name = 'monkeinnepal'
maddress = 'MWHEuBEecYU9429irdNUefe3qpQTz4mzNR'
file_type = 'JPEG'

serial_num = 100000
data_packet_num = 0
max_data_packet_num = (len(data_list)-1)

"""
below here is broken!! maybe someome can help I am atempting to insert the data packet into the four fields in the omni
command and run the comanned though the RPC.
"""
{"jsonrpc": "1.0", "id":"curltest", "method": "omni_sendissuancefixed", "params": ["3Ck2kEGLJtZw9ENj2tameMCtS3HB7uRar3", 2, 1, 0, "Companies", "Litecoin Mining", "Quantum Miner", "", "", "1000000"] }
while data_packet_num <= max_data_packet_num:
    
    serial_num_str = str(serial_num)[-5:]
    
     ## if there is enough data to create one data packet. This creates the commmand and adds it to RPCcommands.txt.
    if data_packet_num==max_data_packet_num:
        d1 = data_list[data_packet_num]
        arguments = [maddress, 1, 1, 0, d1, "", name+file_type+serial_num_str, "", "", "1"]
        arguments_str = str(arguments)
        arguments_quotes = arguments_str[1:-1].replace("'", '"')
        #rpc_connection.omni_sendissuancefixed(arguments_quotes)      # remove the "#" when fixed.
        print(arguments_quotes)
        add_to_output_txt()
        print(serial_num)
        exit()    
     ## if there is enough data to create two data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_packet_num==max_data_packet_num-1:
        d1 = data_list[data_packet_num]
        d2 = data_list[data_packet_num+1]
        arguments = [maddress, 1, 1, 0, d1, d2, name+file_type+serial_num_str, "", "", "1"]
        arguments_str = str(arguments)
        arguments_quotes = arguments_str[1:-1].replace("'", '"')
        #rpc_connection.omni_sendissuancefixed(arguments_quotes)      # remove the "#" when fixed.
        print(arguments_quotes)
        add_to_output_txt()
        print(serial_num)
        exit()
     ## if there is enough data to create three data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_packet_num==max_data_packet_num-2:
        d1 = data_list[data_packet_num]
        d2 = data_list[data_packet_num+1]
        d3 = data_list[data_packet_num+2]
        arguments = [maddress, 1, 1, 0, d1, d2, name+file_type+serial_num_str, d3, "", "1"]
        arguments_str = str(arguments)
        arguments_quotes = arguments_str[1:-1].replace("'", '"')
        #rpc_connection.omni_sendissuancefixed(arguments_quotes)      # remove the "#" when fixed.
        print(arguments_quotes)
        add_to_output_txt()
        print(serial_num)
        exit()    
     ## if there is enough data to create four data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_packet_num==max_data_packet_num-3:
        d1 = data_list[data_packet_num]
        d2 = data_list[data_packet_num+1]
        d3 = data_list[data_packet_num+2]        
        d4 = data_list[data_packet_num+3] 
        arguments = [maddress, 1, 1, 0, d1, d2, name+file_type+serial_num_str, d3, d4, "1"]
        arguments_str = str(arguments)
        arguments_quotes = arguments_str[1:-1].replace("'", '"')
        #rpc_connection.omni_sendissuancefixed(arguments_quotes)      # remove the "#" when fixed.
        print(arguments_quotes)
        add_to_output_txt()
        print(serial_num)
        exit()  
    ## if there is enough data to create more than four data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_packet_num<=max_data_packet_num-4:
        d1 = data_list[data_packet_num]
        d2 = data_list[data_packet_num+1]
        d3 = data_list[data_packet_num+2]        
        d4 = data_list[data_packet_num+3] 
        arguments = [maddress, 1, 1, 0, d1, d2, name+file_type+serial_num_str, d3, d4, "1"]
        arguments_str = str(arguments)
        arguments_quotes = arguments_str[1:-1].replace("'", '"')
        #rpc_connection.omni_sendissuancefixed(arguments_quotes)        #I dont know why its not working the arguments seen to be in the corret format.
        print(arguments_quotes)
        add_to_output_txt()
        print(serial_num)
        serial_num += 1
        data_packet_num += 4
        
       ##await rpc_command.omni_sendissuancefixed("hash")       #maybe the await can wait for txid hash string return

