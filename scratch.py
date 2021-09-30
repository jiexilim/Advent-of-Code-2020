import copy


class Instruction:
    def __init__(self, input):
        parsed = input.strip().split(" ")
        self.type = parsed[0]
        self.number = int(parsed[1])
        self.done = False
    
    def __repr__(self):
        return self.type + ": " + str(self.number)


class Run:
    def __init__(self, instructions, endAtEnd):
        self.acc = 0
        self.instruction_number = 0
        self.instructions = instructions
        self.endAtEnd = endAtEnd
    
    def done(self, instruction):
        if self.endAtEnd and self.instruction_number == len(self.instructions) - 1:
            return True
        return instruction.done is True
    
    def run(self):
        instruction = self.instructions[self.instruction_number]
        while not self.done(instruction):
            if instruction.type == "nop":
                self.instruction_number += 1
            elif instruction.type == "acc":
                self.acc += instruction.number
                self.instruction_number += 1
            elif instruction.type == "jmp":
                self.instruction_number += instruction.number
            else:
                raise Exception()
            
            instruction.done = True
            instruction = self.instructions[self.instruction_number]
        return self.acc, self.instruction_number


original_instructions = []
with open("Day8.txt") as file:
    for command in file.readlines():
        inst = Instruction(command)
        original_instructions.append(inst)

print(Run(copy.deepcopy(original_instructions), False).run())

for i in range(len(original_instructions)):
    instruction = original_instructions[i]
    if instruction.type == "acc":
        continue
    tmp_instructions = copy.deepcopy(original_instructions)
    if instruction.type == "nop":
        tmp_instructions[i].type = "jmp"
    elif instruction.type == "jmp":
        tmp_instructions[i].type = "nop"
    res = Run(tmp_instructions, True).run()
    if res[1] == len(original_instructions) - 1:
        print(res)