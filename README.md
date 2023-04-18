Domain Finder tool
========


## Usage 

Git clone the repo. 

```bash
git clone https://github.com/MiichaelKlimenko/domain_finder/
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Run domain_finder.py

```bash
python3 domain_finder.py

usage: python3 domain_finder.py --company <name> [--company-in-domain]
```
`--company-in-domain` specifies if found domain should contain company's name.

Examples:
```bash
python3 domain_finder.py --company hackerone

blog-hackerone.com
cloudflaressl.com
enorekcah.com
hacker.one
hackerone-ext-content.com
hackerone-user-content.com
hackerone.ae
hackerone.co.me
hackerone.co.za
hackerone.com
hackerone.com.ph
hackerone.com.ua
hackerone.design
hackerone.ee
hackerone.engineer
hackerone.frl
hackerone.lt
hackerone.md
hackerone.net
hackerone.pw
hackerone.us
hackeronecommunity.com
hackeronemail.com
hackeronemail.org
hackeronestatus.org
hackeronesucks.com
hackeronezendesk.com
inverselink.com
msk.ru
weardhackerone.com
withinsecurity.com
```

```bash
python3 domain_finder.py --company hackerone --company-in-domain True

blog-hackerone.com
hackerone-ext-content.com
hackerone-user-content.com
hackerone.ae
hackerone.co.me
hackerone.co.za
hackerone.com
hackerone.com.ph
hackerone.com.ua
hackerone.design
hackerone.ee
hackerone.engineer
hackerone.frl
hackerone.lt
hackerone.md
hackerone.net
hackerone.pw
hackerone.us
hackeronecommunity.com
hackeronemail.com
hackeronemail.org
hackeronestatus.org
hackeronesucks.com
hackeronezendesk.com
weardhackerone.com
```

To scan lots of domains at one time:
```
./lots_domains.sh companies.txt
```
