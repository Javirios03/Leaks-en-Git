# !user/bin/python3
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
from git import Repo
import signal, sys, re


def handler_signal(signal, frame):
    print("\n\n [!] out ..........\n")
    sys.exit(1)


# Control-c
signal.signal(signal.SIGINT, handler_signal)

REPO_DIR = "./skale/skale-manager"

def extract(url: str) -> list:
    repo = Repo(url)
    commits = repo.iter_commits()
    return list(commits)

def transform(commits: list):
    sol = []
    patron = 'password|credentials|Password|Credentials|identification|Identification|key|Key'
    for commit in commits:
        passwords = re.findall(patron, commit.message)
        sol.append([commit, passwords]) if passwords != [] else None
    return sol

def load(passwords: list):
    with open("passwords.txt", "w") as f:
        for password in passwords:
            f.write(f">>{password[0].message}")

if __name__ == "__main__":
    commits = extract(REPO_DIR)
    passwords = transform(commits) 
    load(passwords)