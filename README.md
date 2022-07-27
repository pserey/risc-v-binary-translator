# 32 bit RISC-V Binary/Hex Translator
A simple translator for getting 32 bit RISC-V assembly instructions from binary or hex machine code.

As it is an early version, it works as an interactive CLI. Firstly it asks for the instruction format (hex/bin), after that, it takes any binary or hexadecimal instruction code up to 32 bits and outputs the respective RISC-V instruction.

- Clone the repository
```
git clone https://github.com/pserey/risc-v-binary-translator
```
- Run conv.py
```
python conv.py
```
- Choose the instruction format (b/h)

![image](https://user-images.githubusercontent.com/65696885/181139143-5929aaa2-86d8-4eb0-b55c-f82b79115bc1.png)

- Input the instruction

![image](https://user-images.githubusercontent.com/65696885/181139215-d300d977-7671-4335-97af-c7690fb8510c.png)

- To exit the CLI, input 's'

All the information about binary RISC-V instruction set was taken from [this](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf) paper.

> Instruction format table

![image](https://user-images.githubusercontent.com/65696885/181085321-6515ab86-ca4e-4fcc-bbff-fb9a3b926e40.png)

> Instruction specific bit information table

![image](https://user-images.githubusercontent.com/65696885/181085437-a26e016a-012a-4d05-b157-fe626871cd50.png)
![image](https://user-images.githubusercontent.com/65696885/181085513-745cf123-110e-418b-991b-8700c133ce9f.png)
