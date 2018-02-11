# Pub Sub Interface

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

Pub Sub interface using etcd to publish messages on the queue you want to send message through.

  - python emit_logs.py queue_name message
  - e.g python emit_logs.py nodes hellloWorld
  - To see the message in the reciever
  - python recieve_logs.py nodes

# Installation

  - install etcd using https://github.com/coreos/etcd/releases/
  - install python etcd client using
  ```sh
$ pip install python-etcd
```