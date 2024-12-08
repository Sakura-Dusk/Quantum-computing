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
    if cbit_result is not None:
        print(f"Measurement result (0 or 1): {cbit_result}")
    else:
        print("No measurement result found.")
    
    pq.destroy_quantum_machine(machine)

if __name__ == "__main__":
    generate_random_bit_01()