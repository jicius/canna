# Rest api template for flask

[![Build Status](https://travis-ci.org/jicius/canna.svg?branch=master)](https://travis-ci.org/jicius/canna)

This is my cookiecutter template to build a simple, fast and rock solid website based upon
the flask framework.

## Features

* (Optional) pytest
* (Optional) tox
* (Optional) Docker support

## Usage

Install [Cookiecutter](https://github.com/audreyr/cookiecutter):

    $ pip install cookiecutter

Initialize the project with cookiecutter and answer some questions for the newly started project:

    $ cookiecutter https://github.com/jicius/canna

    project_name [project_name]: flask_test
    project_slug [tornado_test]:
    author_name [Your name]: Your name
    email [Your e-mail]: yourname@example.com
    github_username [yourname]: yourusername
    repo_name [tornado-project]:
    description [A short description of the project.]: short description
    version [0.1.0]:
    use_pytest [y]: y
    use_tox [y]: y
    use_docker [y]: y
    use_vagrant [y]: y
    use_bumpversion [y]: y
    Select open_source_license:
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1
