import heapq


def process_operations(operations):
    heap = []
    result_operations = []

    for op in operations:
        parts = op.split()
        command = parts[0]

        if command == 'insert':
            value = int(parts[1])
            heapq.heappush(heap, value)
            result_operations.append(op)

        elif command == 'getMin':
            expected_min = int(parts[1])

            # Remove elements less than the expected minimum
            while heap and heap[0] < expected_min:
                heapq.heappop(heap)
                result_operations.append('removeMin')

            # If heap does not have the expected minimum, insert it
            if not heap or heap[0] > expected_min:
                heapq.heappush(heap, expected_min)
                result_operations.append(f'insert {expected_min}')

            result_operations.append(op)

        elif command == 'removeMin':
            if heap:
                heapq.heappop(heap)
                result_operations.append(op)
            else:
                # Add an element before removing if heap is empty
                result_operations.append('insert 0')
                result_operations.append(op)

    return result_operations


def main():
    # Read the number of operations
    n = int(input().strip())
    operations = []

    # Read each operation
    for _ in range(n):
        operations.append(input().strip())

    # Process the operations and generate the modified sequence of operations
    corrected_operations = process_operations(operations)

    # Output the number of operations and the operations themselves
    print(len(corrected_operations))
    for line in corrected_operations:
        print(line)


if __name__ == '__main__':
    main()
