import os
import click


@click.argument('name')
@click.argument('url')
def fake(name, url):
    os.system(f'poetry add {url}')
    print('zae-park')