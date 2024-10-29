% Main script
server_ip = '192.168.1.159';
server_port = 5001;
message_home = 'get_angles()';

% Call the function
send_tcp_packet(server_ip, server_port, message_home);


