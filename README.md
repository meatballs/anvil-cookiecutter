# Anvil Cookiecutter Template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create a new [Anvil](https://anvil.works) application on your local machine.

## Features

* Dynamic menu construction using the [navigation](https://github.com/meatballs/anvil-navigation) module

#### Coming Soon

* Optional role based authorisation
* Optional dynamic serialisation of data tables content

## Pre-requisites

* You will need to have cookiecutter installed on your machine. Follow the [cookiecutter installation instructions](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)

## Usage

To create a new app, run the following command in your terminal:
```
cookiecutter gh:meatballs/anvil-coookiecutter
```

You will be asked for the name of your new app and the name of the python package for that app 
(which will default to 'MyApp' and 'my_app' respectively) and your app will then be created in your current
working directory.

You can specify a different destination folder for your app by passing the `-o` option to  cookiecutter:
```
cookiecutter gh:meatballs/anvil-cookiecutter -o <destination folder>
```
Other options are described fully in the cookiecutter docs.

## Running Your App

You can run your app locally using Anvil's app server or you can push it to your Anvil account and run it on their cloud service.

### Running Locally
TODO

### Running on anvil.works
TODO
