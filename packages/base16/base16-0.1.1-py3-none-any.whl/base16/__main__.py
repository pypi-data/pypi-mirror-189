'''Usage: base16 --encode <data> | --decode <data> [--strict] [--filter]'''

import sys

from base16 import base16


def usage():
    '''Print usage information.'''
    print(__doc__)
    sys.exit(1)

def main(args=None):
    '''Main function. Default entry point.'''
    args = args or sys.argv[1:]

    if len(args) < 2:
        usage()

    elif args[0] == '--encode':
        data = args[1]
        data = data.encode('utf-8')

        out = base16.encode(data)

        print(out)

    elif args[0] == '--decode':
        data = args[1]
        data = data.encode('utf-8')

        strict = '--strict' in args
        filter_invalid = '--filter' in args

        try:
            out = base16.decode(
                data,
                strict=strict,
                filter_invalid=filter_invalid,
            )
        except ValueError as exc:
            print(exc)
            sys.exit(1)

        print(out)

    else:
        usage()

    return 0


if __name__ == '__main__':
    sys.exit(main())
