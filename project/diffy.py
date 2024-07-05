import difflib
import re

from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text


def highlight_word_differences(line1, line2):
    # Split lines into words
    words1 = line1.split()
    words2 = line2.split()

    # Compare words
    matcher = difflib.SequenceMatcher(None, words1, words2)
    result1 = Text()
    result2 = Text()

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            result1.append(" ".join(words1[i1:i2]) + " ")
            result2.append(" ".join(words2[j1:j2]) + " ")
        elif tag == "replace":
            result1.append(" ".join(words1[i1:i2]) + " ", style="bold red")
            result2.append(" ".join(words2[j1:j2]) + " ", style="bold green")
        elif tag == "delete":
            result1.append(" ".join(words1[i1:i2]) + " ", style="bold red")
        elif tag == "insert":
            result2.append(" ".join(words2[j1:j2]) + " ", style="bold green")

    return result1, result2


def highlight_regex_matches(text, pattern):
    highlighted_text = Text()
    last_end = 0
    for match in re.finditer(pattern, text):
        start, end = match.span()
        highlighted_text.append(text[last_end:start])
        highlighted_text.append(text[start:end], style="bold yellow")
        last_end = end
    highlighted_text.append(text[last_end:])
    return highlighted_text


def generate_statistics(original, new, pattern=""):
    stats = {
        "Total Lines": len(original.splitlines()),
        "Total Words Original": len(original.split()),
        "Total Words New": len(new.split()),
        "Regex Matches": len(re.findall(pattern, original)) if pattern else 0,
        "Changes": sum(
            1
            for tag, _, _, _, _ in difflib.SequenceMatcher(
                None, original, new
            ).get_opcodes()
            if tag != "equal"
        ),
    }
    return stats


def display_statistics(stats):
    table = Table(
        show_header=True, header_style="bold magenta", box=box.MINIMAL_DOUBLE_HEAD
    )
    table.add_column("Statistic", style="dim", width=50)
    table.add_column("Value", style="dim", width=50)

    for key, value in stats.items():
        table.add_row(key, str(value))

    return table


def side_by_side_diff(original, new, pattern=""):
    console = Console()
    table = Table(
        show_header=True, header_style="bold magenta", box=box.MINIMAL_DOUBLE_HEAD
    )
    table.add_column("Original Text", style="dim", width=50)
    table.add_column("New Text", style="dim", width=50)

    original_lines = original.splitlines()
    new_lines = new.splitlines()

    max_lines = max(len(original_lines), len(new_lines))
    for i in range(max_lines):
        if i < len(original_lines):
            line1 = original_lines[i]
        else:
            line1 = ""

        if i < len(new_lines):
            line2 = new_lines[i]
        else:
            line2 = ""

        if pattern:
            highlighted_line1 = highlight_regex_matches(line1, pattern)
            highlighted_line2 = Text(line2)
        else:
            highlighted_line1, highlighted_line2 = highlight_word_differences(
                line1, line2
            )

        table.add_row(highlighted_line1, highlighted_line2)

    console.print(table)

    # Generate and display statistics
    stats = generate_statistics(original, new, pattern)
    stats_table = display_statistics(stats)
    console.print(stats_table)


if __name__ == "__main__":
    original_text = """This is the3434 original text123.
    It has multiple lines.
    Here is the555 third line."""

    pattern = r"\d+"
    new_text = re.sub(pattern, "", original_text)

    side_by_side_diff(original_text, new_text, pattern)
