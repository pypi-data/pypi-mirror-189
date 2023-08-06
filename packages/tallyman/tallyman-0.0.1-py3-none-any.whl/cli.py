import click

from logcfg import logger
from tallyman import TallyMan


@click.group()
def cli1():
    pass


@click.group()
def cli2():
    pass


@cli1.command()
@click.argument('config')
@click.option("--csvfilename", default="tallyman.csv", help="csv file name for save operation")
def scan(config: str, csvfilename: str) -> None:
    """
    Scan Folder

    :param config: yaml absolute file path
    :param csvfilename: csv file name
    :return:
    """
    tallyman = TallyMan()
    filepath = tallyman.scan(config, csvfilename)
    logger.info(f"Output operation to {filepath}")


@cli2.command()
@click.argument('csvfilepath')
def organize(csvfilepath: str) -> None:
    """
    organize files by operation in csv file

    :param csvfilepath: csv filepath
    :return:
    """
    tallyman = TallyMan()
    tallyman.organize(csvfilepath)


cli = click.CommandCollection(sources=[cli1, cli2])
if __name__ == '__main__':
    cli()
