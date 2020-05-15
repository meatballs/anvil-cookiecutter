# Anvil Cookiecutter Template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create a new [Anvil](https://anvil.works) application on your local machine.

## Features

* Dynamic menu construction using the [navigation](https://github.com/meatballs/anvil-navigation) module
* Optional inclusion of [hash routing](https://github.com/s-cork/HashRouting)
* Optional role based authorisation using the [authorisation](https://github.com/meatballs/anvil-authorisation) module
* Optional event propogation using the [events](https://github.com/meatballs/anvil-events) module

## Pre-requisites

* You will need to have cookiecutter installed on your machine. Follow the [cookiecutter installation instructions](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)

## Usage

To create a new app, run the following command in your terminal:
```
cookiecutter gh:meatballs/anvil-coookiecutter
```

You will be asked for the name of your new app and the name of the python package for that app 
(which will default to 'MyApp' and 'my_app' respectively). You'll also be aksed whether or not you want to include the optional components and then your app will then be created in your current working directory.

You can specify a different destination folder for your app by passing the `-o` option to  cookiecutter:
```
cookiecutter gh:meatballs/anvil-cookiecutter -o <destination folder>
```
Other options (e.g. using ssh) are described fully in the [usage section of the cookiecutter docs](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html#generate-your-project).

## Pushing your app to anvil.works

To push your app to your anvil account, you will need to have git installed on your local machine.

  * Create a new app within your Anvil account
  * From its 'Settings' menu, open the 'Version History...' option and click the 'Clone with Git' at the bottom
  * Copy the url for your app to your clipboard (that's everything between `git clone` and the app name in the command that's displayed).
  * Cancel the Git Access window and close your app
  * In your terminal, initialise a git repository in your local app folder and add the app at anvil.works as a remote:
  ```
  cd <path to your new local app>
  git init .
  git remote add anvil <paste the url you copied here>
  git fetch anvil
  ```
  * Commit the files in your local app to git and push them to anvil.works:
  ```
  git add -A
  git commit -m "Initial commit"
  git branch -u anvil/master
  git push -f
  ```
  NOTES:
  * This last step uses a 'force' push to overwrite the history on your app at anvil.works. Whilst this is fine for a new app as described here, be careful about doing this to an existing app unless you know what you're doing.
  * If you included the authorisation module, you will need to add tables to your new app. Full instructions are in the module's README.
