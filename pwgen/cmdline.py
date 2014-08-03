import pwgen
import argparse

"""

    Contribution at Aug 2014 by Luar Roji <cyberplant@gmail.com>

    This module adds the command line interface to be able to run as the
    regular pwgen.

"""


def main(data=None):
    parser = argparse.ArgumentParser(description='random PassWord GENerator')

    parser.add_argument('pw_length', default='8', type=int,
                        nargs='?',
                        help="Password length")

    parser.add_argument('--capitalize', '-c', action='store_true',
                        dest="capitalize",
                        help="Include at least one capital letter in "
                             "the password")

    parser.add_argument('--no-capitalize', '-A', action='store_true',
                        dest="no_capitalize",
                        help="Don't include capital letters in the password")

    parser.add_argument('--numerals', '-n', action='store_true',
                        dest='numerals',
                        help="Include at least one number in the password")
    parser.add_argument('--no-numerals', '-0', action='store_true',
                        dest='no_numerals',
                        help="Don't include numbers in the password")

    parser.add_argument('--symbols', '-y', action='store_true', dest='symbols',
                        help="Include at least one special symbol in "
                             "the password")

    # parser.add_argument('--secure', '-s', action='store_true', dest='secure',
    #                     help="Generate completely random passwords")

    parser.add_argument('--ambiguous', '-B', action='store_true',
                        dest='no_ambiguous',
                        help="Don't include ambiguous characters in "
                             "the password")

    # parser.add_argument('-H or --sha1=path/to/file[#seed]
    #                     help="Use sha1 hash of given file as a (not so) "
    #                          "random generator")

    # parser.add_argument('-C', action='store_true', dest='print_in_columns',
    #                     help="Print the generated passwords in columns")

    parser.add_argument('-1', action='store_const', const=1, default='160',
                        dest='num_pw',
                        help="Don't print the generated passwords in columns")

    # parser.add_argument('--no-vowels', '-v', action='store_false',
    #                     dest='vowels',
    #                     help="Do not use any vowels so as to avoid
    #                          "accidental nasty words")

    args = parser.parse_args()

    d = vars(args)

    result = pwgen.pwgen(**d)

    if type(result) == list:
        for y in range(20):
            print " ".join([result.pop() for x in range(8)])
    else:
        print result
