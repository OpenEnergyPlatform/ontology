## Development

### Prerequisites

- [Git](https://git-scm.com/)

### Contribution of OEO content
Please read [OEO wiki](https://github.com/OpenEnergyPlatform/ontology/wiki/Best-Practice-Principles) carefully.

### Workflow

The development of a feature for this repository is inspired from the workflow described 
by [Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/):

1. Create [an issue](https://help.github.com/en/articles/creating-an-issue) on the github repository

    Choose the right issue for you among the choices you have on github:

    A) Including a new term to the ontology. Only 1 new term (with a few subclasses, if at all)
    
    B) Restructuring existing parts of the ontology

    C) Other issue

    Discussion about the implementation details should occur within this issue. [Assign a project](https://help.github.com/en/github/managing-your-work-on-github/adding-issues-and-pull-requests-to-a-project-board#adding-issues-and-pull-requests-to-a-project-board-from-the-sidebar) (default "Issues") to the issue

2. Create a branch from `dev` to work on your issue (see below, the "Branch name convention" section)

    **Important**: If you are working on an issue of type A), please discuss with someone else within the issue thread **before** starting to work on a solution on your own

    Checkout the latest stand of `dev`
    ```bash
    git checkout dev
    ```
    ```bash
    git pull
    ```
    Branch from `dev`
    ```bash
    git checkout -b feature/myfeature
    ```
    As all need to edit the same `oeo.omn` file, it is better to merge one changes as fast *as possible* (i.e. do not wait for 6 months) to avoid merging conflicts
3. Open [protégé](https://protege.stanford.edu/) and work on the ontology

    One can also edit the `oeo.omn` file in a text editor
4. Before committing your changes, open the `oeo.omn` file with protégé and save the file from protégé. You should also check if you included unconsistencies by following [this ontology test procedure](https://github.com/OpenEnergyPlatform/ontology/wiki/ontology-test-guide)

    See the "Conventions" section below for commit messages format tips
5. Push your local branch on the remote server `origin`
    ```bash
    git push
    ```
    If your branch does not exist on the remote server yet, git will provide you with instructions, simply follow them
6. Submit a pull request (PR)
    - Follow the [steps](https://help.github.com/en/articles/creating-a-pull-request) of the github help to create the PR.
    - Please note that you PR should be directed from your branch (for example `myfeature`) towards the branch `dev`
7. Describe briefly (i.e. in one or two lines) what you changed in the `CHANGELOG.md` file. End the description by the number in parenthesis `(#<your PR number>)`
8. Commit the changes to the `CHANGELOG.md` file
9. Write the PR number in the corresponding issue so that they are linked. Write it with one of the [special keywords](https://help.github.com/en/github/managing-your-work-on-github/closing-issues-using-keywords) so that the issue will be automatically closed when the PR is merged (example: `Closes #<your issue number>`)
10. [Ask](https://help.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users) for review of your PR 
 
    A) If including new terms to the ontology, ask at least two persons to review
    
    B) If restructuring the ontology, one person is enough, though two is better
    
    C) If your PR does not modify the ontology, only one reviewer is enough

11. Check that, after this whole process, you branch does not have conflict with `dev` (github prevents you to merge if there are conflicts). In case of conflicts you are responsible to fix them on your branch before your merge (see below "Fixing merge conflicts" section)
    
12. (if approved) Merge the PR into `dev` and delete the branch on which you were working. In the merge message on github, you can notify people who are currently working on other branches that you just merged into `dev`, so they know they have to check for potential conflicts with `dev`
   
   
### Fixing merge conflicts


Avoid large merge conflict by merging the updated `dev` versions in your branch.

In case of conflicts between your branch and `dev` you must solve them locally.

1. Get the latest version of `dev`
    ```bash
    git checkout dev
    ```
   
    ```bash
    git pull
    ```
    
2. Switch to your branch

    ```bash
    git checkout <your branch>
    ```
    
3. Merge `dev` into your branch
    ```bash
    git merge dev
    ```
    
4. The conflicts have to be [manually](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line) resolved
    

### Conventions
The convention is to always have `feature/` in the branch name. The `myfeature` part should describe shortly what the feature is about (separate words with `_` or `-`). Is it also nice to end the branch name with the issue number it linked to:

Examples of branch names : `feature/solving-duplicate-problems-#11` or `feature/add_ontology_new_class_#43`

If the branch purpose is to fix a problem `feature/` can be replaced by `fix/`

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
