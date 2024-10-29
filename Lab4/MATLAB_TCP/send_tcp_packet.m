
function send_tcp_packet(server_ip, server_port, message)
    try
        % Create a TCP client
        t = tcpclient(server_ip, server_port, 'Timeout', 10);
        disp(['Connected to ', server_ip, ':', num2str(server_port)]);
        
        % Send the message
        write(t, uint8(message));  % Convert message to uint8 for transmission
        disp(['Sent: ', message]);

        % Optionally receive a response from the server
        pause(0.5); % Allow some time for response (if necessary)
        if t.BytesAvailable > 0
            response = read(t, t.BytesAvailable, 'char');
            disp(['Received: ', response]);
        end

    catch ME
        % Display any errors
        disp(['Error: ', ME.message]);
    end

    % Ensure the connection is closed
    clear t;
    disp('Connection closed.');
end

