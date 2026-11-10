from playwright.sync_api import sync_playwright
from pathlib import Path
import re,json
base=Path('/mnt/data/scientific_plot_studio_v2')
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page();html=(base/'index.html').read_text();html=re.sub(r'<script[^>]+src="[^"]+"[^>]*></script>','',html);html=re.sub(r'<link[^>]+rel="stylesheet"[^>]*>','',html);page.set_content(html)
 for css in ['assets/styles.css','assets/v2.css']:page.add_style_tag(content=(base/css).read_text())
 for js in ['assets/plotly.min.js','assets/stats.js','assets/app.js','assets/v2.js']:page.add_script_tag(content=(base/js).read_text())
 result=page.evaluate('''() => {let core=window.SPSCore,errors=[],ok=[];for(let f of core.families){try{core.state.custom=false;core.selectStyle(f.name,0,true);if(f.name==='Phylogenetic Tree')window.SPSNewick='((A:0.2,B:0.3):0.4,C:0.6);';let spec=core.buildPlot();if(!spec.data.length)throw Error('empty trace');ok.push(f.name)}catch(e){errors.push([f.name,e.message])}}return {ok,errors}}''')
 print('OK',len(result['ok']),'ERRORS',json.dumps(result['errors']))
 b.close()
