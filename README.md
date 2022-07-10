# Password-Generator
Generates a random password as you want.

## Requirements

- Python 3.8.10+

## Usage

Usage guide:

```shell script
$ python  generate_password.py [-h] [-l {weak,medium,strong}] [-len LENGTH] [-up] [-lw] [-d] [-s]
```

Arguments:
```shell script
optional arguments:
  -h, --help            show this help message and exit
  -l {weak,medium,strong}, --level {weak,medium,strong}
  -len LENGTH, --length LENGTH
                        Length of password
  -up, --upper          Use upper case characters
  -lw, --lower          Use lower case characters
  -d, --digit           Use digits
  -s, --symbol          Use symbols
```

Examples:
```shell script
$ python generate_password.py
lrvql086

$ python generate_password.py -l weak
usy01hfo

$ python generate_password.py -l medium
5aPn8gtk6sunMKD5

$ python generate_password.py -l strong
4gRKCGX>7;M\i?&xnL"nUn>#

$ python generate_password.py -len 12 -up -lw -d
JdywZgWG3Zqb

$ python generate_password.py -len 20 -up -lw -d -s
^5!Z\)\>?7YG7.O.kj~'
```

## Licensing

GNU General Public License v3.0

Read the license at [LICENSE](https://github.com/AliLastReza/Password-Generator/blob/main/LICENSE) file.

## Contributions

All kind of contributions are welcome.

Feel free to send pull requests.

### Contributors

* [AliLastReza](https://github.com/AliLastReza/) - Email address: [AliLastReza@pm.me](mailto:AliLastReza@pm.me)

## Questions

If you have any questions about the repo, open an issue or contact me directly at [AliLastReza@pm.me](AliLastReza@pm.me). You can find more of my work at [AliLastReza GitHub profile](https://github.com/AliLastReza/).
