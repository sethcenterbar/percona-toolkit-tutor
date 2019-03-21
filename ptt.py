import click
import functions
    
@click.group()
def cli():
  """Percona Toolkit Tutor is a wrapper around percona-toolkit, aimed at making the kit more discoverable.

    \b
    To see a list of supported percona-toolkit tools, run the following command:
      $ ptt tools
    """


@cli.command(help="Show all info about a given tool")
@click.argument('tool')
def info(tool):
  """
  Info will run all commands to give a great overview of the tool
  """

  functions.output_info(tool)
  functions.output_examples(tool)
  functions.output_blog_posts(tool)

@cli.command(help="Show examples of a given tool")
@click.argument('tool')
def examples(tool):
  """
  Examples allows you to pass the name of a supported percona-toolkit tool and retreive relevant examples about it
  """
  functions.output_examples(tool)

@cli.command(help="Useful links that reference a given tool")
@click.argument('tool')
def blog(tool):
  """
  Blog allows you to pass the name of a supported percona-toolkit tool and retrieve relevant blog posts about it
  """
  functions.output_blog_posts(tool)

@cli.command(help="Useful videos that reference a given tool")
def video():
  pass


@cli.command(help='List the supported percona-toolkit tools')
def tools():
  supported_scripts = functions.import_docs(scripts=True)

  for script in supported_scripts:
    click.echo(script)
