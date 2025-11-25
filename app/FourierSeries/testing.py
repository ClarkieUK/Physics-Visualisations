import numpy as np

def get_series_representation(limit: int, scale: float):

    cos_coeffs = []
    sin_coeffs = []
    cos_freqs = []
    sin_freqs = []

    for n in range(1, limit + 1):
        
        cos_freqs.append(360 * (2 * n - 1))
        sin_freqs.append(360 * n)
        
        cos_coeffs.append(scale * 1 / (2 * n - 1))
        sin_coeffs.append(scale * (-(-1) ** n) / n)

    sin_phases = [0.0] * limit
    cos_phases = [np.pi / 2] * limit

    return {
        "sin_coeffs": sin_coeffs,
        "cos_coeffs": cos_coeffs,
        "sin_freqs": sin_freqs,
        "cos_freqs": cos_freqs,
        "sin_phases": sin_phases,
        "cos_phases": cos_phases,
    }
