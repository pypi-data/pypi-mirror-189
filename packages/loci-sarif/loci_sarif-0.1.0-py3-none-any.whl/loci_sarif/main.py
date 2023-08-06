import click

import loci_sarif.utils as lcu
from loci_sarif.add import add
from loci_sarif.summary import summary


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    lcu.print_version()
    ctx.exit()


@click.group()
@click.option("-v", "--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def loci_sarif():
    pass


loci_sarif.add_command(add)
loci_sarif.add_command(summary)


if __name__ == "__main__":
    loci_sarif()
