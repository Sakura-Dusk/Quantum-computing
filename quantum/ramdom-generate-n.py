import pyqpanda as pq

def generate_random_bit_01():
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    
    q = machine.qAlloc_many(1)
    cbit = machine.cAlloc_many(1)
    
    prog = pq.QProg()

    prog.insert(pq.H(q[0]))

    prog.insert(pq.Measure(q[0], cbit[0]))
    
    result = pq.run_with_configuration(prog, 1)
    
    cbit_result = cbit[0].get_val()
    # if cbit_result is not None:
    #     print(f"{cbit_result}")
    # else:
    #     print("No measurement result found.")
    
    pq.destroy_quantum_machine(machine)

    return cbit_result

if __name__ == "__main__":
    n = int(input())
    k = 1
    num = 0
    while k < n:
        k = k * 2
        num = num + 1
    ans = n + 1
    while ans >= n:
        ans = 0
        now = 1
        for i in range(num):
            ans = ans + now * generate_random_bit_01()
            now = now * 2
    ans = ans + 1
    print(f"Random number between 1 and {n}: {ans}")