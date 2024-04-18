import click

@click.command()
@click.option('--name', prompt='Your name',
    help='The person to greet.')

def hello(name):
    click.echo('Hello %s!' % name)
#asfasd
if __name__ == '__main__':
    hello() 