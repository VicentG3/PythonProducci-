import click
@click.command()
@click.option('--a', prompt='First number',
    help='The first number to sum.')
@click.option('--b', prompt='Second number',
    help='The second number to sum.')
def sum(a, b):
    click.echo('The sum is %s' %(a + b))

if __name__ == '__main__':
    sum()