import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help', 'help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """This is a custom help menu for the main() func"""
    return

@main.command(hidden=True)
@click.pass_context
def help(ctx): 
    print(ctx.parent.get_help())

if __name__ == '__main__':
    main()
