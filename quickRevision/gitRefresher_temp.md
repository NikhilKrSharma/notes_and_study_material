# Git Refresher


## 1. Resources
[GIT Immersion](https://gitimmersion.com/lab_01.html)


## 2. Important Git Commands

### Configurations related
- git clone \<gitRepoURL>
- git config --list --show-origin
- git config --global user.name \<userName>
- git config --global user.email \<emialID>
- git config --global core.editor emacs
- git config --global http.sslVerify false
- git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
- git config --global http.postBuffer 524288000
- git config --global credential.helper osxkeychain [in case of password change on remote]
- git config --global http.version HTTP/2
- git config --global http.version HTTP/1
- git config --global pack.windowMemory "100m"
- git config --global pack.packSizeLimit "100m"
- git config --global pack.threads "1" 
- git config --global pack.deltaCacheSize "512m"

### Help related
git \<command> -h
git \<command> --help

### 2.2. Daily used commands
-  **git status** : show the working tree status
-  **git log** or **git history**: shows commit logs
-  **git diff** or **git diff HEAD** : show differences between your work and last commited version
-  **git add .** : stage all changes in current directory (add to staging area)
-  **git reset HEAD** : unstage all changes that are currently not committed
-  **git commit -m "commit message"** : make a new commit with given message
-  **git push origin master** : send local commits to remote repository
-  **git pull origin master** : get latest updates from remote repository
-  **git rm  \<file>** : remove file from source control
-  **git diff | git diff -- staged**  : compare files in working directory vs staged/indexed
-  **git rm --cached \<fileName>** : removes a file from the index, but keeps it in the working directory.
-  **git remote show origin** : Shows the remote URL of that particular git repo.


#### Branching & Merging [Come back and redo this section]
-  **git branch** : list branches, * indicates the current one
-  **git checkout -b newBranch** : create a new branch and switch to it
-  **git merge otherBranch** : combine code from another branch into the current one
-  **git branch -d oldBrach** : delete an old branch


#### Conflicts during merging
-  **git diff*** : see conflicts
  


#### Tracking and Visualising
-  git log
-  git log --stat
-  git log --pretty=oneline



