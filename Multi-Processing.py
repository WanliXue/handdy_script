import multiprocessing
def worker(num):
    print(f'we got {num}')
    for i in range(num):
      print('worker:', i)

def another_w(num):
    print('another:', num)

if __name__ == '__main__':
    jobs = []


    # p = multiprocessing.Process(target=worker, args=(3,))
    # jobs.append(p)
    # p.start()
    #
    # p = multiprocessing.Process(target=another_w, args=("worker",))
    # jobs.append(p)
    # p.start()
    #
    # for i in jobs:
    #     i.join()



    for i in range(5):
        p = multiprocessing.Process(target=another_w, args=(i,))
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
print('Done')
#
# with open('README.md') as f:
#     print(f.readlines())