import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.asarray(param, dtype=float)
    grad = np.asarray(grad, dtype=float)
    m = np.asarray(m, dtype=float)
    v = np.asarray(v, dtype=float)
    
    m_ = beta1*m + (1.0-beta1)*grad
    v_ = beta2*v + (1.0-beta2)*grad**2
    m_t = m_/(1.0-beta1**t)
    v_t = v_/(1.0-beta2**t)
    param -= lr*(m_t/(v_t**0.5+eps))
    
    return param, m_, v_