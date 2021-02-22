# https://stackoverflow.com/questions/8368110/python-argparse-subcommand-subcommand

import argparse


def test_sub_sub_sub(args):
    print("print from sub_sub_sub")

parser = argparse.ArgumentParser(prog='PROG')
parser_subparsers = parser.add_subparsers()
sub = parser_subparsers.add_parser('sub')
sub_subparsers = sub.add_subparsers()
sub_sub = sub_subparsers.add_parser('sub_sub')

sub_sub_subparsers = sub_sub.add_subparsers()
sub_sub_sub = sub_sub_subparsers.add_parser('sub_sub_sub')
sub_sub_sub.set_defaults(func=test_sub_sub_sub)

args = parser.parse_args()


if args.func:
    args.func(args)


'''

Test:


% python3 args_parser.py sub sub_sub sub_sub_sub
print from sub_sub_sub

% python3 args_parser.py sub sub_sub            
Traceback (most recent call last):
  File "args_parser.py", line 22, in <module>
    if args.func:
AttributeError: 'Namespace' object has no attribute 'func'

'''
