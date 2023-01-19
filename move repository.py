import shutil
import os
import subprocess
import stat
from time import sleep


githubLink = ""
gitlabLink = ""
githubFolder = "github"
gitlabFolder = "gitlab"
alias = "origin"
branch = 'master'
commit = "Manager and consumer api"
gitName = ""
gitEmail = ""


def pull_repo(githubLink1, gitlabLink1, githubFolder1, gitlabFolder1, branch1):
    p1 = subprocess.Popen(
        f'git clone  -b {branch1}  {githubLink1} {githubFolder1}')
    p1.wait()
    p2 = subprocess.Popen(
        f'git clone  -b {branch1}  {gitlabLink1} {gitlabFolder1}')
    p2.wait()
    return


def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)
    return


def move_files():
    sleep(1)
    shutil.rmtree(f'{githubFolder}/.git', onerror=remove_readonly)
    shutil.move(f'{gitlabFolder}/.git', f'{githubFolder}')
    return


def set_git_config(gitName1, gitEmail1):
    p1 = subprocess.Popen(
        f'git config user.name "{gitName1}"', cwd="github")
    p1.wait()
    p2 = subprocess.Popen(f'git config user.email "{gitEmail1}"', cwd="github")
    p2.wait()
    return


def push_repo(commit1, alias1, branch1):
    p0 = subprocess.Popen(f'git checkout {branch1}', cwd="github")
    p0.wait()
    p1 = subprocess.Popen(
        f'git add .', cwd="github")
    p1.wait()
    p2 = subprocess.Popen(f'git commit -m "{commit1}"', cwd="github")
    print(f"git commit -m '{commit1}'")
    p2.wait()
    p3 = subprocess.Popen(
        f'git push -u {alias1} {branch1}', cwd="github")
    p3.wait()
    return


def remove_folder():
    shutil.rmtree(gitlabFolder, onerror=remove_readonly)
    shutil.rmtree(githubFolder, onerror=remove_readonly)
    return


pull_repo(githubLink, gitlabLink, githubFolder, gitlabFolder, branch)
move_files()
set_git_config(gitName, gitEmail)
push_repo(commit, alias, branch)
remove_folder()
