# 32 bit RISC-V Binary/Hex Translator
A simple translator for getting 32 bit RISC-V assembly instructions from binary or hex machine code.

As it is an early version, it works as an interactive CLI with a Python script.

- Clone the repository
```
git clone https://github.com/pserey/risc-v-binary-translator
```
- Run conv.py
```
python conv.py
```
- Choose the the instruction reading mode (`i` for interactive `l` for .101 file reading)
- If .101 file reading is chosen, type the .101 file address
- If interactive is chosen, you can choose if the given instructions are in binary (b) or hexadecimal (x). 
- After that, you can input options that decide if constants in the code are printed as:
    - decimal (default = `Enter`)
    - hexadecimal (`'sx'`)
    - binary (`'sb'`)
- To exit the CLI, input `'s'`

All the information about binary RISC-V instruction set translation to binary was taken from [this](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf) paper.

> Instruction format table

![image](https://user-images.githubusercontent.com/65696885/181085321-6515ab86-ca4e-4fcc-bbff-fb9a3b926e40.png)

> Instruction specific bit information table

![image](https://user-images.githubusercontent.com/65696885/181085437-a26e016a-012a-4d05-b157-fe626871cd50.png)
![image](https://user-images.githubusercontent.com/65696885/181085513-745cf123-110e-418b-991b-8700c133ce9f.png)
