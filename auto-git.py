from datetime import datetime
import time
import sys
import os

AUTO_GIT_WAIT_TIME_SECOND = 30

def git_commit_push(repo_path : str, commit_message : str) -> None:

    sys.stdout.write(f"system INFO:\t start git process.\n\n")

    try:

        os.chdir(repo_path)
        os.system('git add .')
        os.system(f'git commit -m "{commit_message}"')
        os.system('git push origin main')
        
        sys.stdout.write("\n\nsystem OK:\t git commit & push successful!\n\n\n\n")

    except Exception as e:

        sys.stdout.write(f"system DETAIL:\t {e}\n\n\n\n")

    else:

        return

def main() -> None:

    git_repo_path = os.getcwd()

    times = 1

    while (True):

        current_time = datetime.now()
        commit_message = current_time.strftime("%Y/%m/%d %H:%M")

        sys.stdout.write(f"system INFO:\t auto git times become: {times} times\n")
        sys.stdout.write(f"system INFO:\t current time is: {commit_message}\n")

        git_commit_push(git_repo_path, commit_message)

        time.sleep(AUTO_GIT_WAIT_TIME_SECOND)
        times += 1

    # return

main()