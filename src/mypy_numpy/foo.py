import numpy as np


def foo(a: np.ndarray, b: dict[str, complex]) -> np.ndarray:
    for k, v in b.items():
        v += np.trace(a)

    return np.sqrt(a)
