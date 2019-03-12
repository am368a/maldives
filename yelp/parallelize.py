'''Simple interface for parallelization
'''

from multiprocessing import Pool

def run(func, fnames, nprocesses=None, timeout=10000):
    '''Run function func for each file name in fnames.
    nprocesses defines the number of parallel processes.
    returns the list of results obtained for each file name.
    
    If nprocesses is None or equal to 1, 
    the processing is interactive.
    '''
    results = []
    if nprocesses and nprocesses>1:
        with Pool(processes=nprocesses) as pool:
            tmp = []
            for fname in fnames: 
                tmp.append( pool.apply_async(func, [fname]) )
            for res in tmp: 
                print('getting result')
                results.append(res.get(timeout=timeout))
    else: 
        for fname in fnames: 
            results.append(func(fname))
    return results