import atexit
import os
import shutil
import subprocess
import sys
import tempfile

import yaml

TEMPLATE_NAME = "scaffold.yml"


def get_template_file(source_dir):
    return os.path.join(source_dir, TEMPLATE_NAME)


def get_data(template):
    """
    Read the template file and return it's contents
    """
    template_dir = fetch(template)
    template_file = get_template_file(template_dir)

    with open(template_file, encoding="UTF-8") as fd:
        return yaml.safe_load(fd)


def git_clone(url):
    # Create a temporary folder to be deleted at exit
    tmpdir = tempfile.mkdtemp(prefix="scaffold")

    def remove_tmpdir():
        shutil.rmtree(tmpdir)

    atexit.register(remove_tmpdir)

    # Clone the repository
    git = shutil.which("git")
    if git is None:
        sys.exit("error: git not found")

    try:
        subprocess.run([git, "clone", url, "repository"], cwd=tmpdir, check=True)

        template_dir = os.path.join(tmpdir, "repository")
        if os.path.isfile(get_template_file(template_dir)):
            return template_dir
        return None
    except subprocess.CalledProcessError:
        sys.exit(f'error: failed to clone remote repository "{url}"')


def fetch(source_dir):
    """
    Fetch the repository if it's a remote one, otherwise
    check that's valid with a scaffold.yml file
    """
    # If it's a template file (and not a directory), be kind
    if os.path.exists(source_dir) and not os.path.isdir(source_dir):
        source_dir = os.path.dirname(source_dir)
        if os.path.isfile(get_template_file(source_dir)):
            sys.exit(f'error: please specify the folder containing "{TEMPLATE_NAME}", not the file itself')

    # If it exists locally, just return it
    if os.path.isdir(source_dir):
        if os.path.isfile(get_template_file(source_dir)):
            return source_dir
    else:
        retval = git_clone(source_dir)
        if retval:
            return retval
    sys.exit(f'error: no template "{TEMPLATE_NAME}" could be found in path "{source_dir}"')
