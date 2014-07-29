sudo pip3 install kombu
sudo apt-get install rabbitmq-server
sudo rabbitmqctl add_user user 123456
sudo rabbitmqctl add_vhost host
sudo rabbitmqctl set_permissions -p host user '.*' '.*' '.*'
