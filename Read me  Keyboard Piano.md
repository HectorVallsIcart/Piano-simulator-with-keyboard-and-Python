# Piano-simulator-with-keyboard-and-Python
# Python Keyboard Piano 

This project is a **simple piano simulator** that allows you to play musical notes using your computer keyboard.

## Assigned Keys

- **A** → C  
- **S** → D  
- **D** → E  
- **F** → F  
- **G** → G  
- **H** → A  
- **J** → B  

## How it works

- The program detects when a key is pressed and plays the corresponding note using `winsound.Beep()`.  
- When you release the key, it stops the sound (internal key state tracked with a dictionary).  

## Usage & Note

Save the file as `keyboard_piano.py` and run it with `python keyboard_piano.py`. Press **A, S, D, F, G, H, J** to play notes. This project only works on **Windows**, as `winsound` is Windows-specific.  

## Requirements

- Python 3  
- Modules: `keyboard`, `winsound`  

```bash
pip install keyboard
