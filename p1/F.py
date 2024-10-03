def get_registers():
    registers = []

    instructions = input().split()
    while instructions[0] != '#':
        q_num = int(instructions[1])
        period = int(instructions[2])

        registers.append([period, period, q_num])
        instructions = input().split()
    
    return registers

def print_tasks(tasks, registers):
    for _ in range(tasks):
        # reorganiza com base no tempo(passado + período) e no id da query
        registers.sort(key = lambda x: (x[0], x[2]))
        past, period, q_num = registers.pop(0)
        registers.append([past + period, period, q_num])
        
        print(q_num)


registers = get_registers()

tasks = int(input())
print_tasks(tasks, registers)
