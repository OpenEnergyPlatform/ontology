## Development

### Prerequisites

- [Git](https://git-scm.com/)


### Philosophy

The development of a feature for this repository is inspired from the workflow described 
by [Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/):

1. Create [an issue](https://help.github.com/en/articles/creating-an-issue) on the github repository to describe the addition to the ontology. Discussion about the implementation details should occur within this issue 
2. Create a branch from dev to work on your issue (see below, the "Branch name convention" section)
    ```bash
    git checkout -b feature/myfeature dev
    ```
    As all need to edit the same `oeo.omn` file, it is better to merge one additions as fast as possible to avoid merging conflicts. 
    Therefore, it is best to create a pull request and merge it at the end of each work session if the ontology changed much.
    This is different from a more conventional workflow where each issue is linked to only one pull request
3. Open [protégé](https://protege.stanford.edu/) and work on the ontology
    Please refrain from editing the `oeo.omn` file in a text editor. 
    If you do so, open protégé and check that the nodes which you modified do not have any problems
4. Describe briefly what you changed in the `CHANGELOG.md` file and commit the file last
5. Push your local branch on the remote server `origin`
    ```bash
    git push
    ```
    If your branch does not exist on the remote server yet, git will provide you with instructions, simply follow them
6. Submit a pull request (PR)
    Follow the [steps](https://help.github.com/en/articles/creating-a-pull-request) of the github help to create the PR
    Please note that you PR should be directed from your branch (for example `myfeature`) towards the branch `dev`
7. [Ask someone](https://help.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users) to review your PR 
8. Write the PR number in the corresponding issue so that they are linked
9. (if approved) Merge the PR into `dev` and delete the branch on which you were working
    

### Branch name convention
The convention is to always have `feature/` in the branch name. The `myfeature` part should describe shortly what the feature is about (separate words with `_`).

Try to follow [these conventions](https://chris.beams.io/posts/git-commit) for commit messages:
- Keep the subject line [short](https://chris.beams.io/posts/git-commit/#limit-50) (i.e. do not commit more than a few changes at the time)
- Use [imperative](https://chris.beams.io/posts/git-commit/#imperative) for commit messages 
- Do not end the commit message with a [period](https://chris.beams.io/posts/git-commit/#end) 
You can use 
```bash
git commit --amend
```
to edit the commit message of your latest commit (provided it is not already pushed on the remote server).
With `--amend` you can even add/modify changes to the commit.
