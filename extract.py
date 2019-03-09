import argparse
import io
import os
import sqlite3
from base64 import b64encode

import qrcode
from qrcode.image.pil import PilImage

ap = argparse.ArgumentParser()
ap.add_argument('database', help='the sqlite database to read')
args = ap.parse_args()

print("""<!doctype html>
<html>
<body>
<table border=1 cellpadding=25>
<tbody>
""")

db = sqlite3.connect(os.path.realpath(args.database))
cur = db.execute('SELECT * FROM accounts')
cols = [d[0] for d in cur.description]
for row in cur:
    row = dict(zip(cols, row))
    url = f"otpauth://totp/{row['email']}?secret={row['secret']}&issuer={row['issuer']}"
    img = qrcode.make(url, image_factory=PilImage, border=0)
    imgio = io.BytesIO()
    img.save(imgio, format="PNG")
    with open('x.png', 'wb') as outf:
        outf.write(imgio.getvalue())
    img_url = 'data:image/png;base64,' + b64encode(imgio.getvalue()).decode()
    print(f"""
    <tr>
    <td><img src="{img_url}" width=200></td>
    <td>{row['email']}</td>
    </tr>
    """)

print("""
</tbody>
</table>
</body>
</html>
""")
