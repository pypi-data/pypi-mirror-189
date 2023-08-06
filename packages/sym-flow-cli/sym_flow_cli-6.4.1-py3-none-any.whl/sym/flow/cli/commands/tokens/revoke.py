import click

import sym.flow.cli.helpers.output as cli_output
from sym.flow.cli.helpers.global_options import GlobalOptions


@click.command(name="revoke", short_help="Revoke a Sym Token")
@click.make_pass_decorator(GlobalOptions, ensure=True)
@click.argument("jti")
def tokens_revoke(options: GlobalOptions, jti: str) -> None:
    """
    Revokes a token with the given identifier
    """
    options.sym_api.revoke_token(jti)
    cli_output.success(f"Successfully revoked token with identifier {jti}")
