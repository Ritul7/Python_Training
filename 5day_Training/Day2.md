# DAY 2 Notes:-

## 1. Terminal Basics 

- Powershell is object oriented shell and scripting language., as it is build on top of the .NET framework and handles data as structured objects.
- Command Prompt is command line interface program that uses text based inputs and outputs to interact with the computer through commands.
- Command Prompt is limited to Windows environment only, but Powershell works on Linux and MacOS as well.
- Technically, a terminal is a software that starts and connects to a Powershell.

## 2. Linux Basics

- Lovable Intellect Not Using XP
- Linux is an open-source OS, mainly used in AWS, CI/CD, DevOps.
- Linux distribution is nothing but the Linux OS. (Ex: Ubuntu)
- Linux doesn't requires any license to use unlike that of windows.
- File names are case-sensitive, which is completely opp from windows.
- More stable and uses (/) for directory seperation, windows uses (\).

### Linux Architecture:-
- Components: Hardware(Terminals, Disks), Kernel, Shell, Applications

1. Kernel - Manages hardware resources like memory management and process management. Controls communication between software and hardware.
2. Shell - A CLI for communication of users and OS through commands.
3. Hardware Layer - Consists of physical components like RAM, CPU, storage that executes the commands and provide resources to system.

## 3. File and Folder Operations:-

- Two files with the same names can't be created.
- cd, pwd, ls, dir, mkdir, rmdir, cp
- ls -la - List down the hidden files also
- rmdir - Only deletes empty directories
- touch - make empty files
- echo - inserting text into files
- rm - Delete files permanently
- rm -r - Deletes the folder and files inside it.
- rm -rf - Deletes the folder and files inside it even the protected ones.
- mv - Rename files or directories
- cat - Printing data of the file
- cp - Copy data from one file to another(overrites the exisiting data).
- cat file1 >> file2 - COpies the data of file1 into 2, without overwriting it.
- uname - Tells about OS
- locate - To search about particular file using database
- ps - Display running processes
- wget - To download files via url
- ps aux - Display all the running processes on the system
- kill - Signals are the messages sent to processes to manage their execution.
    -- SIGKILL (Signal no: 9) - Immediately terminate the process (forcefully).
    -- SIGTERM (SIgnal no: 15) - Gracefully terminate the process, allowing it to do the cleanup tasks before exiting,
    -- SIGCONT (Signal no: 18) - Continue a stopped process.
    -- SIGSTOP (Signal no: 19) - Pause or Stop a process. Like SIGKILL it can't be ignored.
- lsof -i :3000 - It shows which processes currently using port:3000

## 4. Process Management:-

- Creation, Scheduling, Controlling and Termination of the process.

- 1. Creation - Process is loaded into memory, assigned a PID and required resourcces like CPU time, files, memory.
- 2. Scheduling - CPU Scheduler inside OS decides which process to run, when to run and for how long. Various Scheduling algorithms are FCFS, SJF, Round-Robin. It allows multitasking.
- 3. Process goes from different states: Ready, Running, Waiting, Terminated
- 4. Context Switching - CPU switches from one process to another. 
- 5. Process Termination.

## 5. Environment Variables:-

- They are named values that OS provides to the program, describing about the environment that program runs in.

1. System Environment Variables:-
- 

## 6. Package Managers:-

- They are tools that helps developers to manage, install, update and remove packages(libraries) that their projects depends on.
- They handle dependencies automatically.
- They installs correct versions.

1. pip (Python Install Packages): It is used to manage python related packages whch are used in a python project. PyPI - Python Package Index (yha se libraries install krta h pip)
2. npm (Node Package Manager): It is used to install js libraries for js based projects ( frontend and backend both)
- 

## 7. Git Fundamentals and Version Control

- Git is a version control system which helps us to keep a track of different versions of our code on the platform called GitHub.
- Git is like, it takes the snapshot of all of our code everytime when we save the code(commit), keeping the history.

- Git uses command line to keep track of the codes and manage different versions of the code
- Basic git commands are:
1. git init - Initializes a git repository
2. git status - Gives us a status of which files are updated
3. git add. - It adds all the unstaged files on stage( it means they are done with the review and are ready to commit).
4. git commit -m "any message": This adds the latest version of the files
5. git push -u origin main: This pushes our committed files to the repo on the 'main' branch
6. git branch - It shows us on which branch we are
7. git branch -b "name" - New branch create hoti h