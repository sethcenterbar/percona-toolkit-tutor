import click
import os

@click.group()
@click.option('--man', is_flag=True, help="Pass this flag to display the manpage.")
@click.pass_context
def cli(ctx, man):
  """percona-toolkit-tutor is a wrapper around percona-toolkit, aimed at making the kit more discoverable.

  /d
  For more information about a command (pt-find in this example), run the following:
    ptt pt-find

  """
  ctx.ensure_object(dict)
  ctx.obj['MAN'] = man

@cli.command('pt-find', help="Find MySQL tables and execute actions, like GNU find.")
@click.pass_context
def pt_find(ctx):
  if ctx.obj['MAN']:
    click.echo("Manual page will be displayed!")
  
@cli.command('pt-summary')
def pt_summary():
  pass
  
@cli.command('pt-archiver')
def pt_archiver():
  pass
  
@cli.command('pt-fingerprint')
def pt_fingerprint():
  pass
  
@cli.command('pt-show-grants')
def pt_show_grants():
  pass
  
@cli.command('pt-table-checksum')
def pt_table_checksum():
  pass
  
@cli.command('pt-config-diff')
def pt_config_diff():
  pass
  
 
@cli.command('pt-table-sync')
def pt_table_sync():
  pass
 
@cli.command('pt-mysql-summary')
def pt_mysql_summary():
  pass
 
@cli.command('pt-table-usage')
def pt_table_usage():
  pass
  
@cli.command('pt-diskstats')
def pt_diskstats():
  pass
  
@cli.command('pt-index-usage')
def pt_index_usage():
  pass
  
@cli.command('pt-online-schema-change')
def pt_online_schema_change():
  pass
  
@cli.command('pt-upgrade')
def pt_upgrade():
  pass
  
@cli.command('pt-duplicate-key-checker')
def pt_duplicate_key_checker():
  pass
 
@cli.command('pt-variable-advisor')
def pt_variable_advisor():
  pass
 
@cli.command('pt-query-digest')
def pt_query_digest():
  pass
  
@cli.command('pt-stalk')
def pt_stalk():
  pass
  
@cli.command('pt-visual-explain')
def pt_visual_explain():
  pass
