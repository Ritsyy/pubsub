import etcd
import sys
import random
import os


class Publisher(object):

    def __init__(self, queue, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.path = BASE_DIR + '/' + queue
        import ipdb; ipdb.set_trace()
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        super(Publisher, self).__init__(*args, **kwargs)

    def publish(self, message):
        # publishes a message
        client = etcd.Client(port=2379)
        random_suffix = random.randint(1, 100)
        path = self.path + '/' + str(random_suffix)
        import ipdb; ipdb.set_trace()
        client.write(path, message)


if __name__ == '__main__':
    # first argument publisher queue
    # second argument message
    queue = sys.argv[1]
    message = sys.argv[2]
    print 'publishing from ', queue, ' Message : ', message
    publisher = Publisher(queue)
    publisher.publish(message)
