
import socket import *
import time

# 用来存储所有的新链接的socket
g_socket_list = list()

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
    server_socket.bind(('', 7890))
    server_socket.listen(128)
    server_socket.setblocking(False)

    while True:

        # 用来测试
        time.sleep(0.5)

        try:
            newClientInfo = server_socket.accept()
        except Exception as result:
            pass
        else:
            print("一个新的客户端到来:%s" % str(newClientInfo))
            newClientInfo[0].setblocking(False)  # 设置为非堵塞
            g_socket_list.append(newClientInfo)

        for client_socket, client_addr in g_socket_list:
            try:
                recvData = client_socket.recv(1024)
                if recvData:
                    print('recv[%s]:%s' % (str(client_addr), recvData))
                else:
                    print('[%s]客户端已经关闭' % str(client_addr))
                    client_socket.close()
                    g_socket_list.remove((client_socket,client_addr))
            except Exception as result:
                pass

        print(g_socket_list)  # for test

if __name__ == '__main__':
    main()
