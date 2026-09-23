"""Uzņem cenu lapu ekrānšāviņus budžeta pielikumiem.

Palaišana (no šīs mapes):  python ekranuznemumi.py            (visi)
                           python ekranuznemumi.py 1.3        (tikai viena lapa)
Rezultāts:                 ekranuznemumi/<lapa>_<n>.png, tad `python budzets.py` ieliek tos Excel.

Katram attēlam augšā ir josla ar saiti un uzņemšanas laiku (pierādījums LU).
Pēc palaišanas attēli JĀPĀRSKATA: vai redzama pareizā cena un vai lapu neaizsedz logs.
"""
import re
import sys
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
OUT = HERE / "ekranuznemumi"

# (faila nosaukums, saite, teksts, ko novietot ekrāna vidū)
SHOTS = [
    ("1.1_1", "https://claude.com/pricing", "From 90"),
    ("1.2_1", "https://www.ovhcloud.com/en-ie/vps/", "€7.21"),
    ("1.2_2", "https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/", "CX33"),
    ("1.2_3", "https://www.digitalocean.com/pricing/droplets", "$48"),
    ("1.3_1", "https://hostnet.lv/lv/domains/", "Domain zone"),
    ("1.3_2", "https://www.nic.lv/lv/buj-maksa-un-norekini", "14,52"),
    ("1.3_3", "https://www.vpsnet.com/en/services/domains/lv", "20.99"),
    ("1.4_1", "https://platform.claude.com/docs/en/about-claude/pricing", "Claude Opus 5"),
]

ACCEPT = re.compile(
    r"^(accept all( cookies)?|allow all|accept|i agree|agree|piekrītu( visam)?|pieņemt( visas)?|"
    r"atļaut visas sīkdatnes|akceptēt visus sīkfailus|apstiprināt visas|sapratu|ok)$", re.I)
CLOSE = re.compile(r"^(close|aizvērt|×|x)$", re.I)

# Noņem atlikušos fiksētos logus par sīkdatnēm (ja pogu neizdevās nospiest)
REMOVE_OVERLAYS_JS = r"""() => {
  for (const el of document.querySelectorAll('body *')) {
    const s = getComputedStyle(el);
    if ((s.position === 'fixed' || s.position === 'sticky') &&
        /cookie|sīkdatn|sīkfail|sikdatn|latest news/i.test(el.innerText || '') &&
        el.getBoundingClientRect().height < window.innerHeight * 0.9) el.remove();
  }
}"""

BANNER_JS = """([url, ts]) => {
  const d = document.createElement('div');
  d.textContent = url + '   |   ' + ts;
  d.style.cssText = 'position:fixed;top:0;left:0;right:0;z-index:2147483647;background:#111;color:#fff;'
    + 'font:14px/1.4 Arial,sans-serif;padding:6px 10px;';
  document.body.appendChild(d);
}"""


def click_first_visible(page, pattern):
    for loc in (page.get_by_role("button", name=pattern), page.get_by_role("link", name=pattern),
                page.get_by_text(pattern)):
        for i in range(min(loc.count(), 5)):
            try:
                if loc.nth(i).is_visible():
                    loc.nth(i).click(timeout=2000)
                    page.wait_for_timeout(800)
                    return True
            except Exception:
                pass
    return False


def center_on_text(page, text):
    loc = page.get_by_text(text, exact=False)
    for i in range(min(loc.count(), 15)):
        el = loc.nth(i)
        try:
            if el.is_visible():
                el.evaluate("e => e.scrollIntoView({block: 'center'})")
                page.wait_for_timeout(800)
                return True
        except Exception:
            pass
    return False


def launch(p):
    try:
        return p.chromium.launch()
    except Exception:
        # Python Playwright versija var gaidīt citu pārlūku; izmanto jau uzstādīto Chromium
        installed = sorted(Path.home().glob("AppData/Local/ms-playwright/chromium-*/chrome-win64/chrome.exe"))
        if not installed:
            raise
        return p.chromium.launch(executable_path=str(installed[-1]))


def main(only=None):
    OUT.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    with sync_playwright() as p:
        browser = launch(p)
        ctx = browser.new_context(
            viewport={"width": 1440, "height": 1000}, locale="lv-LV", timezone_id="Europe/Riga",
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/140.0 Safari/537.36"),
        )
        for name, url, target in SHOTS:
            if only and not name.startswith(only):
                continue
            page = ctx.new_page()
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(4000)
                click_first_visible(page, ACCEPT)
                click_first_visible(page, CLOSE)
                page.evaluate(REMOVE_OVERLAYS_JS)
                found = center_on_text(page, target)
                page.evaluate(REMOVE_OVERLAYS_JS)
                page.evaluate(BANNER_JS, [url, ts])
                page.screenshot(path=OUT / f"{name}.png")
                print(f"OK   {name}  {'(atrasts: ' + target + ')' if found else '(teksts NAV atrasts)'}  {url}")
            except Exception as e:
                print(f"KĻŪDA {name}  {url}: {type(e).__name__}: {str(e)[:120]}")
            finally:
                page.close()
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
