"""API module

Handles"""
#══════════════════════════════════════════════════════════════════════════════
# IMPORT
from .dataclass_validate import dataclass as _dataclass_orig
from .dataclass_validate import field as _field

from collections.abc import Collection as _Collection
from collections.abc import Iterable as _Iterable
from collections import defaultdict as _defaultdict
import enum as _enum 
import itertools as _itertools
import re as _re
from string import punctuation as _punctuation 
import sys
from typing import Any as _Any
from typing import Generator as _Generator
from typing import Union as _Union

# To skip using slots on python 3.9
if sys.version_info[1] <= 9: # absorbe keyword "slots"
    def _dataclass(*args, slots = None, **kwargs):    # pragma: no cover
        return _dataclass_orig(*args, **kwargs)        # pragma: no cover
else:                                                 # pragma: no cover
    _dataclass = _dataclass_orig                     # pragma: no cover
#══════════════════════════════════════════════════════════════════════════════
# AUXILIARIES
_INDENT = '    '

class Alignment(_enum.Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3

LEFT, CENTER, RIGHT = Alignment # type: ignore

class ListingStyle(_enum.Enum):
    ORDERED = 1
    UNORDERED = 2
    DEFINITION = 3

ORDERED, UNORDERED, DEFINITION = ListingStyle # type: ignore

class TextStyle(_enum.Enum):
    BOLD = 1
    ITALIC = 2
    STRIKETHROUGH = 3
    HIGHLIGHT = 4

BOLD, ITALIC, STRIKETHROUGH, HIGHLIGHT = TextStyle # type: ignore

class Flavour(_enum.Enum):
    BASIC = 1
    EXTENDED = 2
    GITHUB = 3
    GITLAB = 4
    PYPI = 5

BASIC, EXTENDED, GITHUB, GITLAB, PYPI = Flavour # type: ignore

_re_begin = _re.compile(r'^\s*\n\s*')
_re_middle = _re.compile(r'\s*\n\s*')
_re_end = _re.compile(r'\s*\n\s*$')
def _sanitise_str(text: str):
    text = _re_begin.sub('', text)
    text = _re_end.sub('', text)
    return _re_middle.sub(' ', text)
#══════════════════════════════════════════════════════════════════════════════
def _is_collectable(obj) -> bool:
    return hasattr(obj, '_collect') and isinstance(obj, Element)
#══════════════════════════════════════════════════════════════════════════════
def _collect_iter(items: _Iterable) -> tuple[dict, dict]:
    '''Doing ordered set _Union thing

    Parameters
    ----------
    items : _Iterable
        items to be checked

    Returns
    -------
    tuple[dict, dict]
        list of unique items
    '''
    output: tuple[dict[Link, None], dict[Footnote, None]] = ({}, {})
    for item in items:
        if _is_collectable(item):
            for old, new in zip(output, item._collect()):
                old |= new
    return output
#══════════════════════════════════════════════════════════════════════════════
# ELEMENTS BASE CLASSES
@_dataclass(slots = True)
class Element:
    #─────────────────────────────────────────────────────────────────────────
    def __add__(self, other):
        return Document([self, other]) # type: ignore
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class ContainerElement(Element):
    #─────────────────────────────────────────────────────────────────────────
    def _collect(self) -> tuple[dict, dict]:
        return (self.content._collect() # type: ignore
                if _is_collectable(self.content) else ({}, {})) # type: ignore
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class IterableElement(Element):
    #─────────────────────────────────────────────────────────────────────────
    def _collect(self) -> tuple[dict, dict]:
        return _collect_iter(self.content)   # type: ignore
    #─────────────────────────────────────────────────────────────────────────
    def __iter__(self):
        return iter(self.content)   # type: ignore
#══════════════════════════════════════════════════════════════════════════════
@_dataclass
class InlineElement(Element):
    """So far only a marker class to wether element can be treated as inline"""
    pass
#══════════════════════════════════════════════════════════════════════════════
# BASIC ELEMENTS

#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Paragraph(IterableElement):
    content: list = _field(default_factory = list)
    separator: str = ''
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return self.separator.join(_sanitise_str(item) if isinstance(item, str)
                                   else str(item) for item in self.content)
    #─────────────────────────────────────────────────────────────────────────
    def __iadd__(self, other):
        if isinstance(other, InlineElement):
            self.content.append(other)
            return self
        elif isinstance(other, Paragraph):
            self.content += other.content
            return self
        else:
            raise TypeError(f"+= has not been implemented for Paragraph with object {repr(other)} type '{type(other).__name__}'")
#══════════════════════════════════════════════════════════════════════════════
_markers = {BOLD:          '**',
            ITALIC:        '*',
            STRIKETHROUGH: '~~',
            HIGHLIGHT:     '=='}
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Text(ContainerElement, InlineElement):
    '''Stylised text

    Parameters
    ----------
    text : has method str 
        text to be containes
    style: set[str]
        style of the text, options are: bold, italic, strikethrough, subscript, superscript, emphasis

    Raises
    ------
    ValueError
        for invalid style attributes
    '''
    content: _Any
    style: set[TextStyle] = _field(default_factory = set)
    level: int = 0 # Normal = 0, subscript = -1, superscipt = 1
    #─────────────────────────────────────────────────────────────────────────
    def __post_init__(self):
        if not -1 <= self.level <= 1:
            raise ValueError(f'Text level must be 0, -1 or 1, not {self.level}')
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        # superscipt and subcript have to be the innermost
        if self.level == 1:
            text = f'^{self.content}^'
        elif self.level == -1:
            text = f'~{self.content}~'
        else:
            text = str(self.content)

        for substyle in self.style:
            marker = _markers[substyle]
            text = f'{marker}{text}{marker}'
        return text
    #─────────────────────────────────────────────────────────────────────────
    def bold(self):
        self.style.add(BOLD)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def unbold(self):
        self.style.discard(BOLD)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def italicize(self):
        self.style.add(ITALIC)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def unitalicize(self):
        self.style.discard(ITALIC)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def strike(self):
        self.style.add(STRIKETHROUGH)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def unstrike(self):
        self.style.discard(STRIKETHROUGH)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def highlight(self):
        self.style.add(HIGHLIGHT)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def unhighlight(self):
        self.style.discard(HIGHLIGHT)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def superscribe(self):
        self.level = 1
        return self
    #─────────────────────────────────────────────────────────────────────────
    def subscribe(self):
        self.level = -1
        return self
    #─────────────────────────────────────────────────────────────────────────
    def normal(self):
        '''Removes superscript or subscript'''
        self.level = 0
        return self
    #─────────────────────────────────────────────────────────────────────────
    def clear(self):
        '''Removes all formatting'''
        self.style = set()
        return self
#══════════════════════════════════════════════════════════════════════════════
markers = {UNORDERED: (lambda : _itertools.repeat('- '), 2),
           ORDERED: (lambda : (f'{n}. ' for n in _itertools.count(1, 1)), 3),
           DEFINITION: (lambda : _itertools.repeat(': '), 2)}
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Listing(IterableElement):
    style: ListingStyle
    content: _Iterable
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        prefixes, prefix_length = markers[self.style]
        output = []
        for item, prefix in zip(self.content, prefixes()):
            if (isinstance(item, tuple)
                and len(item) == 2
                and isinstance(item[1], Listing)):
                output.append(prefix + str(item[0]))
                output.append(_INDENT + str(item[1]).replace('\n', '\n'+ _INDENT))
            else:
                output.append(prefix + str(item).replace('\n',
                                                         '\n'+ ' '* prefix_length))
        return '\n'.join(output)
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Checkbox(ContainerElement):
    checked: bool
    content: _Any
    #─────────────────────────────────────────────────────────────────────────
    def __bool__(self) -> bool:
        return self.checked
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        content = (_sanitise_str(self.content)
                  if isinstance(self.content, str)
                  else self.content)
        return (f'[{"x" if self else " "}] {content}')
    #─────────────────────────────────────────────────────────────────────────
    def __add__(self, other):
        raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'")
#══════════════════════════════════════════════════════════════════════════════
def make_checklist(items: _Iterable[tuple[bool, _Any]]):
    return Listing(UNORDERED, (Checkbox(*item) for item in items)) # type: ignore
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Heading(ContainerElement):
    level: int
    content: _Any
    alt_style: bool = False # Underline instead of #
    in_TOC: bool = True
    #─────────────────────────────────────────────────────────────────────────
    def __post_init__(self) -> None:
        if self.level <= 0:
            raise ValueError(f'Level must be greater that 0, not {self.level}')
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        text = str(self.content)
        toccomment = '' if self.in_TOC else ' <!-- omit in toc -->'
        if self.alt_style and (self.level == 1 or self.level == 2):
            return ''.join((text, toccomment, '\n',
                            ('=', '-')[self.level - 1] * len(text)))
        else: # The normal style with #
            return ''.join((self.level * "#", ' ', text, toccomment))
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class Code(InlineElement):
    content: _Any
    def __str__(self) -> str:
        return f'`{self.content}`'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class CodeBlock(InlineElement):
    content: _Any
    language: _Any = ''
    _tics: int = 3
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        text = str(self.content)
        language = _sanitise_str(str(self.language))
        self._tics = (self.content._tics + 1
                      if isinstance(self.content, CodeBlock)
                      else self._tics)
        return f'{"`" * self._tics}{language}\n{text}\n{"`" * self._tics}'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class Address(InlineElement):
    content: _Any
    def __str__(self) -> str:
        return f'<{self.content}>'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class Link(InlineElement):
    """Do not change `_index`"""
    content: _Any
    target: _Any
    title: _Any = None
    _index: int = 0
    #─────────────────────────────────────────────────────────────────────────
    def _collect(self) -> tuple[dict, dict]:
        return ({} if self.title is None else {self: None},
                self.content._collect()[1] if _is_collectable(self.content) else {})
    #─────────────────────────────────────────────────────────────────────────
    def __hash__(self) -> int:
        return hash(str(self.target)) + hash(str(self.title)) + hash(str(self.content))
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return (f'[{self.content}][{self._index}]' if self._index else
                f'[{self.content}]({self.target})')
#══════════════════════════════════════════════════════════════════════════════
# Table
def _pad(items: list[str],
         widths: _Iterable[int],
         alignments: _Iterable[Alignment]
         ) -> _Generator[str, None, None]:
    for alignment, item, width in zip(alignments, items, widths):
        if alignment == LEFT:
            yield f'{item}{(width - len(item)) * " "}'
        elif alignment == CENTER:
            item += ((width - len(item))//2) * ' '
            yield f'{(width - len(item)) * " "}{item}'
        elif alignment == RIGHT:
            yield f'{(width - len(item)) * " "}{item}'
        else:
            raise ValueError(f'alignment {alignment} not recognised')
#══════════════════════════════════════════════════════════════════════════════
def _str_row_sparse(row: _Iterable[str]):
    return '| ' + ' | '.join(row) + ' |'
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Table(IterableElement):
    header: _Iterable
    content: list[_Collection] = _field(default_factory = list)
    alignment: _Collection[Alignment] = _field(default_factory = list)
    compact: bool = False
    #─────────────────────────────────────────────────────────────────────────
    def _collect(self) -> tuple[dict, dict]:
        output = _collect_iter(self.header)
        for row in self.content:
            for old, new in zip(output, _collect_iter(row)):
                old |= new
        return output
    #─────────────────────────────────────────────────────────────────────────
    def append(self, row: _Collection) -> None:
        if hasattr(row, '__iter__'):
            self.content.append(row)
        else:
            raise TypeError(f"'{type(row)}' is not _Iterable")
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        header = [str(item) for item in self.header]
        headerlen = len(header)

        max_rowlen = headerlen
        for row in self.content:
            if len(row) > max_rowlen:
                max_rowlen = len(row)
        header += ['']*(max_rowlen - len(header))
        alignment = list(self.alignment) + [LEFT] * (max_rowlen - len(self.alignment))
        alignment_row: list[str] = []
        if self.compact:
            output = ['|'.join(header)]
            # Alignments

            for i, item in enumerate(alignment):
                if item == LEFT:
                    alignment_row.append(':--')
                elif item == CENTER:
                    alignment_row.append(':-:')
                elif item == RIGHT:
                    alignment_row.append('--:')
            output.append('|'.join(alignment_row))
            for row in self.content:
                row = list(row) + [''] * (max_rowlen - len(row))
                output.append('|'.join(str(item) for item in row))
        else:
            # maximum cell widths
            max_widths = [max(len(item), 3) for item in header] + (max_rowlen - headerlen) * [3]
            content = [[str(item) for item in row] for row in self.content]
            for row in content:
                for i, cell in enumerate(row):
                    if len(cell) > max_widths[i]:
                        max_widths[i] = len(cell)

            output = [_str_row_sparse(_pad(header, max_widths, alignment))]
            # Alignments and paddings
            for item, width in zip(alignment, max_widths):
                if item == LEFT:
                    alignment_row.append(':'+ (width - 1) * '-')
                elif item == CENTER:
                    alignment_row.append(':'+ (width - 2) * '-' + ':')
                elif item == RIGHT:
                    alignment_row.append((width - 1) * '-' + ':')
            output.append(_str_row_sparse(item for item in alignment_row))
            for row in content:
                row = list(row) + [''] * (max_rowlen - len(row))
                output.append(_str_row_sparse(_pad(row, max_widths, alignment)))
        return '\n'.join(output)
#══════════════════════════════════════════════════════════════════════════════
# EXTENDED ELEMENTS
@_dataclass(slots = True)
class Footnote(InlineElement):
    """Do not change `_index`"""
    content: _Any
    _index: int = 0 # TODO something with `_field` to prevent assignment at init
    #─────────────────────────────────────────────────────────────────────────
    def _collect(self) -> tuple[dict, dict]:
        return {}, {self: None}
    #─────────────────────────────────────────────────────────────────────────
    def __hash__(self) -> int:
        return hash(str(self.content))
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return f'[^{self._index}]'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Math(InlineElement):
    text: _Any
    flavour: Flavour = GITHUB
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        if self.flavour == GITHUB:
            return f'${self.text}$'
        elif self.flavour == GITLAB:
            return f'$`{self.text}`$'
        raise ValueError(f'Flavour {self.flavour} not recognised')
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class MathBlock(Element):
    text: _Any
    flavour: Flavour = GITHUB
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        if self.flavour == GITHUB:
            return f'$$\n{self.text}\n$$'
        elif self.flavour == GITLAB:
            return f'```math\n{self.text}\n```'
        raise ValueError(f'Flavour {self.flavour} not recognised')
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class QuoteBlock(ContainerElement):
    content: _Any
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return '> ' + str(self.content).replace('\n', '\n> ')
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class HRule(Element):
    def __str__(self) -> str:
        return '---'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class Image(Element):
    path: _Any
    alt_text: _Any = ''
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return f'![{self.alt_text}]({self.path})'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True)
class Emoji(InlineElement):
    """https://www.webfx.com/tools/emoji-cheat-sheet/"""
    code: _Any
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return f':{self.code}:'
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class TOC(Element):
    level: int = 4
    _text: str = ''
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        return self._text
#══════════════════════════════════════════════════════════════════════════════
def _preprocess_document(content: _Iterable
                ) -> tuple[list,
                           dict[int, list],
                           int,
                           list,
                           dict[Link, None],
                           dict[Footnote, None]]:
    '''Iterates through document tree and collects
        - TOCs
        - headers
        - references
        - footnotes
    and cleans string objects'''
    items: tuple[dict[Link, None],
                 dict[Footnote, None]] = ({}, {})
    new_content = []
    TOCs: dict[int, list[TOC]] = _defaultdict(list)
    headings = []
    top_level = 999
    for item in content:
        if isinstance(item, str):
            new_content.append(_sanitise_str(item).strip())
        else:
            new_content.append(item)
            if isinstance(item, TOC):
                TOCs[item.level] += [item]
            else:
                if isinstance(item, Heading) and item.in_TOC:
                    headings.append(item)
                    if item.level < top_level:
                        top_level = item.level
                if _is_collectable(item):
                    for old, new in zip(items, item._collect()):
                        old |= new
    return new_content, TOCs, top_level, headings, *items
#══════════════════════════════════════════════════════════════════════════════
def _process_footnotes(footnotes: dict[Footnote, None]):
    footnotelines = []
    for index, footnote in enumerate(footnotes, start = 1):
        footnote._index = index
        footnotelines.append(f'[^{index}]: {footnote.content}')
    return '\n'.join(footnotelines)
#══════════════════════════════════════════════════════════════════════════════
def _process_references(references: dict[Link, None]) -> str:
    reftargets: dict[str, list[Link]] = _defaultdict(list)
    for link in references: # matching links to references
        reftargets[f'<{link.target}> "{link.title}"'] += [link]
    reflines = []
    for index, (reftext, links) in enumerate(reftargets.items(), start = 1):
        for link in links: # Adding indices to links and reftext
            link._index = index
        reflines.append(f'[{index}]: {reftext}')
    return '\n'.join(reflines)
#══════════════════════════════════════════════════════════════════════════════
def _process_header(language, content) -> str:
    language = str(language).strip().lower()
    if language == 'yaml':
        return f'---\n{content}\n---'
    elif language == 'toml':
        return f'+++\n{content}\n+++'
    elif language == 'json':
        return f';;;\n{content}\n;;;'
    else:
        return f'---{language}\n{content}\n---'
#══════════════════════════════════════════════════════════════════════════════
def _translate(text, *args):
    return str(text).translate(''.maketrans(*args))
#══════════════════════════════════════════════════════════════════════════════
def _heading_ref_texts(text: str) -> tuple[str, str]:
    '''Generates visible link text and internal link target'''
    return (_translate(text, '', '', '[]'),
            '#' + _translate(text, ' ', '-', _punctuation).lower())
#══════════════════════════════════════════════════════════════════════════════
def _process_TOC(TOCs, headings, top_level) -> None:
    '''Generates table of content string and sets it to correct TOCs'''
    refcounts: dict[str, int] = {} # {reference: number of headings}
    TOCtexts: dict[int, list[str]] = _defaultdict(list) # {level: texts}
    for heading in headings:
        text, ref = _heading_ref_texts(heading.content)

        if ref in refcounts: # Handling multiple same refs
            refcounts[ref] += 1
            ref += str(refcounts[ref]) 
        else:
            refcounts[ref] = 0

        line = '- '.join(((heading.level - top_level) * _INDENT,
                            f'[{text}]({ref})'))

        for level in TOCs:
            if heading.level <= level:
                TOCtexts[level] += [line]

    for level, toclist in TOCs.items(): # Adding appropriate texts
        text = '\n'.join(TOCtexts[level])
        for toc in toclist:
            toc._text = text
#══════════════════════════════════════════════════════════════════════════════
@_dataclass(slots = True, validate = 'middle') # type: ignore
class Document(IterableElement):
    content: list = _field(default_factory = list)
    header_language_and_text: _Union[tuple[()],
                                    tuple[_Any, _Any]] = _field(
                                        default_factory = tuple) # type: ignore
    #─────────────────────────────────────────────────────────────────────────
    def __add__(self, item):
        if isinstance(item, self.__class__):
            self.content += item.content
        else:
            self.content.append(item)
        return self
    #─────────────────────────────────────────────────────────────────────────
    def __iadd__(self, item):
        return self.__add__(item)
    #─────────────────────────────────────────────────────────────────────────
    def __str__(self)  -> str:
        content, TOCs, top_level, headings, refs, footnotes = _preprocess_document(self.content)

        if self.header_language_and_text: # Making heading
            content.insert(0, _process_header(*self.header_language_and_text))

        if footnotes: # Handling footnotes
            content.append(_process_footnotes(footnotes))

        if refs: # Handling link references
            content.append(_process_references(refs))

        if TOCs and headings: # Creating TOC
            _process_TOC(TOCs, headings, top_level)

        return '\n\n'.join(str(item) for item in content)