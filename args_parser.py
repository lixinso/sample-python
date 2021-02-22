# https://stackoverflow.com/questions/8368110/python-argparse-subcommand-subcommand


import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser_subparsers = parser.add_subparsers()
sub = parser_subparsers.add_parser('sub')
sub_subparsers = sub.add_subparsers()
sub_sub = sub_subparsers.add_parser('sub_sub')
sub_sub_subparsers = sub_sub.add_subparsers()
sub_sub_sub = sub_sub_subparsers.add_parser('sub_sub_sub')
