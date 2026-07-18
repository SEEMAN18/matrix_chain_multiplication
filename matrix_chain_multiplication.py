# ---------------- Matrix Chain Multiplication ----------------

def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming

    Time Complexity  : O(n^3)
    Space Complexity : O(n^2)

    dims[i-1] x dims[i] represents the dimensions of matrix Ai.
    """

    n = len(dims) - 1

    # Cost table
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # Split table
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            m[i][j] = float("inf")

            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


# ---------------- Print Optimal Parenthesization ----------------
def print_optimal_parens(s, i, j):

    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} x {right})"


# ---------------- Print DP Table ----------------
def print_dp_table(m, n):

    print("\nDP Cost Table\n")

    print(f'{"":<6}', end="")

    for j in range(1, n + 1):
        print(f'A{j:<10}', end="")

    print()

    for i in range(1, n + 1):

        print(f'A{i:<5}', end="")

        for j in range(1, n + 1):

            if j < i:
                print(f'{"---":<12}', end="")
            else:
                print(f'{m[i][j]:<12}', end="")

        print()


# ---------------- Example ----------------

dims = [10, 30, 5, 60, 10]

n = len(dims) - 1

print("Matrix Dimensions")

for i in range(n):
    print(f"A{i+1} : {dims[i]} x {dims[i+1]}")

m, s = matrix_chain_order(dims)

print("\nMinimum Scalar Multiplications :", m[1][n])

print("Optimal Parenthesization :", print_optimal_parens(s, 1, n))

print_dp_table(m, n)