from prettytable import  PrettyTable
import sys

def readNEA():
    alphabet = input("Please input alphabet in form x,y,z:\n").replace(" ","").rstrip(',').split(',')
    states = input("Please input states in form x,y,z:\n").replace(" ","").rstrip(',').split(',')
    print("Transition function")
    transitions=[]
    for state in states:
        line=[]
        for symbol in alphabet:
            verifier = False
            tempInput = ''
            while not verifier:
                verifier = True
                tempInput = input(f"Please input target states, from {state} at {symbol} in form x,y,z:\n").replace(" ","").rstrip(',').split(',')
                for target in tempInput:
                    if target not in states and target!='':
                        verifier=False
                        print(f"{target} is not a recognized state")
            line.append(tempInput)
        transitions.append(line)
    return [alphabet,states,transitions]

def printAutomaton(automaton): #automaton = [alphabet,states,transition]
    alphabet = automaton[0]
    states = automaton[1]
    transitions = automaton[2]
    table = PrettyTable()
    table.field_names = [""] + alphabet
    for i in range(len(states)):
        row = [states[i]]
        for symbol in transitions[i]:
            row.append(','.join(symbol))
        table.add_row(row)
    print(table)

def convertAutomaton(automaton):
    alphabet = automaton[0]
    states = automaton[1]
    transitions = automaton[2]
    new_states= [states[0]]
    new_transitions = []
    iterator = 0
    while iterator < len(new_states):
        transitionLine = []
        for i in range(len(alphabet)):
            transition = []
            for state in new_states[iterator].split(','):
                oldStateNumber=-1
                for old_state in range(len(states)):
                    if states[old_state]==state:
                        oldStateNumber=old_state
                        break
                assert oldStateNumber!=-1,(f"{state} not found.")
                if transitions[oldStateNumber][i][0] is not '':
                    transition.extend(transitions[oldStateNumber][i])
            transition = list(dict.fromkeys(transition))
            if len(transition)==0:
                transition.append('')
            elif ','.join(transition) not in new_states:
                new_states.append(','.join(transition))

            transitionLine.append(transition)
        new_transitions.append(transitionLine)
        iterator+=1
    return [alphabet,new_states,new_transitions]

def main():
    if len(sys.argv)==1 or sys.argv[1] == 0:
        NEA = readNEA()
    elif sys.argv[1] == '1':
        NEA = [['0', '1'], ['q0', 'q1'], [[['q0'], ['q0','q1']], [[''], ['']]]]
    elif sys.argv[1] == '2':
        NEA = [['0', '1'], ['q0', 'q1', 'q2', 'q3', 'q4'], [[['q4'], ['q1']], \
        [['q1', 'q2'], ['q1']], [['q3'], ['']], [['q4'], ['']], [['q4'], ['q1']]]]
    elif sys.argv[1] == '3':
        NEA = [['a', 'b'], ['q0', 'q1', 'q2', 'q3', 'q4'], [[['q1', 'q2'], \
        ['']], [['q4'], ['']], [['q3'], ['q2']], [[''], ['']], [['q1'], ['']]]]
    else:
        NEA= readNEA()

    # NEA = [['0', '1'], ['q0', 'q1'], [[['q0'], ['q0','q1']], [[''], ['']]]]
    # NEA = [['0', '1'], ['q0', 'q1', 'q2', 'q3', 'q4'], [[['q4'], ['q1']], \
    # [['q1', 'q2'], ['q1']], [['q3'], ['']], [['q4'], ['']], [['q4'], ['q1']]]]
    printAutomaton(NEA)
    DEA = convertAutomaton(NEA)
    printAutomaton(DEA)


if __name__ == '__main__':
    main()
