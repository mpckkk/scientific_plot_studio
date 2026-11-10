from playwright.sync_api import sync_playwright
from pathlib import Path
import re,zipfile,xml.etree.ElementTree as ET
from PIL import Image
base=Path('/mnt/data/scientific_plot_studio_v2')
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-web-security'])
 page=browser.new_page(viewport={'width':1350,'height':1000},accept_downloads=True)
 html=(base/'index.html').read_text();html=re.sub(r'<script[^>]+src="[^"]+"[^>]*></script>','',html);html=re.sub(r'<link[^>]+rel="stylesheet"[^>]*>','',html)
 page.set_content(html)
 for css in ['assets/styles.css','assets/v2.css']:page.add_style_tag(content=(base/css).read_text())
 for js in ['assets/plotly.min.js','assets/stats.js','assets/app.js','assets/v2.js']:page.add_script_tag(content=(base/js).read_text())
 page.wait_for_timeout(700)
 page.locator('#addPanel').click();page.wait_for_timeout(500)
 page.locator('#composeTitle').fill('Figure 1')
 with page.expect_download(timeout=45000) as d:page.locator('#composeSvg').click()
 d.value.save_as(base/'tests/composite-test.svg')
 ET.parse(base/'tests/composite-test.svg');print('Composite SVG valid', (base/'tests/composite-test.svg').stat().st_size)
 page.locator('[data-v2tab="publication"]').click();page.locator('#pubFormat').select_option('tiff');page.locator('#pubPreset').select_option('single');page.locator('#pubDpi').select_option('300');
 with page.expect_download(timeout=45000) as d:page.locator('#pubExport').click()
 d.value.save_as(base/'tests/publication-test.tif')
 im=Image.open(base/'tests/publication-test.tif');print('TIFF',im.size,im.mode,im.info)
 page.locator('[data-v2tab="batch"]').click();page.locator('#batchFamilies').select_option(['Bar','Box','PCA']);page.locator('#batchDesigns').select_option(['0']);
 with page.expect_download(timeout=45000) as d:page.locator('#batchRun').click()
 d.value.save_as(base/'tests/export-test.zip')
 with zipfile.ZipFile(base/'tests/export-test.zip') as f:
  bad=f.testzip();print('ZIP valid',bad, f.namelist())
 page.locator('[data-v2tab="statistics"]').click();page.locator('#statTest').select_option('welch');page.locator('#statGroup').select_option('4');page.locator('#statY').select_option('1');page.locator('#statA').select_option('Control');page.locator('#statB').select_option('Treatment');page.locator('#runStat').click();print('Welch',page.locator('#statResult').inner_text()[:120]);
 print('all export tests complete');browser.close()
