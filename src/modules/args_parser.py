from argparse import ArgumentParser


def args_parser():

    arg_parse = ArgumentParser()

    arg_parse.add_argument("-i", "--image", default=None, required=True,
                           help="path to Image file")
    arg_parse.add_argument("-o", "--output", default=None,
                           help="path to Output file")
    arg_parse.add_argument("-p", "--predict", default=None, action='store_true',
                           help="use this argument when want to make prediction about the image")
    arg_parse.add_argument("-d", "--detect", default=None, action='store_true',
                           help="use this argument when want to detect objects in the image")

    args = vars(arg_parse.parse_args())

    return args
