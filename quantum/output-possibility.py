import pyqpanda as pq

if __name__ == "__main__":
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    qubits = machine.qAlloc_many(3)
    prog = pq.create_empty_qprog()
    prog.insert(pq.H(qubits[0])) \
        .insert(pq.H(qubits[1])) \
        .insert(pq.CNOT(qubits[1], qubits[2]))
    result = pq.prob_run_dict(prog, qubits, -1)
    pq.destroy_quantum_machine(machine)
    for k in result:
        print(k+":"+str(result[k]))