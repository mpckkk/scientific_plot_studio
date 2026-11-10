from playwright.sync_api import sync_playwright
import pathlib, json, time
url=pathlib.Path('/mnt/data/scientific_plot_studio_v2/index.html').as_uri()
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-web-security'])
 page=browser.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
 errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
 base=pathlib.Path('/mnt/data/scientific_plot_studio_v2');html=(base/'index.html').read_text();import re
 html=re.sub(r'<script[^>]+src="[^"]+"[^>]*></script>','',html);html=re.sub(r'<link[^>]+rel="stylesheet"[^>]*>','',html)
 page.set_content(html,wait_until='load')
 for css in ['assets/styles.css','assets/v2.css']:page.add_style_tag(content=(base/css).read_text())
 for js in ['assets/plotly.min.js','assets/stats.js','assets/app.js','assets/v2.js']:page.add_script_tag(content=(base/js).read_text())
 page.wait_for_timeout(1800)
 print('TITLE',page.title());print('CORE',page.evaluate('!!window.SPSCore'),'V2',page.evaluate('!!window.SPSV2'),'FAMILIES',page.evaluate('window.SPSCore?.families.length'))
 print('INITIAL',page.locator('#status').inner_text(),page.locator('#plotMeta').inner_text())
 page.locator('#addPanel').click();page.wait_for_timeout(1200)
 print('PANELS',page.locator('.compose-card').count(),'MESSAGE',page.locator('#composeMessage').inner_text())
 page.locator('[data-v2tab="statistics"]').click();page.locator('#statTest').select_option('pearson');page.locator('#statY').select_option('1');page.locator('#statGroup').select_option('3');page.locator('#runStat').click();print('STATS',page.locator('#statResult').inner_text()[:250])
 page.locator('[data-v2tab="assistant"]').click();page.locator('#aiExample').click();print('AI',page.locator('#aiResult').inner_text()[:250])
 page.locator('[data-v2tab="bio"]').click();page.locator('#bioTree').click();page.wait_for_timeout(1100);print('TREE',page.locator('#bioStatus').inner_text(),page.locator('#status').inner_text())
 page.locator('#bioSample').select_option('umap');page.locator('#bioLoad').click();page.wait_for_timeout(1100);print('UMAP',page.locator('#bioStatus').inner_text(),page.locator('#status').inner_text())
 page.locator('[data-v2tab="batch"]').click();page.locator('#batchFamilies').select_option(['Scatter','Line']);page.locator('#batchDesigns').select_option(['0']);
 with page.expect_download(timeout=45000) as d:page.locator('#batchRun').click()
 download=d.value;target='/mnt/data/scientific_plot_studio_v2/tests/batch-test.zip';download.save_as(target);print('BATCH',pathlib.Path(target).stat().st_size,page.locator('#batchStatus').inner_text())
 page.locator('[data-v2tab="publication"]').click();page.locator('#pubFormat').select_option('svg');
 with page.expect_download(timeout=45000) as d:page.locator('#pubExport').click()
 download=d.value;target='/mnt/data/scientific_plot_studio_v2/tests/pub-test.svg';download.save_as(target);print('PUB SVG',pathlib.Path(target).stat().st_size)
 page.screenshot(path='/mnt/data/scientific_plot_studio_v2/tests/screenshot.png',full_page=True)
 print('ERRORS',json.dumps(errors[:12]));browser.close()
