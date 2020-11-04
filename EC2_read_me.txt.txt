In EC2 instance, below script is called.
The "Hello to user data scripts" can be seen in system log during instance creation/login.

#! /bin/bash

echo $PATH > /tmp/output.txt
echo "Hello to user data scripts"






[ec2-user@ip-10-0-1-219 log]$ grep -i hello cloud-init-output.log
Hello to user data scripts

