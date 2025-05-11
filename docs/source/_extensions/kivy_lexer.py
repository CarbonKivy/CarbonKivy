from pygments.lexer import RegexLexer, bygroups
from pygments.token import Comment, Keyword, Name, Number, String, Text


class KivyLexer(RegexLexer):
    """
    A simple lexer for Kivy's KvLang.
    """

    name = "KvLang"
    aliases = ["kvlang"]
    filenames = ["*.kv"]

    tokens = {
        "root": [
            (r"#.*$", Comment.Single),  # Comments
            (r"[a-zA-Z_][a-zA-Z0-9_]*:", Name.Tag),  # Widget/Property names
            (r"[a-zA-Z_][a-zA-Z0-9_]*", Name),  # Identifiers
            (r'"[^"]*"', String),  # Double-quoted strings
            (r"'[^']*'", String),  # Single-quoted strings
            (r"[+-]?\d+\.\d+", Number.Float),  # Floating point numbers
            (r"[+-]?\d+", Number.Integer),  # Integers
            (r"\s+", Text),  # Whitespace
            (r".", Text),  # Fallback for any other text
        ],
    }
