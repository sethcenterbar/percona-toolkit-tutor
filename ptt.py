import click
import os
import yaml

supported_scripts = []

def import_docs():
  """
  Pulls in yaml from docs/tools.yaml, the tools 'database'
  """
  with open('docs/tools.yaml') as f:
    doc = yaml.safe_load(f)

  for tool in doc['tools']:
    supported_scripts.append(tool['name'])

  return doc

def import_tool_from_docs(tool_name):
  """
  This function pulls a specific tool from the documentation
  """
  doc = import_docs()
  
  if tool_name in supported_scripts:
    this_tool = None
    for tool in doc['tools']:
      if tool['name'] == tool_name:
        this_tool = tool
        break
    return this_tool
  else:
    click.echo(click.style("\n" + tool_name + " is not a currently supported tool",fg='red'))

    click.echo("\nPlease use a valid tool name from the list below")
    for script in supported_scripts:
      click.echo("\t" + script)
   
def output_info(tool_name):

  tool = import_tool_from_docs(tool_name)
  
  if tool:
    click.echo(click.style('\n//Info about ' + tool_name + "\n", fg='green'))
    click.echo("     Name: " + tool['name'])
    click.echo("  Summary: " + tool['summary'])
    click.echo("Situation: " + tool['situation'])
    click.echo("\n")


def output_blog_posts(tool_name):
  """
  Given a tool_name, this function echos out each one of its blog posts 
  """

  tool = import_tool_from_docs(tool_name)

  if tool:
    click.echo(click.style('//Blog Posts about ' + tool_name, fg='green'))

    postnum = 1
    for post in tool['blog_posts']:
      click.echo("\nPost #" + str(postnum))
      click.echo("    Description: " + post['description'])
      click.echo("           Link: " + post['link'])
      postnum = postnum + 1

def output_examples(tool_name):
  """
  Given a tool_name, this function echos out each one of its blog posts 
  """

  tool = import_tool_from_docs(tool_name)

  if tool:
    click.echo(click.style('//Relevant examples of ' + tool_name, fg='green'))

    example_num = 1
    for post in tool['examples']:
      click.echo("\nExample #" + str(example_num))
      click.echo("    Description: " + post['description'])
      click.echo("        Command: " + post['command'])
      example_num = example_num + 1


    
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

  output_info(tool)
  output_examples(tool)
  output_blog_posts(tool)

@cli.command(help="Show examples of a given tool")
@click.argument('tool')
def examples(tool):
  """
  Examples allows you to pass the name of a supported percona-toolkit tool and retreive relevant examples about it
  """
  output_examples(tool)

@cli.command(help="Useful links that reference a given tool")
@click.argument('tool')
def blog(tool):
  """
  Blog allows you to pass the name of a supported percona-toolkit tool and retrieve relevant blog posts about it
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
