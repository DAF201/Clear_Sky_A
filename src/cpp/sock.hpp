// This file is just to same my time making socket, not for making DLL
#include <WinSock2.h>
#include <stdio.h>
#include <string>
#include <thread>
#include <queue>
#include <windows.h>
#define MAX_LENGTH 1024
#define MTU_SIZE 1460
using namespace std;
struct send_pkg
{
    void *data;
    int size;
};
class cpp_socket
{
public:
    cpp_socket(string server_ip, int server_port, int interval = 100)
    {

        sending_interval = interval;
        socket_closed = false;
        sock_version = MAKEWORD(2, 2);
        // Start up the WSA
        if (WSAStartup(sock_version, &WSA_data) != 0)
        {
            printf("%s", "WSAStartup error\n");
            exit(-1);
        }
        // create socket
        client_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        if (client_socket == INVALID_SOCKET)
        {
            printf("%s", "error when creating socket\n");
            exit(-1);
        }

        // bind socket
        server_address.sin_family = AF_INET;
        server_address.sin_port = htons(server_port);
        server_address.sin_addr.s_addr = inet_addr(server_ip.c_str());

        // create connection
        if (connect(client_socket, (sockaddr *)&server_address, sizeof(server_address)) == SOCKET_ERROR)
        {
            printf("%s", "connecting error\n");
            exit(-1);
        }

        // LIE thread header used unix lib, so dont work here
        // create recving thread and sending thread
        RECV_THREAD = thread(&cpp_socket::RECVING, this);
        SEND_THREAD = thread(&cpp_socket::SENDING, this);

        printf("%s", "socket created\n");
    }
    void S_send(void *data, int size)
    {
        // push a package to the waitlist
        send_pkg new_pkg = {data, size};
        send_queue.push(new_pkg);
    };

    void *S_recv()
    {
        // take a package out of buffer
        if (!recv_queue.empty())
        {
            void *data = recv_queue.front();
            recv_queue.pop();
            return data;
        }
        return nullptr;
    };

    void S_close()
    {

        closesocket(client_socket);
        WSACleanup();
    }

private:
    SOCKET client_socket;
    WORD sock_version;
    WSADATA WSA_data;
    sockaddr_in server_address;
    thread RECV_THREAD;
    thread SEND_THREAD;
    queue<void *> recv_queue;
    queue<send_pkg> send_queue;
    int sending_interval;
    bool socket_closed;

    void SENDING()
    {
        send_pkg data;
        while (true)
        {
            if (!send_queue.empty())
            {
                data = send_queue.front();
                send_queue.pop();
                send(client_socket, (const char *)data.data, data.size, 0);
                Sleep(sending_interval);
            }
        }
    }
    void RECVING()
    {
        char buffer[MTU_SIZE];
        while (true)
        {
            recv(client_socket, buffer, MTU_SIZE, 0);
            recv_queue.push(buffer);
        }
    }
};
