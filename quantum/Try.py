import pyqpanda as pq
 
if __name__ == "__main__":
    # 初始化量子虚拟机
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    qubits = pq.qAlloc_many(4)
    cbits = pq.cAlloc_many(2)
    cbits[0].set_val(0)
    cbits[1].set_val(1)
    prog = pq.QProg()
    branch_true = pq.QProg()
    branch_false = pq.QProg()
 
    # 构建QIf正确分支以及错误分支
    branch_true.insert(pq.H(qubits[0])) \
        .insert(pq.H(qubits[1])) \
        .insert(pq.H(qubits[2])) \
        .insert(pq.H(qubits[3])) \
        .insert(pq.CZ(qubits[1], qubits[2])) \
        .insert(pq.RX(qubits[1], -1.570796)) \
        .insert(pq.RX(qubits[2], -1.570796)) \
        .insert(pq.CNOT(qubits[0], qubits[2]))
    branch_false.insert(pq.H(qubits[0]))
 
    # 构建QIf
    qif = pq.create_if_prog(cbits[0] < cbits[1], branch_true, branch_false)
 
    # QIf插入到量子程序中
    prog.insert(qif)
 
    # 概率测量
    result = pq.prob_run_dict(prog, qubits, -1)
 
    # 打印概率测量结果
    print(result)

    print(branch_true)
    print(branch_false)
 
    pq.destroy_quantum_machine(machine)