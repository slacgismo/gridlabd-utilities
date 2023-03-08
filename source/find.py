"""Find elements in a GridLAB-D CSV, GLM, or JSON file

Syntax: gridlabd find INPUT.{csv,glm,json} SPEC [-o|--output=OUTPUT.{csv,glm,json}]

Installation:

	$ curl -sL https://rawusercontent.github.com/slacgismo/gridlabd-utilities/main/install.sh | sh
	$ gridlabd utility get find

Examples:

	$ gridlabd find https://models.gridlabd.us/master/gridlabd-4/IEEE/13.glm class=load
"""

import sys, os, json, pandas

E_OK = 0
E_INVALID = 1
E_SYNTAX = 9

def error(msg,code=None):
	printf(f"ERROR [find]: {msg} (code {CODE})",file=sys.stderr)


if len(sys.argv) < 3:
	print(__doc__.split("\n")[2],file=sys.stderr)
	quit(E_SYNTAX)

INPUT = None
SPEC = None
FORMAT = "csv"
OUTPUT = "/dev/stdout"

for arg in sys.argv[1:]:
	if "=" in arg:
		opt = arg.split('=')
		tag = opt[0]
		value = "=".join(opt[1:]).split(",")
		if len(value) == 1:
			value = value[0]
	else:
		tag = arg
		value = True

	if INPUT is None:
		INPUT = arg
	elif SPEC is None:
		SPEC = arg
	elif tag in ['-o','--output']:
		OUTPUT = value if value else "/dev/stdout"
	else:
		error(f"invalid option '{arg}'",E_SYNTAX)

error("not implemented",E_INVALID)
