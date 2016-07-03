![](https://travis-ci.org/WorldBrain/cortex.svg?branch=master)
[![codecov](https://codecov.io/gh/WorldBrain/cortex/branch/master/graph/badge.svg)](https://codecov.io/gh/WorldBrain/cortex)
![](https://img.shields.io/badge/Python-3.5-green.svg)

# cortex
`cortex` is the back-end server for the [webmarks][marks] project.

It is a [django][django] and [django-rest-framework][drf] powered application.

# Status
This project is in the initial bootstrap stages and as such is lacking many things.

Please help us to change this! Join us at our [gitter chat][chat].

# Documentation
If you'd like to get more familiarised with the goals of [Worldbrain][brain], check out the [docs repo][docs].

We value documentation highly, please help us to keep the documentation up to date and relevant.

# Installation
Fork this repo and get a local copy with:

```
$ git clone https://github.com/<username>/cortex && cd $_
```

Please [create a virtualenv first][venv].

Install the system requirements:

```
$ make system_requirements
```

We use [pip-tools][tools] and [pip][python-pip] to manage our requirements:

```
$ pip install -r requirements/dev.txt
```

Get a PostgreSQL database and a user up and running:

```
$ sudo -u postgres createdb worldbrain
$ sudo -u postgres psql
postgres=# CREATE USER cortex with PASSWORD 'cortex';
postgres=# GRANT ALL PRIVILEGES ON DATABASE worldbrain to cortex;
postgres=# ALTER USER cortex CREATEDB;
```

You'll then need to export a number of environment variables.

Please check the `.travis.yml` under `global` for those.

After that, you can then run:

```
$ python manange.py migrate
$ python manage.py runserver
```

Happy hacking!

# Testing
We are using [py.test][pytest] for our testing. You can run them with:

```
$ py.test worldbrain           # test runner
$ ptw worldbrain -- --testmon  # test watcher
```

# Contributing
We will soon add details to the [docs repo][docs].

In the mean time, please check our [issues][iss] list for things to do.

[marks]: https://github.com/WorldBrain/webmarks
[django]: https://www.djangoproject.com/
[drf]: http://www.django-rest-framework.org/
[docs]: https://github.com/WorldBrain/docs
[brain]: http://www.worldbrain.io/
[pytest]: http://pytest.org/latest/
[venv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[tools]: https://github.com/nvie/pip-tools
[python-pip]: https://pip.pypa.io/en/stable/installing/
[iss]: https://github.com/WorldBrain/cortex/issues
[chat]: https://gitter.im/WorldBrain/webmarks
