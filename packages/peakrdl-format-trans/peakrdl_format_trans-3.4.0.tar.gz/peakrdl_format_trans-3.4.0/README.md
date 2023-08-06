# format_trans
Import csv/xlxs transfer to systemrdl file
# usage
peakrdl formattrans test.rdl --xlsx test_excel.xlsx -o test.rdl the test.rdl (input file must) dose not affect my pak=ckage funciotn but the main pakeardl package need,so give the correct systemrdl file
# usage: peakrdl formattrans [-h] [-I INCDIR] [-t TOP] [--rename INST_NAME] [-P PARAMETER=VALUE] [--xlsx XLSX] [--csv CSV] [--remap-state STATE] -o OUTPUT [-f FILENAME] FILE [FILE ...]

transfer csv/xlxs to rdl.

options:
  -h, --help           show this help message and exit
  -f FILENAME          Specify a file containing more command line arguments

compilation args:
  FILE                 One or more input files  (********must give)
  -I INCDIR            Search directory for files included with `include "filename"
  -t TOP, --top TOP    Explicitly choose which addrmap in the root namespace will be the top-level component. If unset, The last addrmap defined will be chosen
  --rename INST_NAME   Overrides the top-component's instantiated name. By default, the instantiated name is the same as the component's type name
  -P PARAMETER=VALUE   Specify value for a top-level SystemRDL parameter

formattrans importer args:
  --xlsx XLSX          display a path of xlsx file
  --csv CSV            display a path of csv file

ip-xact importer args:
  --remap-state STATE  Optional remapState string that is used to select memoryRemap regions that are tagged under a specific remap state.

exporter args:
  -o OUTPUT            Output path(**********must give)
#my package have upload pypi