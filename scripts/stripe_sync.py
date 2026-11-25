"""Pull live seat counts for each workshop from Stripe.

For every workshop in build.py with a Stripe Payment Link in `book`, this reads
the link's payment limit (the workshop's capacity) and how many payments it has
taken (seats booked), and writes them to data/workshop-seats.json. build.py
uses that file, so the page shows "N spots left" / "Sold out" on its own.

To change a workshop's capacity, change the payment limit on its Payment Link
in Stripe (Payment Links > the link > Edit > Advanced > Limit the number of
payments). The site follows within the hour.

Needs a read-only Stripe restricted key in the STRIPE_READ_KEY environment
variable (Payment Links: Read). Without it the script does nothing.
"""
import json, os, re, sys, urllib.parse, urllib.request
import base64

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'workshop-seats.json')
KEY = os.environ.get('STRIPE_READ_KEY', '').strip()


def workshops():
    """Read slug and book link for each workshop from build.py without running it."""
    src = open(os.path.join(ROOT, 'build.py'), encoding='utf-8').read()
    block = src[src.index('WORKSHOPS = ['):src.index('PASSES = [')]
    found = []
    for d in re.findall(r'dict\((.*?)\)(?:,|\s*\])', block, re.S):
        slug = re.search(r"slug='([^']+)'", d)
        book = re.search(r"book='([^']*)'", d)
        if slug:
            found.append((slug.group(1), book.group(1) if book else ''))
    return found


def stripe_links():
    links, after = {}, None
    auth = 'Basic ' + base64.b64encode((KEY + ':').encode()).decode()
    while True:
        q = {'limit': 100}
        if after:
            q['starting_after'] = after
        req = urllib.request.Request('https://api.stripe.com/v1/payment_links?' + urllib.parse.urlencode(q),
                                     headers={'Authorization': auth})
        with urllib.request.urlopen(req, timeout=30) as r:
            page = json.load(r)
        for pl in page['data']:
            links[pl['url'].rstrip('/')] = pl
        if not page.get('has_more'):
            return links
        after = page['data'][-1]['id']


def main():
    if not KEY:
        print('STRIPE_READ_KEY is not set; nothing to do.')
        return 0
    ws = [(s, b) for s, b in workshops() if 'stripe.com' in b]
    if not ws:
        print('No workshop has a Stripe link yet; nothing to do.')
        return 0
    links = stripe_links()
    seats = {}
    for slug, book in ws:
        pl = links.get(book.rstrip('/'))
        if not pl:
            print(f'{slug}: no Payment Link in Stripe matches {book}')
            continue
        cs = (pl.get('restrictions') or {}).get('completed_sessions') or {}
        entry = {'booked': int(cs.get('count') or 0)}
        if cs.get('limit'):
            entry['seats'] = int(cs['limit'])
        if not pl.get('active', True):
            entry['closed'] = True
        seats[slug] = entry
        print(slug, entry)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    old = open(OUT).read() if os.path.exists(OUT) else ''
    new = json.dumps(seats, indent=2, sort_keys=True) + '\n'
    if new != old:
        open(OUT, 'w').write(new)
        print('Updated', OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
