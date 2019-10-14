# Recipe App API

![recipe-app-api](./images/medfood.jpg)

[![Build Status](https://travis-ci.org/masoudr/recipe-app-api.svg?branch=master)](https://travis-ci.org/masoudr/recipe-app-api)
[![Coverage Status](https://coveralls.io/repos/github/masoudr/recipe-app-api/badge.svg?branch=master)](https://coveralls.io/github/masoudr/recipe-app-api?branch=master)

This is a recipe RESTful API written with **Django** and **Django REST framework** based on **Test-driven development** built over **Docker** and **Travis CI**.

This project is a sample app that can be used for other projects.

## Features

* Setting up the project with Docker
* Configuration for Travis CI and Coveralls
* Use a fully custom user model instead of the default Django User model
* Endpoints for creating and managing users, tags, ingredients, and recipes
* Filtering to list endpoints
* Image upload for recipes
* Lots of unit tests

## Usage

To start project, run:

```shell
cd <project_dir>
docker-compose build
docker-compose up
```

The API will be available at [http://127.0.0.1:8000](.)

## Test

To test project, run:

```shell
docker-compose.exe run --rm app sh -c "python manage.py test && flake8"
```
