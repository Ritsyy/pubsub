# Pub Sub Interface


pubsub implemention with etcd 

### Publishing messge to a queue
- python emit_logs.py queue_name message
```
python emit_logs.py nodes helloWorld
```
#### To see the message in the reciever
- python receive_logs.py queue_name
```
python recieve_logs.py nodes
```
# Installation

  - install etcd using https://github.com/coreos/etcd/releases/
  - install python etcd client using
  ```sh
$ pip install python-etcd
```