# SSHmon
A SysAdmin tool to monitor all the SSH connections to a server

# How does it work ?

SSHmon listens for all incoming tty sessions and when a new ssh session is detected bashrc sends the Process ID of the tty session to a bash script via a web server which is not exposed to the internet but logging SSH sessions is not like using a key logger because when the keys are sent from the users computer they are encrypted so we had to listen to all the data coming to system calls because any information before going to the processor first goes through stdin so we get that data clean it and present it to the admin via a locally hosted website