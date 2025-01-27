'''
Created on Mar 27, 2015

@author: school
'''
from FifoQueue import FifoQueue


def create_queue_of_data(file_name):
    queue = FifoQueue()
    file = open(file_name, 'r')
    all_data = file.read()
    file.close()
    cleaned_data = filter(lambda x : len(x) > 0, all_data.split())
    for data in cleaned_data:
        queue.insert(data)
    return queue

def get_k_bits(queue, k = 2):
    ans = []
    for idx in range(0, k):
        if not queue.is_empty():
            ans.append(queue.get())
        else:
            break
    return ''.join(ans)

def list_to_string(xs):
    return ''.join(xs)
