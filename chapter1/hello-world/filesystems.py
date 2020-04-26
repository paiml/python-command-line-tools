import click

#CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


#@click.group(context_settings=CONTEXT_SETTINGS)
#@click.option('--verbose', is_flag=True, help='Produce more output')
#@click.pass_context
@click.command
def main(ctx, verbose):
    """ A Tool that deals with filesystems """
    return


if __name__ == '__main__':
    main()
