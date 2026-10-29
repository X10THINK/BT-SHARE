#!/usr/bin/env python3
"""Repair known BT SHARE Markdown links moved during repository reorganization.

Run from the repository root:
  python scripts/repair_repository_links.py --apply
  python scripts/repair_repository_links.py --check

The file edits are limited to Markdown link targets and href/src paths.
No design, binary asset, Git metadata, or absolute external URL is changed.
"""
from __future__ import annotations
import argparse
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote

MD_LINK = re.compile(r'(!?\[[^\]]*\])\(([^)]+)\)')
HTML_ATTR = re.compile(r'\b(src|href)="([^"]+)"')
EXCLUDE = {'.git','node_modules','.dart_tool','build','dist','.venv','.next'}
OWN_GITHUB = 'https://github.com/X10THINK/BT-SHARE/blob/main/'


def docs(root: Path):
    for file in sorted(root.rglob('*.md')):
        if not (set(file.relative_to(root).parts) & EXCLUDE):
            yield file


def normalize(ref: str):
    return posixpath.normpath(ref.replace('\\','/')).lstrip('/')


def fix_ref(ref: str, file: Path, root: Path) -> str:
    # Absolute links to this very repository that use stale paths are changed
    # into portable relative paths, so branch previews work as well.
    parts = ref.split('#',1)
    url, fragment = parts[0], ('#'+parts[1] if len(parts)==2 else '')
    if url.startswith(OWN_GITHUB):
        repo_path = unquote(url[len(OWN_GITHUB):])
        repo_path = repo_path.replace('Basic Documents/','First_Documents/').replace('docs/mobile-app/','FeaturE_Scope_Documentations/mobile-app/')
        dest = root / repo_path
        if dest.exists():
            rel = posixpath.relpath(repo_path, file.parent.relative_to(root).as_posix() or '.')
            return rel + fragment
        return ref
    if url.startswith(('http:','https:','mailto:','#','data:','tel:')):
        return ref
    # Repair only the two known moved directory names, including URL encoding.
    new = url.replace('Basic%20Documents/','First_Documents/').replace('Basic Documents/','First_Documents/')
    if file.parent == root:
        new = new.replace('docs/mobile-app/','FeaturE_Scope_Documentations/mobile-app/')
    return new + fragment


def modify(text: str, file: Path, root: Path) -> str:
    def md(m):
        label, ref = m.groups()
        return label + '(' + fix_ref(ref,file,root) + ')'
    text = MD_LINK.sub(md,text)
    def html(m):
        attr, val = m.groups()
        return f'{attr}="{fix_ref(val,file,root)}"'
    return HTML_ATTR.sub(html,text)


def audit(root: Path):
    checked=0; missing=[]
    for file in docs(root):
        text=file.read_text(encoding='utf-8')
        refs=[m.group(2) for m in MD_LINK.finditer(text)]
        refs += [m.group(2) for m in HTML_ATTR.finditer(text)]
        for ref in refs:
            ref=ref.split(' "',1)[0].split('#',1)[0].split('?',1)[0]
            if not ref or ref.startswith(('https:','http:','mailto:','data:','tel:','/')):
                continue
            checked += 1
            dest=(file.parent/unquote(ref))
            if not dest.exists():
                missing.append((file.relative_to(root).as_posix(),ref))
    return checked, missing


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--apply',action='store_true')
    p.add_argument('--check',action='store_true')
    args=p.parse_args()
    if not (args.apply or args.check):p.error('Specify --apply, --check or both')
    root=Path.cwd()
    if not (root/'README.md').is_file():p.error('Run from BT-SHARE project root')
    if args.apply:
        touched=[]
        for file in docs(root):
            raw=file.read_bytes(); text=raw.decode('utf-8')
            edited=modify(text,file,root)
            if edited!=text:
                # Preserve CRLF for documents from Windows clone.
                if b'\r\n' in raw and raw.count(b'\r\n') == raw.count(b'\n'):
                    edited=edited.replace('\r\n','\n').replace('\n','\r\n')
                file.write_bytes(edited.encode('utf8'))
                touched.append(file.relative_to(root).as_posix())
        print(f'Updated link targets in {len(touched)} Markdown files')
        for x in touched:print('  ',x)
    if args.check:
        checked,missing=audit(root)
        print(f'Checked {checked} local Markdown/HTML references; broken: {len(missing)}')
        for file,ref in missing:print('BROKEN',file,ref)
        if missing:raise SystemExit(1)

if __name__=='__main__':main()
