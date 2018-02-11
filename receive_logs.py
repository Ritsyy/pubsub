import etcd
import os
import sys
import time


class Subscriber(object):

    def __init__(self, queue, *args, **kwargs):
        # Or provide option for them to provide path to subscribe
        # TODO : make it configurable
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path = BASE_DIR + '/' + queue
        if not os.path.exists(path):
            os.makedirs(path)
        self.path = path
        self.client = etcd.Client(port=2379)
        super(Subscriber, self).__init__(*args, **kwargs)

    def on_receive(self):
        # subscribed message
        try:
            # read from directory here
            r = self.client.read(self.path, recursive=True, sorted=True)
            for child in r.children:
                # to prevent deleting from path
                if not child.key == self.path:
                    print("consumed message from {} : {}".format(child.key, child.value))
                    # delete message from queue after consumption
                    self.client.delete(child.key)
        except etcd.EtcdKeyNotFound:
            print 'key not found, waiting...'
        except etcd.EtcdNotFile as e:
            print 'exception occured while trying to delete, '
            print e
        time.sleep(1)
        print "waiting....."


if __name__ == '__main__':
    # first argument subscriber queue
    queue = sys.argv[1]
    subscriber = Subscriber(queue)
    while True:
        subscriber.on_receive()
