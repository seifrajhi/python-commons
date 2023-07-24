def array_contains(needle, haystack):
    """
    Returns True if the given item (needle) is in the given array (haystack); returns False otherwise.
    """
    return needle in haystack

def array_split(separator, string):
    """
    Splits the given string into a list of elements based on the given separator.

    Examples:
    array_split(",", "a,b,c") -> ["a", "b", "c"]
    """
    return string.split(separator)

def array_join(separator, values):
    """
    Joins the elements of the given list into a string with the given separator between each element.

    Examples:
    array_join(",", ["A", "B", "C"]) -> "A,B,C"
    """
    return separator.join(values)

def array_prepend(prefix, array):
    """
    Adds the given prefix to the beginning of each element in the given list.

    Examples:
    array_prepend("P", ["a", "b", "c"]) -> ["Pa", "Pb", "Pc"]
    """
    return [prefix + item for item in array]

# Append an element to the end of the list
def array_append(array, element):
    """
    Appends the given element to the end of the list.

    Examples:
    array_append([1, 2, 3], 4) -> [1, 2, 3, 4]
    """
    array.append(element)

# Remove the first occurrence of the element from the list
def array_remove(array, element):
    """
    Removes the first occurrence of the given element from the list.

    Examples:
    array_remove([1, 2, 3, 4, 3], 3) -> [1, 2, 4, 3]
    """
    array.remove(element)

# Get the index of the first occurrence of the element in the list
def array_index(array, element):
    """
    Returns the index of the first occurrence of the given element in the list.

    Examples:
    array_index([10, 20, 30, 40, 20], 20) -> 1
    """
    return array.index(element)

# Sort the list in ascending order (in-place)
def array_sort(array):
    """
    Sorts the list in ascending order (in-place).

    Examples:
    array_sort([3, 1, 2]) -> [1, 2, 3]
    """
    array.sort()

# Reverse the elements of the list (in-place)
def array_reverse(array):
    """
    Reverses the order of elements in the list (in-place).

    Examples:
    array_reverse([1, 2, 3]) -> [3, 2, 1]
    """
    array.reverse()

# Count the number of occurrences of the element in the list
def array_count(array, element):
    """
    Returns the number of occurrences of the given element in the list.

    Examples:
    array_count([1, 2, 2, 3, 2], 2) -> 3
    """
    return array.count(element)

# Check if all elements in the list satisfy a condition
def array_all(array, condition):
    """
    Returns True if all elements in the list satisfy the given condition; False otherwise.

    Examples:
    array_all([1, 2, 3], lambda x: x > 0) -> True
    array_all([1, 2, -3], lambda x: x > 0) -> False
    """
    return all(condition(item) for item in array)

# Check if any element in the list satisfies a condition
def array_any(array, condition):
    """
    Returns True if any element in the list satisfies the given condition; False otherwise.

    Examples:
    array_any([1, 2, 3], lambda x: x < 0) -> False
    array_any([1, 2, -3], lambda x: x < 0) -> True
    """
    return any(condition(item) for item in array)
