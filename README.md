<p align="center">
  <img width="300" src="https://github.com/mESmaC/Hydrazine/blob/main/init/hydrapak/assets/hydrazine.svg">
</p>
<h1 align="center">Hydrazine Framework</h1>


#### Hydrazine is a lightweight web framework and CMS that simplifies the creation and management of dynamic websites and web applications. It uses .hdz files for easy content management and allows you to build and organize your components with minimal effort.

------------


Installation
Prerequisites
Python 3.8 or later

pip for managing Python packages

### Steps to Get Started

Clone the repository:
```
git clone https://github.com/mESmaC/Hydrazine.git
cd hydrazine
```
Activate the virtual environment: If you haven’t created a virtual environment yet, do so with:
```
python -m venv .venv
```
Then activate it:

Windows:
```
.\.venv\Scripts\activate
```

Mac/Linux:
```
source .venv/bin/activate
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Install Hydrazine in editable mode:
```
pip install -e .
```
Usage
After setting up your environment, you can begin creating and compiling projects with Hydrazine.

1. Initialize a New Project
To initialize a new project, navigate to your project directory and run:

```
hydrazine init
```
This will create a basic project structure, including configuration and source files.

2. Edit Your Project
Your project directory will be structured like this

```
/your-project
  /assets/        # Image and asset files
    hydrazine.svg # Example SVG asset
  /hydra/         # Folder for Hydra-related files
    index.hdz     # Primary Hydra file
    /styles/      # Folder for Hydra component styles
  /scripts/       # Folder for your JavaScript files
    hButton.js    # Example JS component
    scripts.js    # Main script file
  /styles/        # Folder for CSS files
    hButton.css   # Styles for hButton component
    styles.css    # Main styles file
  hydra.json      # Configuration file
  index.html      # Final compiled HTML file
  requirements.txt
  README.md
```
The src/ directory (inside hydra/) contains your .hdz files, where you can define and organize your components. assets/ stores images and other assets, while scripts/ and styles/ contain the JS and CSS files used in your project.

4. Compile the Project
Once you’ve edited your .hdz files in the hydra/ folder, compile the project to generate the HTML output:

hydrazine compile
This will compile your project and generate the necessary HTML file(s) in the project root directory.

4. Access the Compiled Output
After compiling, you will find the compiled index.html in the project directory. This is the HTML file that you can deploy to your web server.

Example Workflow
Initialize a new project:
```
hydrazine init
```
Edit .hdz files in the hydra/ directory (e.g., index.hdz).

Compile the project:
```
hydrazine compile
```
Deploy or open the index.html from the root directory.

Project Structure
Here is an example structure for your Hydrazine project:
```
/your-project
  /assets/
    hydrazine.svg          # Example image asset
  /hydra/
    index.hdz              # Your main Hydra file
    /styles/
      hButton.css          # Component styles
  /scripts/
    hButton.js             # JS component for hButton
    scripts.js             # Additional JS functionality
  /styles/
    hButton.css            # Styles specific to hButton
    styles.css             # Global styles
  hydra.json               # Hydra configuration
  index.html               # Compiled HTML output
  requirements.txt         # Dependencies file
  README.md                # Project documentation
```
