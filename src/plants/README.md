# plants

> A collection of homegrown Python libraries

I maintain a handful of personal projects written in Python. This repository
contains code that is shared between them. To avoid the headache of publishing
and maintain packages, I simply add this repository as a submodule within my
other repositories.

Setup is as follows:

1. Add the submodule: `git submodule add git@github.com:mackorone/plants.git`
1. Update requirements files to reference the one in this repo: `-r plants/requirements.in`
1. If using GitHub Actions, update the checkout step to include: `submodules: recursive`
