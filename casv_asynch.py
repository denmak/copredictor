import datetime
from multiprocessing.dummy import Pool as ThreadPool
from casv_utils import timethis


pool = ThreadPool(6)

@timethis
def executor(url):
    print(url, ' started...')
    result = urllib.request.urlopen(url)
    print(url, ' done')
    return result


@timethis
def executeAsynch(executor,params):
    # Open the urls in their own threads
    # and return the results
    results = pool.map(executor, params)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()


@timethis
def executeSynch(executor,params):
    results = []
    for url in params:
        result = executor(url)
        results.append(result)
