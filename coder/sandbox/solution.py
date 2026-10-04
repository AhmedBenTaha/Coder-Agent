# solution.py
"""
Calculate the first 1,000,000 terms of the Leibniz series for pi:
    1 - 1/3 + 1/5 - 1/7 + ...
Multiply the sum by 4 and print the result.

The series converges slowly, but 1,000,000 terms give a decent approximation.
"""

def leibniz_pi_terms(n_terms: int) -> float:
    """Return 4 * sum_{k=0}^{n_terms-1} ((-1)**k) / (2*k + 1).

    Args:
        n_terms: Number of terms to include in the sum.
    """
    total = 0.0
    sign = 1.0
    denominator = 1.0
    for _ in range(n_terms):
        total += sign / denominator
        sign = -sign          # flip sign for next term
        denominator += 2.0   # next odd number
    return 4.0 * total

if __name__ == "__main__":
    N = 1_000_000
    result = leibniz_pi_terms(N)
    # Print with 15 decimal places, enough to see the approximation.
    print(f"Approximation of pi using {N:,} terms: {result:.15f}")
