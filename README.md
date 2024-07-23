# Binary Search Algorithm
**Introduction**

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the search continues in the lower half, or if the value is greater, in the upper half, until the value is found or the interval is empty.

**Time Complexity**

Best Case: O(1) - The key is found at the middle index on the first try.
Average Case: O(log n) - The search space is halved with each step.
Worst Case: O(log n) - The key is either not present or at the last position to be checked.
Here, n is the number of elements in the list.

**Code Explanation**

**Function Definition:**

The binarySearch function takes four parameters: arr (a sorted list of integers), start (the starting index of the list), end (the ending index of the list), and key (the integer to search for).

**While Loop:**

The loop continues as long as start is less than or equal to end.

**Calculate Midpoint:**

The midpoint mid is calculated using the formula start + ((end - start) / 2), ensuring it avoids overflow.

**Check Midpoint:**

* If arr[mid] is equal to key, the function returns the index of mid.
* If arr[mid] is greater than key, the search continues in the lower half by updating end to mid - 1.
* If arr[mid] is less than key, the search continues in the upper half by updating start to mid + 1.

**Key Not Found:**

If the loop completes without finding key, the function returns "Element not found".

**User Input:**
* The user is prompted to enter the elements of the list as a space-separated string. This input is converted to a list of integers using map and list.
* The user is then prompted to enter the key to search for.

**Function Call and Result:**

* The binarySearch function is called with the user-provided list, starting index, ending index, and key.
* The result of the search (index of the key or "Element not found") is printed to the console.

**Usage**
* Run the code.
* Enter the elements of the list when prompted. Separate each element with a space. Ensure the list is sorted for binary search to work correctly.
* Enter the key to search for.
* The program will output the index of the key if it is found in the list or "Element not found" if the key is not present in the list.
