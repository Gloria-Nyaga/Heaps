# HEAPS
HEAP- this is a binary tree data structure that satisfies the heap property that the value of each node is greater than or equal to the value of its children.
Max-Heap: Tracks the maximum values in a data set. Parent node is greater than or equal to the children node.
Min-Heap: Tracks the minimum values in a data set. Parent node is less than or equal to the children node.

 Advantage
1. Efficient Insertion and deletion of elements.
2. Space efficient - requires less memory.
3. Allows access to highest priority element.
4. Guarantees access to max and min elements.

Disadvantage
1. Lacks flexibility.
2. It takes more time to compute.
3. It takes much time to execute.
4. Memory management is more complicated and error-prone. 

Properties
1. Structural: Each node in a heap must have a value.
2. Parent should either be less than or equal to its children (min-heap) or parent should be greater than or equal to its children(max-heap).
3. Implementation:  Heaps are usually implemented in an array.
4. It is complete.

Application
1. Allows efficient access to highest priority task.
2. Priority queues: It implements priority queues based on their priority.
3. Used in graph algorithms due to its efficiency.
4. Job Scheduling: It schedules task based of urgency. 
5. Memory Management: It is used to store, manage and allocate memory blocks to programs as needed.

Accessing Items in a Heap 
1. Adding Items in a heap
2. Increase the heap size by one to store a new element.
3. Insert the new element at the end of the heap.
4. Analyze the heap property since new elements can affect the sequence.
5. Apply the heapify method to create a proper heap.

Removing Items in a heap
1. Replace the element to be removed by the last rightmost element in the heap.
2. Delete the last element from the heap.
3. Check if the heap is following the property of the heap or not. 
4. Apply the heapify method to create a proper heap.


# TUPLES
Tuple - It is a built-in data structure  that consists of immutable ordered set of values that store multiple data types.

PROPERTIES OF A TUPLE

1. Ordered 
 - Its elements always remain in their positions.
 - It does not change its order every time it’s called.

2. They are Immutable
 - Once the value is assigned, it can neither be modified or deleted.

3. It can hold duplicates
 - It allows multiple combinations of data types.


ADVANTAGES OF A TUPPLE

1. It is faster than lists.
2. It can be used as dictionary keys is it contains immutable values like strings, numbers or  another tuple.
3. They use less memory.
4. Processing a tuple is faster.


DISADVANTAGES

1. They are immutable.
- One cannot delete or add an element in a tuple.
2. They are less flexible than lists.
3. You can’t sort a tuple.
4. You cannot replace an element in a tuple one has to convert it to a list first.




