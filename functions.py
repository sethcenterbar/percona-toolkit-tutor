import yaml
import click

supported_scripts = []

def import_docs(scripts=False):
  """
  Pulls in yaml from docs/tools.yaml, the tools 'database'
  """
  with open('docs/tools.yaml') as f:
    doc = yaml.safe_load(f)

  for tool in doc['tools']:
    supported_scripts.append(tool['name'])

  if scripts:
    return supported_scripts
  else:
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
    click.echo(click.style('\nInfo about ' + tool_name + "\n", fg='green'))
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
    click.echo(click.style('Blog Posts about ' + tool_name, fg='green'))

    postnum = 1
    for post in tool['blog_posts']:
      click.echo(click.style("\nPost #" + str(postnum), fg='yellow'))
      click.echo("    Description: " + post['description'])
      click.echo("           Link: " + post['link'])
      postnum = postnum + 1

def output_examples(tool_name):
  """
  Given a tool_name, this function echos out each one of its blog posts 
  """

  tool = import_tool_from_docs(tool_name)

  if tool:
    click.echo(click.style('Relevant examples of ' + tool_name, fg='green'))

    example_num = 1
    for post in tool['examples']:
      click.echo(click.style("\nExample #" + str(example_num), fg='yellow'))
      click.echo("    Description: " + post['description'])
      click.echo("        Command: " + post['command'])
      example_num = example_num + 1