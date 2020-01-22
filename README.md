# [Backdoor](https://www.google.com/search?q=backdoor) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/koritarsa)

![version](https://img.shields.io/badge/version-1.0-blue.svg?style=flat)
![licence](https://img.shields.io/badge/licence-MIT-blue.svg?style=flat)
![build](https://img.shields.io/badge/build-passing-orange.svg?style=flat)

It is a simple reverse shell handler for all platforms that can run Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to use the software and how to install them

Packages:

```
python^3.6
python@socket,
	  @os,
	  @subprocess,
	  @time@sleep
```
To install them:

```
pip i <package name>
```

### Running

You will need to put you IP address and the open port on server.py and client.py

#####And to run the program

Need to start the server that will send the commands and receive the response.

```
python3 server.py
```

 After that, the "victim" need to start the client.py

```
python3 client.py
```


## Built With

* [Python](https://www.python.org/) - The JavaScript runtime
* [Sublime Text](https://www.sublimetext.com/) - Used to code

## Versioning

It only has one version, but I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jakoritarleite/twitter-bot/tags).

## Authors

* **João Koritar** - *Every Work* - [Twitter](https://twitter.com/koritarsa)

See also the list of [contributors](https://github.com/jakoritarleite/twitter-bot/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* If you want to give me a hat tip, email me at [jakoritarleite@gmail.com]()
