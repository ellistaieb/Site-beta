"""Produce an offline, navigable preview with no changes to deployment output."""
import os
import pathlib
import re
import shutil
import zipfile
root=pathlib.Path(__file__).resolve().parent
preview=root/'review/site'
shutil.copytree(root/'dist',preview,dirs_exist_ok=True)
for page in preview.rglob('*.html'):
    def relative(match):
        attr,value=match.groups()
        value=re.sub(r'^/Site-beta/', '/', value)
        target,separator,query=value.partition('?')
        destination=preview/target.lstrip('/')
        if target.endswith('/'):destination=destination/'index.html'
        suffix=separator+query if separator else ''
        return f'{attr}="{os.path.relpath(destination,page.parent)}{suffix}"'
    page.write_text(re.sub(r'(href|src)="(/[^" ]*)"',relative,page.read_text()))
with zipfile.ZipFile(root/'review/valerie-migueres-preview.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for file in preview.rglob('*'):
        if file.is_file():archive.write(file,file.relative_to(preview))
print('Offline preview: review/site/index.html; archive: review/valerie-migueres-preview.zip')
