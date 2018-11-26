import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''This function generates the interest rate or vector of interest rates'''
    ''' Firstly, check the type of inputs '''
    if type(K) != int and type(K) != float and type(K) != np.ndarray:
        raise TypeError('K should be a scalar or vector.')
    if type(L) != int and type(L) != float and type(L) != np.ndarray:
        raise TypeError('L should be a scalar or vector.')
    if type(alpha) != float or type(delta) != float:
        raise TypeError('Both alpha and delta should be float.')
    if type(Z) != int and type(Z) != float:
        raise TypeError('Z should be a integer or float.')

    '''Then, check the value of inputs'''
    if (type(K) != np.ndarray and K <= 0) or (type(K) == np.ndarray and not np.all(K > 0)):
        raise ValueError("K should be larger than zero")
    if (type(L) != np.ndarray and L <= 0) or (type(L) == np.ndarray and not np.all(L > 0)):
        raise ValueError("L should be larger than zero")
    if not 0 < alpha < 1:
        raise ValueError("Alpha should in the interval of (0,1).")
    if not Z > 0:
        raise ValueError("Z should be larger than zero")
    if not 0 <= delta < 1:
        raise ValueError("Delta should in the interval of (0,1).")
    
    '''Finally, make sure the length of K and L are the same'''
    if type(K) == np.ndarray and type(L) == np.ndarray:
    	assert len(K) == len(L)

    ''' If the input meet all restrictions, then do the following calculation.'''
    r = alpha * Z * (L / K) ** (1 - alpha) - delta
    return r