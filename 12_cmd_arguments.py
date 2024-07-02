# argparse
import argparse
import os

parser = argparse.ArgumentParser(description="Usage of multilingual dictionary")

# Kötelező argumentumok
parser.add_argument(
    "-l",
    "--language",
    required=True,
    choices=["English", "Hungarian", "German", "French"],
    help="Set the language of the given word",
)
parser.add_argument("-w", "--word", required=True, type=str, help="Word")

# Opcionális argumentumok
parser.add_argument(
    "-v", "--verbose", action="store_true", help="Increase output verbosity"
)
parser.add_argument(
    "-d", "--definition", type=str, help="Provide a definition for the word"
)
parser.add_argument(
    "-t", "--translation", nargs="+", help="Provide translations for the word"
)
parser.add_argument(
    "-n",
    "--number",
    type=int,
    default=1,
    help="Specify the frequency or importance of the word",
)

args = parser.parse_args()

print(f"Language: {args.language}")
print(f"Word: {args.word}")
print(f"Frequency/Importance: {args.number}")

if args.verbose:
    print("Verbose mode ON")

if args.definition:
    print(f"Definition: {args.definition}")

if args.translation:
    print(f"Translations: {', '.join(args.translation)}")

# python3 12_cmd_arguments.py -l English -w hello
# python3 12_cmd_arguments.py -l German -w hallo -v
# python3 12_cmd_arguments.py -l French -w bonjour -d "A common greeting"
# python3 12_cmd_arguments.py -l Hungarian -w szia -t hello hi hey
# python3 12_cmd_arguments.py -l English -w goodbye -n 10
# python3 12_cmd_arguments.py -l German -w tschüss -d "A casual farewell" -t bye ciao adieu -n 3 -v
