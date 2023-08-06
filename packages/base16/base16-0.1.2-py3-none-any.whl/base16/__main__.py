'''Usage: base16 --encode <data> | --decode <data> [--strict] [--filter]'''

import sys

import base16


def usage():
    '''Print usage information.'''
    print(__doc__)
    sys.exit(1)

def main(args=None):
    '''Main function. Default entry point.'''
    args = args or sys.argv[1:]

    command = None
    data = None
    strict = False
    filter_invalid = False

    # Parse flags and remove
    for arg in args[:]: # Copy list to avoid modifying it
        if arg == '--encode':
            command = 'encode'
            args.remove(arg)
        elif arg == '--decode':
            command = 'decode'
            args.remove(arg)
        elif arg == '--random':
            command = 'random'
            args.remove(arg)
        elif arg == '--strict':
            strict = True
            args.remove(arg)
        elif arg == '--filter':
            filter_invalid = True
            args.remove(arg)
        elif arg.startswith('--'):
            print('Unknown flag: {}'.format(arg))
            usage()

    # Parse data
    if not sys.stdin.isatty():
        data = sys.stdin.read()
        data = data.strip()

    elif len(args) > 0:
        data = args[0]

    # Check arguments
    if command is None or data is None:
        usage()

    data = data.encode('utf-8')

    # Run command
    if command == 'encode':
        result = base16.encode(data)
        sys.stdout.buffer.write(result)

    elif command == 'decode':
        try:
            result = base16.decode(
                data,
                strict=strict,
                filter_invalid=filter_invalid,
            )
        except ValueError as exc:
            print(exc)
            sys.exit(1)

        sys.stdout.buffer.write(result)

    elif command == 'random':
        length = int(data) if data.isdigit() else 16

        result = base16.random(length)
        sys.stdout.buffer.write(result)

    else:
        usage()

    # End with a newline
    sys.stdout.buffer.write(b'\n')

    return 0


if __name__ == '__main__':
    sys.exit(main())
