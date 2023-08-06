# ebranch

Tool for branching Fedora packages for EPEL

```
$ ebranch
Usage: ebranch [OPTIONS] COMMAND [ARGS]...

  Tool for branching Fedora packages for EPEL

Options:
  --help  Show this message and exit.

Commands:
  dependencies  Commands for working with dependencies
  issues        Commands for issue tracker integration
  version       Display ebranch version information

$ ebranch dependencies
Usage: ebranch dependencies [OPTIONS] COMMAND [ARGS]...

  Commands for working with dependencies

Options:
  --help  Show this message and exit.

Commands:
  build-reqs             lists build requirements for a package
  calculate-chain-build  Calculate chain build
  find-cycles            Find dependency cycles
  is-branched            checks if a package is branched
  iterate                computes missing BRs for new top-level packages
  ls-branches            lists branches for a package
  missing-build-reqs     lists missing build requirements to build for a...
  unfold                 adds new missing BRs to the top-level list

$ ebranch issues
Usage: ebranch issues [OPTIONS] COMMAND [ARGS]...

  Commands for issue tracker integration

Options:
  --help  Show this message and exit.

Commands:
  file-request  file a branch request
```

## Presentation
Presented at [CentOS Dojo FOSDEM
2022](https://wiki.centos.org/Events/Dojo/FOSDEM2022#Bootstrapping)
([slides](https://salimma.fedorapeople.org/slides/2022/centos_dojo-202202-epel_branching_with_ebranch.pdf),
[video](https://www.youtube.com/watch?v=VjPZmq_h2Rk)).

## Installation
``` bash
sudo dnf install ebranch
```

## Local development
Make sure you install `rpmdistro-repoquery`:

```bash
sudo dnf install rpmdistro-repoquery
```

``` bash
python3 -m venv .venv-dev
source .venv-dev/bin/activate
pip install --upgrade pip
pip install -q build
make dist install
make install
```
