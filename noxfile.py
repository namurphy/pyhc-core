import nox

PYTHON_VERSIONS = ("3.9", "3.10", "3.11", "3.12")

nox.options.default_venv_backend = "uv|virtualenv"

@nox.session(python=PYTHON_VERSIONS)
def build(session: nox.Session):
    """Build and verify a source distribution and wheel."""
    session.install("twine", "build")
    build_command = ("python", "-m", "build")
    session.run(*build_command, "--sdist")
    session.run(*build_command, "--wheel")
    session.run("twine", "check", "dist/*")


@nox.session(python=PYTHON_VERSIONS)
def install(session: nox.Session):
    session.install("uv", "nox")
    session.run("uv", "pip", "compile", "pyproject.toml", "--all-extras")
