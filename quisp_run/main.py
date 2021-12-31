#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from typing import List

from quisp_run.commands import run, parse


@click.group()
def main():
    pass


main.add_command(run)
main.add_command(parse)