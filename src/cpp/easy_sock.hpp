#include <string>
#include <cstring>
#include <cstdlib>
#include <thread>
#include <vector>
using namespace std;
#ifdef _WIN32
#include <WinSock2.h>
#pragma comment(lib, "ws2_32.lib")

#define MAX_LENGTH 1024

const static int ip_type[3] = {AF_INET, AF_INET6, AF_UNIX};
const static int sock_type[3] = {SOCK_STREAM, SOCK_DGRAM, SOCK_RAW};

typedef struct sock_msg
{
    SOCKET sock;
    int MSG_length;
    int MSG_num;
    string MSG;
} sock_msg;

vector<sock_msg> socket_msg_queue = vector<sock_msg>();

void subsocket_handler(SOCKET sub_socket)
{
    char buffer[MAX_LENGTH];
    int MSG_length = 0;
    int MSG_num = 0;
    while (true)
    {
        try
        {
            recv(sub_socket, buffer, sizeof(buffer), 0);
            string str_buffer = string(buffer);
            if (str_buffer.find("_EOS_") != string::npos)
            {

                return;
            }
            sock_msg new_msg = {sub_socket, stoi(str_buffer.substr(0, 5)), stoi(str_buffer.substr(5, 5)), str_buffer};
        }
        catch (...)
        {
            continue;
        }
    }
}

class easy_sock_s
{
public:
    easy_sock_s(string IP = "0.0.0.0", int port = 920, int ip_protocal = 0, int socket_protocal = 0, int max_listen)
    {
        if (server_init <= 0)
        {
            init(IP, port, ip_protocal, socket_protocal, max_listen);
            server_init++;
        }
        else
        {
            return;
        }
    }
    void cleanup()
    {
        if (server_init <= 0)
        {
            return;
        }
        WSACleanup();
        server_init--;
    }
    void start()
    {
        sock_thread = thread(server_run);
    }
    void recv()
    {
    }
    void send()
    {
    }
    ~easy_sock_s()
    {
        if (server_init > 0)
        {
            cleanup();
        }
    }

private:
    int server_init = 0;
    int server_status = 0;
    int sock_size = sizeof(sockaddr_in);
    SOCKET server_sock;
    sockaddr_in server_sock_addr;
    thread sock_thread;

    void init(string IP, int port, int ip_protocal, int socket_protocal, int max_listen = 10)
    {
        WORD wVersion = MAKEWORD(2, 2);
        WSADATA wsadata;
        WSAStartup(wVersion, &wsadata);
        server_sock = socket(ip_type[ip_protocal], sock_type[socket_protocal], 0);
        memset(&server_sock_addr, 0, sizeof(server_sock_addr));
        server_sock_addr.sin_family = AF_INET;
        server_sock_addr.sin_addr.s_addr = inet_addr(IP.c_str());
        server_sock_addr.sin_port = htons(port);
        bind(server_sock, (SOCKADDR *)&server_sock_addr, sock_size);
        listen(server_sock, max_listen);
    }
    void server_run()
    {
        while (server_status == 0)
        {
            SOCKET sub_s = accept(server_sock, (SOCKADDR *)&server_sock_addr, &sock_size);
            thread sub_sock_thread = thread(subsocket_handler, sub_s);
            sub_sock_thread.detach();
        }
    }
};

#endif
