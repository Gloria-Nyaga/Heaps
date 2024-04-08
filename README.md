# Heaps
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
