import click
import os
import yaml

supported_scripts = []

def import_docs():
  with open('docs/tools.yaml') as f:
    doc = yaml.safe_load(f)

  for tool in doc['tools']:
    supported_scripts.append(tool['name'])

  return doc

def output_blog_posts(intool):
  click.echo(click.style('//Blog Posts about ' + intool, fg='green'))
  try:
    doc = import_docs()
    this_tool = None
    for tool in doc['tools']:
      if tool['name'] == intool:
        this_tool = tool
        break
    
    postnum = 1
    for post in this_tool['blog_posts']:
      click.echo("\nPost #" + str(postnum))
      click.echo("    Description: " + post['description'])
      click.echo("           Link: " + post['link'])
      postnum = postnum + 1

  except:
    click.echo("Couldn't find that tool")

  
@click.group()
def cli():
  """Percona Toolkit Tutor is a wrapper around percona-toolkit, aimed at making the kit more discoverable.

    \b
    To see a list of supported percona-toolkit tools, run the following command:
      $ ptt tools
    """


@cli.command(help="Show all info about a given tool")
def info():
  """
  Info will run all commands to give a great overview of the tool
  """
  doc = import_docs()
  print(doc)

@cli.command(help="Show examples of a given tool")
def examples():
  pass

@cli.command(help="Useful links that reference a given tool")
@click.argument('tool')
def blog(tool):
  """
  Blog allows you to pass the name of a supported percona-toolkit tool and retrive relevant blog posts about it
  """
  output_blog_posts(tool)

@cli.command(help="Useful videos that reference a given tool")
def video():
  pass


@cli.command(help='List the supported percona-toolkit tools')
def tools():
  import_docs()

  for script in supported_scripts:
    click.echo(script)
