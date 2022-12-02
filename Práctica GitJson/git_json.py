from git_leaks import *
import json
from git import Commit


def load_to_json(leaks: list[list]):
    '''Dada una lista llena de commits (provenientes de la práctica del bloque 1 
    git_leaks), los guarda en un archivo de formato .json

    Parameters
    leaks:
        lista cuyos elementos son a su vez listas de la forma [commit, repeticiones en el mensaje]
    
    Returns
    Nada, sólo crea el archivo json
    '''
    
    passwords = {'leaking_commits': []}
    for password in leaks:
        commit: Commit = password[0]
        commit_dict = {
                'author': commit.author.name,
                'commiter': commit.committer.name,
                'commited_date': commit.committed_date,
                'message': commit.message,
                'ocurrences': password[1]
                }
        passwords['leaking_commits'].append(commit_dict)

    with open("secrets.json", "w") as f_json:
        json.dump(passwords, fp=f_json, skipkeys=True, indent=3)


if __name__ == '__main__':

    commits = extract(REPO_DIR)
    passwords = transform(commits)
    load_to_json(passwords)
