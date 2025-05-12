import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .codesnippet import CodeSnippet, CodeSnippetCopyButton, CodeSnippetLayout

filename = os.path.join(UIX, "codesnippet", "codesnippet.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
