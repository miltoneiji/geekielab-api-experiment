[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This project is an experiment using Geekie Lab's Single Sign On. Code structure was cloned from https://github.com/realpython/flask-boilerplate.

### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/danielbucher/geekielab-api-experiment.git
  $ cd geekielab-api-experiment
  ```

2. Initialize and activate a virtualenv:
  ```
  $ mkvirtualenv geekielab-api-experiment
  $ workon geekielab-api-experiment
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)

### Testing the API

1. Add your credential info in app.py
 
Edit `app.py` lines 49 to 51 with your credentials. Reload the page and try logging into Geekie Lab.

