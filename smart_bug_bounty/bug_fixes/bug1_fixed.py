def get_recent_transactions(transactions, count, history=None):
    """
    Returns the last `count` transactions and logs the query in `history`.
    """
    if history is None:
        history = []

    if count <= 0 or not transactions:
        return []

    history.append(f"Fetched {count} items")

    return transactions[-count:]


if __name__ == "__main__":
    txs = ["tx1", "tx2", "tx3", "tx4", "tx5"]
    assert get_recent_transactions(txs, 2) == ["tx4", "tx5"]
    assert get_recent_transactions(txs, 1) == ["tx5"]
    assert get_recent_transactions(txs, 10) == ["tx1", "tx2", "tx3", "tx4", "tx5"]
    assert get_recent_transactions(txs, 0) == []

    # Verify history is not shared across calls
    log1 = []
    get_recent_transactions(txs, 1, log1)
    log2 = []
    get_recent_transactions(txs, 2, log2)
    assert len(log1) == 1 and len(log2) == 1
    print("All bug1_fixed.py test cases passed!")
