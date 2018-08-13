#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/hci.h>
#include <bluetooth/hci_lib.h>
#include <bluetooth/rfcomm.h>

#define my_device "88:79:7E:2B:C1:25"
#define Raspberry_pi "B8:27:EB:07:AE:EC"

char* Scan_device(int dev_id,int sock)
{
    inquiry_info *ii = NULL;
    int max_rsp, num_rsp;
    int len = 8, flags = IREQ_CACHE_FLUSH;
    int i;
    char addr[19] = { 0 };
    char name[248] = { 0 };

    max_rsp = 255;


    ii = (inquiry_info*)malloc(max_rsp * sizeof(inquiry_info));
while(1){
    num_rsp = hci_inquiry(dev_id, len, max_rsp, NULL, &ii, flags);//performs a Bluetooth device discovery and returns a list of detected devices and some basic information about them in the variable ii.
    if( num_rsp < 0 ) perror("hci_inquiry");

    for (i = 0; i < num_rsp; i++) {

        ba2str(&(ii+i)->bdaddr, addr);

        memset(name, 0, sizeof(name));

        if (hci_read_remote_name(sock, &(ii+i)->bdaddr, sizeof(name), 
            name, 0) < 0)
        strcpy(name, "[unknown]");
        printf("%s  %s\n", addr, name);
	if((strcmp(addr,my_device) == 0)){
		break;
	}
    }
	if((strcmp(addr,my_device) == 0)){
		break;
	}
} 
    free( ii );


char* data = NULL;
	if(addr){
		data = (char*)malloc(sizeof(char)*20);
		memset(data,0,sizeof(data));
		sprintf(data,"%s",addr);
	}
    return data;
}

int bluez_pair_device(char* addr, char *controller_baddr)
{
    char btaddr_str[19] = { '\0' };
    int retry_count = 0;
    char pair_cmd[512];
    char response[512];
    char keycmd[512];
    char hciinfo[50];
    FILE *fp;
    int ret;
    strcpy(btaddr_str, addr);

    /* pairing might already exists so check first */
    /* /var/lib/bluetooth/78:A5:04:23:4A:51/00:04:3E:9F:C1:3F/info */
    sprintf(keycmd, "sudo cat /var/lib/bluetooth/%s/%s/info | grep Key=", controller_baddr, btaddr_str);
    fp = popen(keycmd, "r");
    if (fp) {
        if (fgets(response, sizeof(response) - 1, fp) != NULL) {
            pclose(fp);
            goto exit_pair;
        }
        printf("Pairing does not exists for: '%s'", btaddr_str);
        pclose(fp);
    }

    strcpy(response, btaddr_str);
    btaddr_str[2] = '_';
    btaddr_str[5] = '_';
    btaddr_str[8] = '_';
    btaddr_str[11] = '_';
    btaddr_str[14] = '_';
    sprintf(pair_cmd, "sudo -i hcitool cc %s && dbus-send --system --dest=org.bluez --print-reply /org/bluez/hci0/dev_%s org.bluez.Device1.Pair",
        response,
        btaddr_str);

    sprintf(hciinfo, "hcitool info %s", response);
retry_pair:
    if (retry_count > 5)
        return -1;

    ret = system(pair_cmd);
    if (ret) {
        retry_count++;
        printf("%s failed to pair bl device: %s", __FUNCTION__, btaddr_str);
        printf("cmd: '%s'", pair_cmd);
        system(hciinfo);
    }

    fp = popen(keycmd, "r");
    if (!fp) {
        printf("%s failed to run cmd: '%s'", __FUNCTION__, keycmd);
        retry_count++;
        goto retry_pair;
    }
    if (fgets(response, sizeof(response) - 1, fp) == NULL) {
        pclose(fp);
        printf("%s LinkKey missing in file", __FUNCTION__);
        printf("cmd: '%s'", pair_cmd);
        retry_count++;
        goto retry_pair;
    }
    pclose(fp);

exit_pair:
    return 0;
}

void bluetooth_receive(){
    struct sockaddr_rc loc_addr = { 0 }, rem_addr = { 0 };
    char buf[1024] = { 0 };
    int s,client, bytes_read;
    socklen_t opt = sizeof(rem_addr);
    s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);
    // bind socket to port 1 of the first available 
    // local bluetooth adapter
    loc_addr.rc_family = AF_BLUETOOTH;
    loc_addr.rc_bdaddr = *BDADDR_ANY;
    loc_addr.rc_channel = (uint8_t) 1;
    bind(s, (struct sockaddr *)&loc_addr, sizeof(loc_addr));
while(buf != '8'){
    // put socket into listening mode
    listen(s, 1);

    // accept one connection
    client = accept(s, (struct sockaddr *)&rem_addr, &opt);

    ba2str( &rem_addr.rc_bdaddr, buf );
    fprintf(stderr, "accepted connection from %s\n", buf);
    memset(buf, 0, sizeof(buf));

    // read data from the client
    bytes_read = read(client, buf, sizeof(buf));
    if( bytes_read > 0 ) {
        printf("received [%s]\n", buf);
    }
}
    // close connection
    close(client);
}

void bluetooth_send(){
    struct sockaddr_rc loc_addr = { 0 }, rem_addr = { 0 };
    char buf[1024] = { 0 };
	int abc;
    int s,client, bytes_read;
    socklen_t opt = sizeof(rem_addr);
    s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);
    // bind socket to port 1 of the first available 
    // local bluetooth adapter
    loc_addr.rc_family = AF_BLUETOOTH;
    loc_addr.rc_bdaddr = *BDADDR_ANY;
    loc_addr.rc_channel = (uint8_t) 1;
    bind(s, (struct sockaddr *)&loc_addr, sizeof(loc_addr));
while(abc != '8'){
    // put socket into listening mode
    listen(s, 1);

    // accept one connection
    client = accept(s, (struct sockaddr *)&rem_addr, &opt);

    ba2str( &rem_addr.rc_bdaddr, buf );
    fprintf(stderr, "accepted connection from %s\n", buf);
    memset(buf, 0, sizeof(buf));

scanf("%d",&abc);
    // read data from the client
    bytes_read = write(s,abc,sizeof(abc));
}
    // close connection
    close(client);
}

int main(){
	int dev_id,sock,status;
	char* ip_address;
	    dev_id = hci_get_route(NULL); // retrieve the resource number of the first available Bluetooth adapter.
	    sock = hci_open_dev( dev_id );// convenience function that opens a Bluetooth socket with the specified resource number.
	    if (dev_id < 0 || sock < 0) {
        	perror("opening socket");
	        exit(1);
	    }
	
	ip_address = Scan_device(dev_id,sock);
	printf(" \n %s \n",ip_address);
	bluez_pair_device(ip_address,Raspberry_pi);
	int val;
while(val != 0){
	printf("\n Select 1: Send \n Select 2: Receive \n Select 0: Exit \n");
	scanf("%d",&val);
	switch(val){
	case 1:
		bluetooth_send();
	case 2:
		bluetooth_receive();	
	case 0:
		break;
	}
}
	close( sock );
	free(ip_address);

return 0;
}