   def last_n_items(items, n):
       """Return the last n items of a list."""
       result = []
       start = len(items) - n + 1
       for i in range(start, len(items)):
           result.append(items[i])
       return result


   numbers = [1, 2, 3, 4, 5]
   print(last_n_items(numbers, 3))  # expected: [3, 4, 5]
   print(last_n_items(numbers, 5))  # expected: [1, 2, 3, 4, 5]
