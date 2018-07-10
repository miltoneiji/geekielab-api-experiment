[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This project is an experiment using Geekie Lab's Single Sign On. It uses the flask boilerplate provided by https://github.com/realpython/flask-boilerplate.

### Requirements

* `GEEKIE_SHARED_SECRET` env var. If you don't know your API secret, contact engineering
* Python 2
* Virtualenv wrapper

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

  You may have to install `hashlib` using `easy_install` before running the above command.

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)
