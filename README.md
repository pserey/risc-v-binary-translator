# 32 bit RISC-V Binary/Hex Translator
A simple translator for getting 32 bit RISC-V assembly instructions from binary or hex machine code.

As it is an early version, it works as an interactive CLI. Firstly it asks for the instruction format (hex/bin), after that, it takes any binary or hexadecimal instruction code up to 32 bits and outputs the respective RISC-V instruction.

All the information about binary RISC-V instruction set was taken from [this](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf) paper.

> Instruction format table

![image](https://user-images.githubusercontent.com/65696885/181085321-6515ab86-ca4e-4fcc-bbff-fb9a3b926e40.png)

> Instruction specific bit information table

![image](https://user-images.githubusercontent.com/65696885/181085437-a26e016a-012a-4d05-b157-fe626871cd50.png)
![image](https://user-images.githubusercontent.com/65696885/181085513-745cf123-110e-418b-991b-8700c133ce9f.png)
