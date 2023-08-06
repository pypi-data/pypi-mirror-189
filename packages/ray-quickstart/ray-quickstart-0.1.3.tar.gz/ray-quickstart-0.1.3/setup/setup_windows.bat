setlocal

wsl --install Ubuntu-22.04

REM enable password-less sudo
wsl -u root -d Ubuntu-22.04 -- echo "%USERNAME%    ALL = (ALL) NOPASSWD: ALL" ^> /etc/sudoers.d/%USERNAME%
wsl -u root -d Ubuntu-22.04 -- chmod 0440 /etc/sudoers.d/%USERNAME%

cd %~dp0
wsl -u %USERNAME% ./setup_ubuntu.sh

netsh advfirewall firewall add rule name="SSH Port 22" dir=in action=allow protocol=TCP localport=22

REM Allow Ray ports through Windows Firewall:
netsh advfirewall firewall add rule name="Ray Port 6380" dir=in action=allow protocol=TCP localport=6380
netsh advfirewall firewall add rule name="Ray Dashboard Port 8265" dir=in action=allow protocol=TCP localport=8265
netsh advfirewall firewall add rule name="Ray Client Server Port 10001" dir=in action=allow protocol=TCP localport=10001

endlocal
