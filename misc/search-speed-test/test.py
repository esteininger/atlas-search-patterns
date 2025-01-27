# test
import lorem
import sys
from settings import db
import math
from time import time

client = db['test'].speed_test


def bytes_to_mb(size_bytes):
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def size_limit():
    t = lorem.text()

    # this is ~ 12mb of text
    number_of_times = 9000

    str = ''
    for i in range(0, number_of_times):
        str += lorem.text()

    str_size = sys.getsizeof(str)
    print(bytes_to_mb(str_size))

    doc = {'key': str}

    client.insert_one(doc)
    print('inserted')


def query():
    # we're hiding the massive key we made earlier
    # this will reduce the results however since payload
    # size is smaller, but for the sake of being an eyesore
    pipe = [
        {
            '$search': {
                'index': 'large_doc_test',
                'text': {
                    'query': 'magnam',
                    'path': 'key'
                }
            }
        }, {
            '$project': {
                'key': 0
            }
        }
    ]
    return list(client.aggregate(pipe))


if __name__ == '__main__':
    # clear
    # client.delete_many({})
    # print('deleting')
    # insert
    size_limit()
    # start
    start = time()
    print(f"timer started")
    # query
    print('querying...')
    print(query())
    # finish
    end = time()
    print(f"timer ended")
    elapsed = end - start
    print(f"elapsed time: {elapsed}")
