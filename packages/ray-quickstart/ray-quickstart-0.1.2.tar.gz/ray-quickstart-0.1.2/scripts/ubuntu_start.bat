netsh interface portproxy reset

REM Start Ubuntu "nohup sleep 100000 &" to keep the process running
START /B CMD /C "C:\Windows\system32\wsl.exe -u %USERNAME% -d Ubuntu-22.04 --cd ~/git nohup sleep 100000 &"

SET ip_address_string="IPv4 Address"
FOR /F "usebackq tokens=2 delims=:" %%i in (`ipconfig ^| findstr /c:%ip_address_string%`) do (
    SET IP_ADDRESS=%%i
    GOTO NEXT
)

:NEXT

FOR /F "tokens=*" %%i IN ('wsl -d Ubuntu-22.04 hostname -I') DO SET UBUNTU_IP_ADDRESS=%%i

netsh interface portproxy set v4tov4 listenport=22 listenaddress=%IP_ADDRESS% connectport=53422 connectaddress=%UBUNTU_IP_ADDRESS% protocol=tcp
netsh interface portproxy set v4tov4 listenport=6380 listenaddress=%IP_ADDRESS% connectport=6380 connectaddress=%UBUNTU_IP_ADDRESS% protocol=tcp
netsh interface portproxy set v4tov4 listenport=8265 listenaddress=%IP_ADDRESS% connectport=8265 connectaddress=%UBUNTU_IP_ADDRESS% protocol=tcp
netsh interface portproxy set v4tov4 listenport=10001 listenaddress=%IP_ADDRESS% connectport=10001 connectaddress=%UBUNTU_IP_ADDRESS% protocol=tcp
netsh interface portproxy show all
