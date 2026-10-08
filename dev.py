"""Serve the preview with its GitHub Pages project path; development only."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

class PreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if urlsplit(path).path == '/Site-beta':
            path = '/'
        elif path.startswith('/Site-beta/'):
            path = path[len('/Site-beta'):]
        return super().translate_path(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    handler = partial(PreviewHandler, directory=str(Path(__file__).parent / 'dist'))
    print(f'Preview on port {args.port}, at /Site-beta/fr/ and /Site-beta/en/', flush=True)
    ThreadingHTTPServer(('0.0.0.0', args.port), handler).serve_forever()
