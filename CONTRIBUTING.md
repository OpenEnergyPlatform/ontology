<!--
SPDX-FileCopyrightText: Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology/>
SPDX-License-Identifier: CC0-1.0 OR MIT
-->

## Table of Contents

- [Welcome](#Welcome)<br>
    - [Prerequisites](#Prerequisites)<br>
- [Development](#development)<br>
    - [Getting Started](#getting-started)<br>
    - [Conventions for git and GitHub](#conventions-for-git-and-github)<br>
    - [Workflow](#workflow)<br>
        - [Communicate your Ideas or Concerns](#communicate-your-ideas-or-concerns)<br>
        - [Make Changes to the OEO](#make-changes-to-the-oeo)<br>
        - [Wait for Review of your Changes](#wait-for-review-of-your-changes)<br>
        - [Merge your Changes after Approval](#merge-your-changes-after-approval)<br>
    - [Fixing merge conflicts in git](#fixing-merge-conflicts-in-git)<br>
    - [Communicate](#communicate)<br>


## Welcome!

First of all, thank you for wanting to participate. Any new idea, any reported problem is helpful for the development and most appreciated. <br>
To get started quickly, there are some prerequisities that you need to fullfill. For a full tutorial, please check out the [Open Energy Academy Course](https://openenergyplatform.github.io/academy/courses/05_ontology/#how-to-become-an-oeo-developer).


### Prerequisites

- We are using [Git](https://git-scm.com/) for version management. [Git How To](https://githowto.com/) provides an introduction into working with Git. Also there is a helpful [Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf).
- We use [Protégé](https://protege.stanford.edu/) to edit the ontology. To get to know Protégé you can use the [Pizza Tutorial](https://www.michaeldebellis.com/post/new-protege-pizza-tutorial). <br> Please make sure you changed your Protégé settings to [numerical identifiers](https://github.com/OpenEnergyPlatform/ontology/wiki/Numerical-Identifiers) and got a [personal ID](https://github.com/OpenEnergyPlatform/ontology/wiki/Add-yourself-as-a-contributor) to add new classes.
- Every other Thursday (even weeks) an online [OEO developer meeting](https://github.com/OpenEnergyPlatform/ontology/wiki/oeo-dev-meeting-plan) takes place. Use the [OEP contact form](https://openenergyplatform.org/contact/) to gain access. 
- Before you change anything, get familiar with the [OEO Workflow](#workflow).

## Development

### Getting Started
Please read the [OEO best practices](https://github.com/OpenEnergyPlatform/ontology/wiki/Best-Practice-Principles) carefully. The following emojis are used in the text to help you identify the tool you are supposed to use for a specific workstep.

| Emoji ...                | ... symbolizes tool ... | ...which is used for ...                                   |
|:------------------------:|:-----------------------:| ---------------------------------------------------------- |
| 🔶 <br/>*orange diamond* | git                     | keeping code in sync between your PC and online-repository |
| 🐙 <br/>*octopus*        | github                  | discussions and reviews                                    |
| 📙 <br/>*orange book*    | protégé                 | changing the ontology                                      |
| 📝 <br/>*memo*           | text editor             | changing the ontology as well as other files               |

### Conventions for git and GitHub

🔶 Naming convention for branches

Follow the [best-practices for git branching naming convention](https://codingsight.com/git-branching-naming-convention-best-practices/).
The convention is `type`-`issue-nr`-`short-description`

**type**

* master / main / stable - includes the current stable version
* dev - includes all current developments
* feature - includes the feature that will be implemented
* release - includes the current version to be released

The majority of the ontology development will be done in `feature` branches.

**issue-nr**

Add the issue number where you describe, discuss and document your development.

**short-description**

Describe shortly what the branch is about. Avoid descriptive names for branches that are either too short or too long, 2-4 words are optimal.

Other hints:
- Separate words with `-` (minus)
- Do not add your name to the branch name, it's a collaborative project
- Avoid using numbers only 
- Branch names should be precise and informative
- Avoid using capital letters

Examples of branch names : `feature-43-add-new-ontology-class` or `feature-711-branch-naming-convention`

🔶 Commit messages

Try to follow existing conventions for commit messages:
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- Keep the subject line [short](https://chris.beams.io/posts/git-commit/#limit-50) (i.e. do not commit more than a few changes at the time)
- Use [imperative](https://chris.beams.io/posts/git-commit/#imperative) for commit messages 
- Start with a [capital letter](https://chris.beams.io/posts/git-commit/#capitalize)
- Do not end the commit message with a [period](https://chris.beams.io/posts/git-commit/#end) 


You can use the command 
```bash
git commit --amend
```
to edit the commit message of your latest commit (provided it is not already pushed on the remote server). <br>
With `--amend` you can even add/modify changes to the commit.


### Workflow

The workflow for contributing to this project has been inspired by the workflow described 
by [Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/).

#### Communicate your Ideas or Concerns

1. 🐙 Create
   [an issue](https://help.github.com/en/articles/creating-an-issue) on
   the GitHub repository describing the problem and proposed solution.

    Choose the right issue type from among the available choices:

    A) Adding a new entity to the ontology. Ideally, each issue should correspond to only one new term (with only a few subclasses, if needed)
    
    B) Restructuring existing parts of the ontology

    C) Updating definitions of existing entities in the ontology

    D) Other issue

    [Assign a project](https://help.github.com/en/github/managing-your-work-on-github/adding-issues-and-pull-requests-to-a-project-board#adding-issues-and-pull-requests-to-a-project-board-from-the-sidebar) (default "Issues") to the issue

    Discussion about the implementation should take place within the issue. <br> <br>
    **Important**: Please discuss the proposal within the issue thread **before** starting to work on a solution. <br>
    For minor changes, which include small changes to improve clarity of definitions and the addition of clarifying annotations, at least one other person from the project team should agree to the proposed change before it is implemented. <br>
    For major changes, which include adding new entities and restructuring the ontology, at least two other members of the project team need to agree to the change before it is implemented, which should include at least one domain expert and at least one ontology expert. <br>
    Issues which are contentious, for which it is difficult to reach agreement, should be added to the agenda of the next ontology working group teleconference for discussion to reach agreement amongst the full working group. Subsequent to such discussion, the issue's first thread should be updated with a documented record of the conclusions reached.   

#### Make Changes To the OEO

2. 🔶 Once a solution has been agreed, create a branch from `dev` to work on your issue (see below, the ["Conventions for git and GitHub"](#conventions-for-git-and-github) section)

    Checkout the latest stand of `dev`
    ```bash
    git checkout dev
    ```
    ```bash
    git pull
    ```
    Branch from `dev` (see also section ["Conventions for git and GitHub"](#conventions-for-git-and-github) below)
    ```bash
    git checkout -b feature-issueNumber-myfeature
    ```
    It is best to merge one's changes *as fast as possible* (i.e. do not wait for 2 weeks) to avoid merging conflicts
3. 📙 or 📝 Open [Protégé](https://protege.stanford.edu/) (version 5.6.1) or a text editor and work on the ontology. If you haven't already, make sure you change your protégé settings to use [numeric identifiers](https://github.com/OpenEnergyPlatform/ontology/wiki/Numerical-Identifiers). Please choose the right module of the oeo to do your changes, oeo.omn is in most cases not the right file to change. Refer to [this article](https://github.com/OpenEnergyPlatform/ontology/wiki/how-to-use-prot%C3%A9g%C3%A9-to-change-the-ontology) for detailed explanations on working with protégé.

    One can also edit the files in a text editor
4. 📙 Before committing your changes, open the `oeo.omn` file with Protégé and save the file from Protégé. You should also check if you included inconsistencies by following [this ontology test procedure](https://github.com/OpenEnergyPlatform/ontology/wiki/ontology-test-guide)

    See the ["Conventions"](#conventions-for-git-and-github) section below for commit messages format tips
5. 🔶 Get your changes online
    
    stage the files you changed
    ```bash
    git add [file_name]
    ```

    **🔎 Quick Tip:** 
    Changes in `catalog.xml`-files do NOT have to be staged, UNLESS something in the file structure has changed (e.g. adding/rearranging files, [see 🔗](https://github.com/OpenEnergyPlatform/ontology/pull/1102#issuecomment-1090003565))

    commit your changes
    ```bash
    git commit [-m " <commit_message> "]
    ```

    push your branch to the remote server

    ```bash
    git push
    ```
    If your branch does not exist on the remote server yet, git will provide you with instructions, simply follow them. 
    
    **Hint:** You can create a draft pull request directly after your first commit 🐙, see 7). <br>
    Then you get the pull request number and 📙 implement the [term tracker annotations](https://github.com/OpenEnergyPlatform/ontology/wiki/Term-Tracker-Annotation) in Protégé. Only after finishing the implementations you can assign reviewers and thus change the state of the PR. Using that workflow, it is clear whether a PR is actually ready for review.
    
6. 🐙 Make sure that all automated tests are successful. This will be indicated by a green or red icon next to your most recent commit. In case an error occured that you don't know how to solve, write a comment in the PR and ask for help from the ontology-expert-team.

#### Wait for Review of your Changes

7. 🐙 Submit a pull request (PR)
    - Follow the [steps](https://help.github.com/en/articles/creating-a-pull-request) of the github help to create the PR.
    - Please note that your PR should be directed from your branch (for example `myfeature`) towards the branch `dev`
    - To make reviewing easier, briefly describe the changes you have made in the pull request and summarise the discussion and conclusions in the associated issue. 
    - Write the corresponding issue number in the pull request so that they are linked. Write it with one of the [special keywords](https://help.github.com/en/github/managing-your-work-on-github/closing-issues-using-keywords) so that the issue will be automatically closed when the PR is merged (example: `Closes #<your issue number>`)
    - Add appropriate labels. See [wiki](https://github.com/OpenEnergyPlatform/ontology/wiki/Usage-of-github-labels) for more information.
8. 📝 Describe briefly (i.e. in one or two lines) what you changed in the `CHANGELOG.md` file. End the description by the number in parenthesis `(#<your PR number>)` 
9. 📙 Add [term tracker annotations](https://github.com/OpenEnergyPlatform/ontology/wiki/Term-Tracker-Annotation) to the main changed classes of the ontology

     ![img](https://github.com/user-attachments/assets/70b0a061-f852-4567-9e1f-146f6fc04ed4)
10. 🔶 Stage, commit and push the changes of steps 7 and 8
11. 🐙 [Ask](https://help.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users) for review of your PR.  
    As the issue will have been discussed and agreed on prior to implementation, the purpose of the review step post-implementation is to check that the implementation has been faithful to what was agreed. One or two reviewers may be needed depending on the nature of the change that has been made.<br> 
    If the change involves adding content (issue type A), a domain expert should review the issue. If the change involves restructuring the ontology (issue type B), an ontology expert should review. If the change involves both changes to content and restructuring (issue types B and C), it is best to ask both an ontology expert and a domain expert to review. See the section "Teams tag" of the [README](https://github.com/OpenEnergyPlatform/ontology/blob/dev/README.md) for more information about the expertise of the different team members.

#### Merge your Changes after Approval

12. 🐙 Check that, after this whole process, your branch does not have conflicts with `dev` (GitHub will prevent you from merging if there are conflicts). In case of conflicts you are responsible for fixing them on your branch before you merge (see below "Fixing merge conflicts" section). If you need help, write a comment in the PR and ask for help from the ontology-expert-team.
    
13. 🐙 Once approved, merge the PR into `dev` and delete the branch on which you were working. In the merge message on github, you can notify people who are currently working on other branches that you just merged into `dev`, so they know they have to check for potential conflicts with `dev`.

**Hint**
GitHub has three versions of merging: 'Create a merge commit', 'Squash and merge' and 'Rebase and merge'. All three are explained in [this article.](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github) <br>
In general you are fine just keeping the default option but either one is feasible.
   
   
### Fixing merge conflicts in git

Avoid large merge conflicts by merging the updated `dev` versions in your branch.
In case of conflicts between your branch and `dev` you must solve them either online via the "resolve conflicts" button (🐙) or locally (🔶+📝).

1. 🔶 Get the latest version of `dev`
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
    
4. 📝 The conflicts have to be [manually](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line) resolved
    


### Communicate

Feel free to ask the community if you need help. We are happy to support you. If you want to contact specific teammembers or experts, please check out the Teams section of our [README](https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file#teams) file. Use the [OEP contact form](https://openenergyplatform.org/contact/) if you want to become a team member.
