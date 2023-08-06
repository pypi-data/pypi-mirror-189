# Git infos

Lightful Git infos library without pretention

It uses shell commands to get git infos.

## Installation

```
pip install simple-git-infos
``` 

## Usage 

Import `gitinfos` module

Current functions are simple and easy to understand

* `get_current_git_branch()`
* `get_full_commit()`
* `get_short_commit_id()`
* `get_tag()`


**Sample**
```python
from simple_git_infos import gitinfos

print(f"BRANCH: {gitinfos.get_current_git_branch()}")
print(f"COMMIT: {gitinfos.get_full_commit()}")
print(f"ID: {gitinfos.get_short_commit_id()}")
print(f"TAG: {gitinfos.get_tag()}")
```

will output 

```
BRANCH: main
COMMIT: commit b78468a45489eec3ea6b816f5b28f7093d9bac4b
Author: marc dexet <marc.dexet@ias.u-psud.fr>
Date:   Fri Feb 3 08:41:52 2023 +0000

    Initial commit
ID: b78468a
TAG: 0.0.1
```

All functions could be pointed to any location


```python
full_commit= gitinfos.get_full_commit(cwd='/home/user/somewhere/')
```