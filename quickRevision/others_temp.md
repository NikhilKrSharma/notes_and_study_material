# OTHER USEFUL COMMANDS

# tmux
| **Command**                                | **Remark**                                      |
|--------------------------------------------|-------------------------------------------------|
| `tmux`                                     | Start a new Tmux session.                       |
| `tmux new -s session_name`                 | Start a new session with the specified name.    |
| `tmux attach -t session_name` <br> `tmux a -t session_name` | Attach to a specified session. |
| `tmux list-session[s]` <br> `tmux ls`      | List all Tmux sessions.                         |
| `tmux detach`                              | Detach from the current session (prefix + d).   |
| `tmux kill-session -t session_name`        | Kill the specified session.                     |
| `tmux rename-session -t old_name new_name` | Rename an existing session.                     |

<br>
<br>

# zip 
`zip -r -9 -e my_archive.zip my_folder`
- -q: Quiet mode; fewer output messages.  
- -9: Maximum compression.  
- -e: Encrypt the zip file with a password.

<br>
<br>

# Logging

| Command | Command	Description |
|---------------|---------------|
|`your_program \| tee output.log`      | Logs output to both the terminal and a file simultaneously. |
|`your_program > output.log`	       | Logs output to file (overwrites file) |
|`your_program >> output.log`	       | Logs output to file (appends to file) |
|`your_program &> output.log`	       | Logs both stdout and stderr to file |
|`your_program 2>&1	\| tee output.log` | Logs Both Standard Output and Error to terminal and a file simultaneously |


