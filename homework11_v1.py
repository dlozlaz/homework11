import argparse
parser = argparse.ArgumentParser(description='argparse capitalize')
parser.add_argument("input_file", default=None, help=("Input file to read"))
parser.add_argument("output_file", default=None, help=("Output file to read"))
parser.add_argument('-r', '--repeat', action="store_true", help='repeat text 2 times')


args = parser.parse_args()

def capitalize(input_file, output_file, repeat=False):
    """Changes the text to capital letters and writes it in output file"""

    with open(input_file, encoding='utf-8') as input_file:
        content = input_file.read()
        capitalized_content = content.upper()
       
    with open(output_file, mode='w', encoding='utf-8') as output_file:
        
        if repeat:
            output_file.write(capitalized_content * 2)
        else:
            output_file.write(capitalized_content)

capitalize(args.input_file, args.output_file, args.repeat)