from pathlib import Path
from jinja2 import Template
import re

from strstyle.__main__ import COMMAND_TO_FUNCTION_MAP


colors_functions_regex = re.compile(
    r"(?<=def )\w+(?=\(str_body: str\) \-> str:)", re.MULTILINE)

repo_root = Path(__file__).parent.parent
j2_readme_path = repo_root / 'resources' / 'README.j2'
readme_path = repo_root / 'README.md'
code_file = repo_root / 'strstyle' / 'str_style.py'
j2_readme_template = Template(j2_readme_path.read_text(), autoescape=True)
colors = re.finditer(colors_functions_regex, code_file.read_text())
readme_path.write_text(j2_readme_template.render(
    colors=map(lambda x: x.group(), colors),
    cli_colors=COMMAND_TO_FUNCTION_MAP.keys()
))
