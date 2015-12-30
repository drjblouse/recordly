import fileinput
from invoke import run, task
import os.path
import sys


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


@task
def package(deb_file=None):
    """ This task creates a debian deployment package for the recordly api.
    :param deb_file: Name of debian file.
    """
    try:
        if not deb_file:
            version = VERSION_NUM + '-' + os.getenv('BUILD_NUMBER', '1')
            deb_file = DEB_FILE_NAME.format(version)
            update_control_version(version)
        print("Creating deployment package " +
              deb_file + " for the recordly API.")
        print("This process takes several minutes. Please wait...")
        if os.path.exists(deb_file):
            run('rm ' + deb_file)
        if not os.path.isdir('debian/opt/recordly'):
            run('mkdir -p debian/opt/recordly')
            run('mkdir -p debian/opt/recordly/log')
            run('mkdir -p debian/opt/recordly/media')
        run('rsync -av --progress . debian/opt/'
            'recordly --exclude debian > /dev/null')
        run('fakeroot dpkg-deb --build debian > /dev/null')
        run('mv debian.deb ' + deb_file)
        print('Created ' + deb_file + ' on root.')
    except Exception as ex:
        print('Something went wrong building deb package.')
        print(ex.message)
    finally:
        run('rm -rf debian/opt')


def update_control_version(version, file_path='debian/debian/control'):
    """ Updates the version number in a provided debian control file.
    :param file_path: Path to the debian control file.
    :param version: Version to write to control file during build.
    """
    for line in fileinput.input(file_path, inplace=1):
        if 'Version: ' in line:
            old_ver = line.split(' ')[1]
            line = line.replace(old_ver, version) + '\n'
        sys.stdout.write(line)
