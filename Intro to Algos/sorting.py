def selection_sort(A, i=None):
    print(f"Selection Sort call with {i=}")
    print(f"A looks like {A}")
    if i is None: i = len(A) - 1
    
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i-1)

def prefix_max(A, i):
    print(f"call prefix_max with {i}, to return max of {A[:i+1]}")
    if i > 0:
        j = prefix_max(A, i-1)
        if A[i] < A[j]:
            print(f"call prefix_max with {i}, to return max of {A[:i+1]} and returns {j}, {A[j]}")
            return j
    print(f"call prefix_max with {i}, to return max of {A[:i+1]} and returns {i}, {A[i]}")
    return i


if __name__ == "__main__":
    A = [1, 3, 2, 5, 4]
    selection_sort(A)