"""Produce an offline, navigable preview with no changes to deployment output."""
import os
import pathlib
import re
import shutil
import zipfile
root=pathlib.Path(__file__).resolve().parent
preview=root/'review/site'
if preview.exists():shutil.rmtree(preview)
shutil.copytree(root/'dist',preview,ignore=shutil.ignore_patterns('brand','delivery'))
domain=__import__('json').loads((root/'content/settings.json').read_text())['domain'].rstrip('/')
for page in preview.rglob('*.html'):
    def relative(match):
        attr,value=match.groups()
        value=re.sub(r'^/Site-beta/', '/', value)
        target,separator,query=value.partition('?')
        if target.startswith(('/brand/','/delivery/')):
            return f'{attr}="{domain}{value}"'
        destination=preview/target.lstrip('/')
        if target.endswith('/'):destination=destination/'index.html'
        suffix=separator+query if separator else ''
        return f'{attr}="{os.path.relpath(destination,page.parent)}{suffix}"'
    page.write_text(re.sub(r'(href|src)="(/[^" ]*)"',relative,page.read_text()))
with zipfile.ZipFile(root/'review/valerie-migueres-preview.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for file in preview.rglob('*'):
        if file.is_file():archive.write(file,file.relative_to(preview))
print('Offline preview: review/site/index.html; archive: review/valerie-migueres-preview.zip')
