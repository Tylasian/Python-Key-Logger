# Python-Key-Logger
Final Project for my Python class (CIS-30A) 

What problems are you solving in this project?
A key logger can be used in many ways… For example:
- Hackers can gather emails, usernames, passwords, bank details from a victim.
- Parents can monitor a child’s computer activities.
- Schools can monitor a student’s computer activities to make sure that the computer is being used appropriately.
- Workplaces can monitor an employee’s computer activities to make sure that the employee is on task during work hours. 
- Developers can use it to debug their programs. If an error/bug occurs, they can check to see if certain keyboard inputs caused it.

What solutions are you implementing in the project? 
- Usage of the library called “Pynput” gives me functions that allow me to easily listen for key presses and mouse movements.

Provide explanation of algorithm implementation.
- Pynput has a built-in function that seems to be a loop that is always checking for key presses. All I have to do is collect what it detects then feed it into a .txt file and check if the Esc key is pressed to stop the program.

What are the program objectives?
-Upon running the program, it should start listening for all keypresses from the keyboard and put it into a text file.

Explain how your program is interacting with the user and its purpose.
- User has to run the .py file through a text editor
- User can press the esc key to terminate the keylogger program.
- User can view the log.txt file to see their keypresses

What are the limitations of the program?
- User has to voluntarily activate the keylogger through running the .py file. Consequently, they can view the source code as well.
- User is aware that the keylogger is running.
- Data collected is saved locally on the user’s computer rather than sent to the attacker’s computer.
- Anti-Virus may detect and block it 

Provide recommendations on improving the limitations of the program.
- use pyinstaller library to easily convert the program into an executable.
- use winreg library to add the executable to the windows startup application registry so that it automatically runs on boot up (only works on Windows OS).
- Give the keylogger an inconspicuous name so that the user cannot easily identify it in the Task Manager.
- Import socket and socketserver to send data from client to attacker’s server over TCP.
