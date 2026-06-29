`np.array()`**:** You are modifying the _copy_. The original array outside the function remains unchanged.



`np.asarray()`**:** You are modifying the _original array_ directly in memory.





param = np.asarray(param, dtype=float) 

If you strictly want to keep the in-place update for memory efficiency, you need to tell NumPy to treat the inputs as floats right from the beginning, even if they look like integers.



**Option A: The Out-of-Place Update (Easiest)** Instead of forcing the new decimal values into the old integer array, just create a new array. Change your in-place subtraction (`-=`) to a standard subtraction:

Python

```
param = param - lr*(m_t/(v_t**0.5+eps))

```

_Why this works:_ Python will calculate the right side as floats, create a brand new float array, and point `param` to it. No type conflicts!