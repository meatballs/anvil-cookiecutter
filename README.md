# Anvil Cookiecutter Template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create a new [Anvil](https://anvil.works) application on your local machine.

## Features

* Dynamic menu construction using the [navigation](https://github.com/meatballs/anvil-navigation) module
* Optional inclusion of [hash routing](https://github.com/s-cork/HashRouting)

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

 * Install the anvil app server by following the 'Set up your environment' section of the [Getting Started Guide](https://github.com/anvil-works/anvil-runtime/blob/master/doc/getting-started.md)
 
 * Start your app:
 ```
 anvil-app-server --app <path to your new app folder>
 ```

 * Open your favourite browser and navigate to `http://localhost:3030`

### Running on anvil.works

To push your app to your anvil account, you will need to have git installed on your local machine.

  * Create a new app within your Anvil account
  * From its 'Settings' menu, open the 'Version History...' option and click the 'Clone with Git' at the bottom
  * Copy the url for your app to your clipboard (that's everything after `git clone` in the command that's displayed).
  * Cancel the Git Access window and close your app
  * In your terminal, initialise a git repository in your local app folder and add the app at anvil.works as a remote:
  ```
  cd <path to your new local app>
  git init .
  git remote add anvil <paste the url you copied here>
  ```
  * Commit the files in your local app to git and push them to anvil.works:
  ```
  git add -A
  git commit -m "Initial commit"
  git push -f -u anvil master
  ```
  NOTE - this last step uses a 'force' push to overwrite the history on your app at anvil.works. Whilst this is fine for a new app as described here, be careful about doing this to an existing app unless you know what you're doing.
  
