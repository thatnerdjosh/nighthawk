## Nighthawk - A Cookiecutter Project

This is a Cookiecutter project template to jumpstart your development process. It provides a basic project structure and necessary setup steps to get you going quickly.

### Getting Started

1. **Install Development Dependencies:**

   Install the development dependencies using pipenv:

   ```bash
   pipenv install --dev
   ```

2. **Generate the Project:**

   Run the following command to generate a new project directory named after your project:

   ```bash
   python generate.py
   ```

3. **Navigate to the Project:**

   Change directories into the newly generated project folder:

   ```bash
   cd <your_project_name>
   ```

### Run your Project

#### Flask API
If you generated a Flask API, you can use it as follows:

1. **Install Dependencies:**

   Change directories into the newly generated project folder:

   ```bash
   pipenv install
   ```

2. **Run the App:**

   Change directories into the newly generated project folder:

   ```bash
   pipenv run python main.py
   ```

#### Nuitka Binary (Optional)
If you generated a Nuitka hardened/compiled project, you can build in this way:

1. **Install Dependencies:**

   Change directories into the newly generated project folder:

   ```bash
   pipenv install --dev
   ```

2. **Run the App:**

   Change directories into the newly generated project folder:

   ```bash
   pipenv run build
   ```

### Project Structure

The generated project will have a basic structure that you can customize further. Here's a general overview:

* `README.md`: This file (you're reading it now!) contains instructions and information about the project.
* `generate.py`: This script can be used to generate the project using Cookiecutter.
* `<your_project_name>`: This directory contains your project's core source code and other relevant files.
	* `Pipfile`: This file manages your project's dependencies using pipenv.
	* `Pipfile.lock`: This lockfile ensures consistent dependencies across environments.
	* `setup.py`: Used for Nuitka builds (optional), otherwise not currently necessary.
	* `.gitignore`: Used for ignoring files which should not be committed to the repostiory.

### Customization

Feel free to modify the generated project structure, dependencies, and build commands based on your specific needs. This template provides a starting point to streamline your development workflow.

### Next Steps

Once you've set up the project, you can start working on your code within the `<your_project_name>` directory. Refer to any additional documentation or instructions specific to your project for further development guidance.

