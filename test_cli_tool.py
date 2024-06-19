import pytest
from click.testing import CliRunner
from cli_tool import cli

def test_greet():
    runner = CliRunner()
    result = runner.invoke(cli, ['greet', 'Alice', '--greeting', 'Hi'])
    assert result.exit_code == 0
    assert 'Hi, Alice!' in result.output

def test_add():
    runner = CliRunner()
    result = runner.invoke(cli, ['add', '5', '7'])
    assert result.exit_code == 0
    assert 'The sum of 5 and 7 is 12' in result.output

def test_add_invalid():
    runner = CliRunner()
    result = runner.invoke(cli, ['add', 'five', 'seven'])
    assert result.exit_code != 0
    assert 'Invalid value for' in result.output

def test_multiply():
    runner = CliRunner()
    result = runner.invoke(cli, ['multiply', '3', '4'])
    assert result.exit_code == 0
    assert 'The product of 3 and 4 is 12' in result.output

