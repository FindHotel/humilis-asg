Humilis plug-in to deploy an Autoscaling Group
===================================================

[![PyPI](https://img.shields.io/pypi/v/humilis-asg.svg?style=flat)](https://pypi.python.org/pypi/humilis-bastion)

A [humilis][humilis] plug-in layer that deploys an Autoscaling Group. 

[humilis]: https://github.com/humilis/humilis


## Installation


```
pip install humilis-bastion
```


To install the development version:

```
pip install git+https://github.com/humilis/humilis-asg
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
make configure
```


## Testing

You can test the deployment with:

```
make test
```

The test suite will create various AWS resources that are required to support
the creation of the bastion host (e.g. a VPC and a public subnet). Those
resources will be automatically destroyed after the tests have run, but you
can make sure you are not leaving any infrastructure behind by manually
running:

```bash
make delete
```


## More information

See [humilis][humilis] documentation.

[humilis]: https://github.com//humilis/blob/master/README.md


## Contact

If you have questions, bug reports, suggestions, etc. please create an issue on
the [GitHub project page][github].

[github]: http://github.com/humilis/humilis-asg


## License

This software is licensed under the [MIT license][mit].

[mit]: http://en.wikipedia.org/wiki/MIT_License

See [License file][LICENSE].

[LICENSE]: https://github.com/humilis/humilis-bastion/blob/master/LICENSE.txt


© 2016 German Gomez-Herrero, [Find Hotel][fh] and others.

[fh]: http://company.findhotel.net
