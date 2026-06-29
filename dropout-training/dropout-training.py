import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """

    x = np.asarray(x, dtype=float)
    
    if rng:
        random_ = rng.random(x.shape)
    else:
        random_ = np.random.random(x.shape)

    survivors = random_>=p #mask
    scale = 1.0/(1.0-p)
    dropout_pattern = survivors*scale

    return x*dropout_pattern, dropout_pattern