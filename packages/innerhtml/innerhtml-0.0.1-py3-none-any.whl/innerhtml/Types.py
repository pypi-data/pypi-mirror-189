# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2023-today Artic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from re import search, findall

class Tag(object):
    def __init__(self, tag: str, /) -> None:
        self.tag: str = tag
        self._id: str = search(r"id=(.*?)", tag)
        self._class: str = search(r"class=(.*?)", tag)
        self._style: str = search(r"style=(.*?)", tag)
        self._type: str = tag.split(">")[0].split(" ")[0].removeprefix("<")
        try:
            self.content: str = tag.split(">")[1].split("<")[0]
        except IndexError:
            self.content: None = None
    
    def __repr__(self) -> str:
        return "<%s%s>" % (self._type, f" {self.content}" if self.content else "")
    
    def __eq__(self, __o: object) -> bool:
        return self.content == __o.content
    
    def __str__(self) -> str:
        return self.content

    def getAttribute(self, name: str) -> str:
        return self.tag.replace("=", " ").split(" ")[self.tag.replace("=", " ").split(" ").index(name) + 1].removeprefix('"').removesuffix('"')

    def hasAttribute(self, name: str) -> bool:
        return name in self.tag.replace("=", " ").split(" ")

class Page(object):
    def __init__(self, html: str, /) -> None:
        self.raw: str = html
        self._html: list[str] = self.raw.split("\n")
        for c in range(len(self._html)):
            self._html[c] = self._html[c].removesuffix("\r")
        else:
            self._html: tuple[str, ...] = tuple(self._html)
        self.html: list[str] = []

        for tag in self._html:
            if tag != r"\r":
                try:
                    self.html.append(f"<{tag.split('<', 1)[1]}".removesuffix(r"\r"))
                except IndexError:
                    self.html.append(f"<{tag.split('<', 1)[0]}".removesuffix(r"\r"))
            else:
                self.html.append(" ")
        else:
            self.html: tuple[str, ...] = tuple(self.html)

        self.tags: list[str] = []
        self._tags = findall(r"<(.*?)>", self.raw)
        
        for match in self._tags:
            if any(i for i in match if i in ["/", "!"]):
                continue
            self.tags.append(str(match).split(" ")[0])
        else:
            self.tags: list = list(set(self.tags))

        self.elements: list[Tag] = []
        for line in self.html:
            self.elements.append(Tag(line))

        return

    def __repr__(self) -> str:
        return self.__class__.__name__