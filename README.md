# Overwatch Queue Notifier
This project uses a neural network to detect when a player is in queue for a game of Overwatch. It then sends a notification to the user using a module specified by the user.

## Installation (Note: Currently in alpha)
1. Clone the repository
2. Install dependencies using `poetry install`
3. Run the program using `poetry run python main.py --notifier notifiers:<NotifierName>`

    The notifier name is the name of the notifier module you want to use. For example, if you want to use the Discord notifier, you would use `poetry run python main.py --notifier notifiers:Discord`

## Notifiers
Currently, none of the notifiers are configured. To use this project, you will need to implement your own notifier script.

## Contributing
If you would like to contribute to this project, please open an issue or pull request. I expect that any PR's will be well documented and tested.

### Development environment
1. Clone the repository
2. Install dependencies using `poetry install --with dev`

Note: In my testing, pytorch (torch) does not function correctly using the virtual environment created by Poetry. Some missing dependency. 

I reccomend using `virtualenv` to create the virtual environment in the working directory with the name `.venv` then setting the poetry configuration to use that virtual environment. This can be done using `poetry config virtualenvs.in-project true`. Then, you can install the dependencies using `poetry install --with dev`. If the virtual environment isnt being detected correctly, you can specify the venv using `poetry config virtualenvs.path .venv`

### Development workflow
- Run `pre-commit install` to install the pre-commit hooks
    - These hooks include black, isort, and mypy. They will run before every commit to ensure that the code is formatted correctly and that there are no type errors.
- Create a new branch for your feature/bugfix
- use `coverage run -m pytest` and `coverage report` to ensure that your code is well tested


## Project Outline
### `./data`
This directory contains all of the data used by the project. This includes the neural network model, the training data, and the testing data.

### `./utils`
Contains some utility packages used by the project.

### `./model`
Contains the neural network model used by the project, a predictor script, as well as the trained pytorch model `model.pth`


