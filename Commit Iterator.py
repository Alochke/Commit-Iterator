"""
A simple python script,
that iterates branch BRANCH_NAME of repository f"{REPO_OWNER}/{REPO_NAME}"
and prints the 5 recent commit objects main information.
"""


from github import Github

# Fill those fields as see fit, will work only with public repos.
REPO_OWNER = "Alochke" # Repository-owner's Github username.
REPO_NAME =  "Workshop-in-InfoSec-assignment-2" # Name of the repository
BRANCH_NAME = "main" # Name of branch.

def print_commit_info(commit: str):
    """
    Print information about a Git commit.

    Parameters:
    - commit: str: A Git commit object containing information about the commit.

    Prints:
    - Commit SHA: The unique identifier of the commit.
    - Author: The name and email of the author who made the commit.
    - Date: The date and time when the commit was authored.
    - Message: The commit message describing the changes made.
    - A line of 50 dashes for visual separation.

    Example:
    >>> commit = get_latest_commit()  # Assuming a function to get the latest commit
    >>> print_commit_info(commit)
    Commit SHA: abcdef1234567890
    Author: John Doe <john.doe@example.com>
    Date: 2022-01-18 12:34:56
    Message: Updated documentation
    --------------------------------------------------
    """
    print(f"Commit SHA: {commit.sha}")
    print(f"Author: {commit.commit.author.name} <{commit.commit.author.email}>")
    print(f"Date: {commit.commit.author.date}")
    print(f"Message: {commit.commit.message}")
    print("-" * 50)

def main():

    g = Github()

    repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
    branch = repo.get_branch(BRANCH_NAME)
    commits = repo.get_commits(sha=branch.commit.sha)

    print(f"Recent commits for branch '{BRANCH_NAME}':")
    print("-" * 50)

    # Print information for the 5 most recent commits
    for commit in commits[:5]:
        print_commit_info(commit)

if __name__ == "__main__":
    main()
