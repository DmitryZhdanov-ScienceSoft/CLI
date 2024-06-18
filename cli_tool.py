import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.option('--greeting', default='Hello', help='Greeting to use')
def greet(name, greeting):
    click.echo(f"{greeting}, {name}!")

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def add(a, b):
    result = a + b
    click.echo(f"The sum of {a} and {b} is {result}")

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def multiply(a, b):
    result = a * b
    click.echo(f"The product of {a} and {b} is {result}")

@cli.command()
@click.argument('filename')
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            click.echo(contents)
    except FileNotFoundError:
        click.echo(f"Error: File '{filename}' not found or cannot be opened.")
    except Exception as e:
        click.echo(f"Error: An unexpected error occurred: {str(e)}")

@cli.command()
@click.option('--uppercase', '-u', is_flag=True, help='Convert text to uppercase.')
@click.argument('text')
def manipulate_text(text, uppercase):
    if uppercase:
        result = text.upper()
    else:
        result = text.lower()
    click.echo(result)

if __name__ == '__main__':
    cli()
