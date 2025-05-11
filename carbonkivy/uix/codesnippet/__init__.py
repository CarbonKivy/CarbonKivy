import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .codesnippet import CodeSnippet, CodeSnippetCopyButton, CodeSnippetLayout

Builder.load_file(os.path.join(UIX, "codesnippet", "codesnippet.kv"))
