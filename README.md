# major-project

### Local Development
* Clone this repository to your local machine
  ```shell
  git clone https://github.com/amitness/major-project
  ```

* In the directory where you placed the cloned repo, create a virtual environment for Python:
  ```shell
  pip install virtualenv
  virtualenv -p python3 venv
  ```
* Activate your virtual environment
  ```shell
  source venv/bin/activate
  ```

* Install all required packages:
  ```shell
  pip install -r requirements.txt
  ```
  *Install ffmpeg package
  ```shell
  sudo add-apt-repository ppa:mc3man/trusty-media
  sudo apt-get update
  sudo apt-get install ffmpeg
  ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
