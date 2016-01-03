""" This is for executing build steps such as invoke build. """
from invoke import run, task
import os.path


DEB_FILE_NAME = 'recordly_{0}.deb'
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
VERSION_NUM = os.getenv('VERSION_NUM', '1.0.0')


@task
def test():
    """ Run django tests. """
    run("python3 -m coverage run --source='.' manage.py test")
    run("python3 -m coverage report")


@task
def lint():
    """ Run lint checking on code. """
    run('python3 -m pylint --load-plugins pylint_django api',
        warn=True, echo=True)


@task(default=True)
def build():
    lint()
    test()
