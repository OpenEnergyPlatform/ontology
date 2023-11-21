# Release Procedure

The release procedure is a process in which different parts of the repository are involved.<br>
These symbols help with orientation:
* 🐙 GitHub
* 💠 git (Bash)
* 📝 File
* 💻 Command Line (CMD)


## Version Numbers

This software follows the [Semantic Versioning (SemVer)](https://semver.org/).<br>
It always has the format `MAJOR.MINOR.PATCH`, e.g. `1.5.0`.

The data follows the [Calendar Versioning (CalVer)](https://calver.org/).<br>
It always has the format `YYYY-MM-DD`, e.g. `2022-05-16`.


## GitHub Release

Following the Semantic Versioning, different workflows for Major, Minor, or Patch
releases are possible. <br>
For Major and Minor releases, follow the complete workflow.<br>
For a **Patch Release** (Hotfix), start at [section 3](https://github.com/rl-institut/super-repo/blob/production/RELEASE_PROCEDURE.md#4--create-a-draft-github-release).

### 1. 🐙 Create a `GitHub Project`
* Create [New classic project](https://github.com/rl-institut/super-repo/projects?type=classic)
* Use the project template *Automated kanban with reviews*
* Named `super-repo-v0.1.0`
* Add a meaningful description
* Track project progress

▶️ It gives an overview of open and finished issues and Pull Requests!

### 2. 🐙 Finish all planned Developments
* Some days before the release, inform all developers
* Merge the open Pull Requests
* On release day, start the release early to ensure sufficient time for reviews
* Merge everything on the `develop` branch

▶️ Completion of the preparation of the planned release!

### 3. 🐙 Create a `GitHub Issue`
* Use `📝issue_template_release`
* Name `Release - Minor Version - 0.1.0`
* Complete the necessary details

▶️ This issue documents the status of the release!

### 4. 🐙 Create a `Draft GitHub Release`
* Start here for a **Patch Release** (Hotfix)
* [Draft a new release](https://github.com/rl-institut/super-repo/releases/new)
* Enter the release version number `0.1.0` as title
* Summarize key changes from changelog in the description
```
## [0.1.0] Minor Release - Name - Date
### Added
### Changed
### Removed
```
* Add a link to the `📝CHANGELOG.md`
    * `**Complete changelog:** [CHANGELOG.md](https://github.com/rl-institut/super-repo/blob/production/CHANGELOG.md)`
* Add a link to compare versions
    * `**Compare versions:** [0.1.0 - 0.2.0](https://github.com/rl-institut/super-repo/compare/v0.1.0...v0.2.0)`
* **Save draft**

### 5. 💠 Create a `release` branch
* Checkout `develop` and branch with `git checkout -b release-v0.1.0`
* Push branch with `git push --set-upstream origin release-v0.1.0`
* Add bump2version (❗ToDo❗) 

### 6. 📝 Update the version files
* `📝CHANGELOG.md`
    * Check that all Pull Request are included
    * Rename `Unreleased` section with release title from issue
    * Follow `[0.0.0] Minor Release - Name of Release - 20YY-MM-DD`
* `📝CITATION.cff`
    * Update `version`
    * Update `date-released`
* `📝setup.py`
    * Update `version`
    * Update `download_url` (.../v0.1.0.tar.gz)

▶️ Increase version numbers!

### 7. 🐙 Create a Release Pull Request
* Merge `release` into `production` branch
* Remove details from template
* Assign two reviewers to check the release
* Run all test
* Execute the software locally
* Wait for reviews and tests
* Merge Pull Request and delete `release` branch

▶️ Merge code on `production` branch!

### 8. 💠 Set the `Git Tag`
* Checkout `production` branch and pull
* Check existing tags `git tag -n`
* Create new tag: `git tag -a v0.1.0 -m "super-repo Minor Release v0.1.0"`
* This commit will be the final version for the release, breath three times and check again
* Push tag: `git push --tags`

If you messed up, remove tags and start again
* Delete local tag: `git tag -d v0.1.0`
* Delete remote tag: `git push --delete origin v0.1.0`

▶️ Git Tag for GitHub Release!

### 9. 🐙 Publish `GitHub Release`
* Navigate to releases and open the draft release
* Choose the correct `Git Tag`
* Choose the `production` branch
* Select `Set as the latest release`
* Select `Create a discussion for this release` in category `Announcements`
* **Publish release**

▶️ Release on GitHub! 🚀

### 10. 💻 Update the documentation
* Checkout `production` branch and pull
* Activate environment and enter repository
* Test version with `mike serve`
* Publish new minor version `mike deploy --push --update-aliases 0.1 latest`
* Set new version as latest `mike set-default --push latest`

▶️ Update the documentation!

### 11. 🐙 Set up new development
* Create a Pull Request from `production` to `develop`
* Named `Set up new development after release v0.1.0`
* Checkout `develop` branch and pull
* Create a new **Unreleased** section in the `📝CHANGELOG.md`
```
## [Unreleased]

### Added
- [(#)]()

### Changed
- [(#)]()

### Removed
- [(#)]()
```

▶️ Continue the developments 🛠


## PyPi Release

### 0. 💻 Check release on Test-PyPI
* Check if the release it correctly displayed on [Test-PyPI](https://test.pypi.org/project/open-mastr/#history)
* With each push to the release branch or the branch `test-release` the package is released on [Test-PyPI](https://test.pypi.org/project/open-mastr/#history) by GitHub workflow (test-pypi-publish.yml).
  * Note: Pre-releases on Test-PyPI are only shown under `Release history` in the navigation bar.
  * Note: The branch status can only be released to a version on Test-PyPI once. Thus, for every branch status that you want to see on Test-PyPI increment the build version with `bump2version build` and push afterwards.
* Once testing on Test-PyPI is done, change the release version to the final desired version with `bump2version release`
  * Note: The release on Test-PyPI might fail, but it will be the correct release version for the PyPI server.
* Push commits to the `release-*` branch

### 1. 💻 Create and publish package on PyPI
* Navigate to git folder `cd D:\git\github\GROUP\REPO\`
* Create package using `python setup.py sdist`
* Check that file has been created in folder `dist`
* Activate python environment `activate release_py38`
* Upload to PyPI using `twine upload dist/NAME_0.5.1.tar.gz`
* Enter `name` and `password`
* Check on PyPI if release arrived
* Breath three times and smile

▶️ Publish the Package

## Sources:
* https://raw.githubusercontent.com/folio-org/stripes/master/doc/release-procedure.md