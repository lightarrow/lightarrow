
def search(arr, n, x):
    """
    O(n)
    """
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


def run_search():
    arr = [2, 3, 4, 10, 40]
    x = 10
    n = len(arr)

    result = search(arr, n, x)
    if result == -1:
        print("not found")
    else:
        print("found")


run_search()
