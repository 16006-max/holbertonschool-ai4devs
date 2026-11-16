def get_recent_transactions(transactions, count, history=[]):
    """
    Returns the last `count` transactions and logs the query in `history`.
    """
    if count <= 0:
        return []

    history.append(f"Fetched {count} items")

    # Bug 1: Off-by-one slicing error (misses the very last element)
    start_index = len(transactions) - count - 1
    if start_index < 0:
        start_index = 0

    return transactions[start_index:-1]


if __name__ == "__main__":
    txs = ["tx1", "tx2", "tx3", "tx4", "tx5"]
    print(get_recent_transactions(txs, 2))  # Expected: ['tx4', 'tx5']
    print(get_recent_transactions(txs, 1))  # Expected: ['tx5']
