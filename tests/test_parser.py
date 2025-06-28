import pytest
from vuln_checker.parser import parse_requirements

def test_parse_requirements(tmp_path):
    req_file = tmp_path / "requirements.txt"
    req_file.write_text("flask==2.0.1\nrequests>=2.26.0\ndjango~=3.2.0\n")

    result = parse_requirements(str(req_file))
    assert result == [
        {
            "version": "2.0.1",
            "operator": "==",
            "package": {"name": "flask", "ecosystem": "PyPI"}
        },
        {
            "version": "2.26.0",
            "operator": ">=",
            "package": {"name": "requests", "ecosystem": "PyPI"}
        },
        {
            "version": "3.2.0",
            "operator": "~=",
            "package": {"name": "django", "ecosystem": "PyPI"}
        }
    ]