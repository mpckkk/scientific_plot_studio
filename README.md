# Scientific Plot Studio v2.0

**Local-first scientific plotting, research analysis and figure composition.**

Open `index.html` in a recent desktop browser (Chrome, Edge, Firefox, or Safari). No installation, accounts, API keys or network connection are required. Plotly.js is included in `assets/plotly.min.js`. A local web server is optional:

```bash
python -m http.server 8000
# open http://localhost:8000
```

## What's included

- **450 selectable plot styles**: 45 chart families × 10 distinct design presets (not 450 independent statistical methods). Searchable gallery, chart preview, editor and saved browser projects.
- **Figure composer**: add real plotted figures as panels, edit panel identifiers/captions, rearrange, choose 1–3 columns, choose aspect ratio, and export a combined SVG or PNG. Use Print / Save as PDF for a PDF.
- **Statistics**: Welch t-test, paired t-test, Mann–Whitney U, one-way ANOVA, Pearson and Spearman correlations, descriptive summaries, and Benjamini–Hochberg adjusted p-values. Export numerical CSV reports; optionally annotate live charts with a computed p-value.
- **Offline plotting assistant**: describes chart styles and recognizes common commands to configure chart family, palette, and supported column names. **This is a deterministic rule-based assistant, not a hosted generative AI model.** No network calls, subscriptions or credentials are involved.
- **Bioinformatics**: volcano, Manhattan, QQ, MA, PCA (computed from numeric columns), precomputed UMAP coordinates, gene expression heatmaps, GO dot/bar plots, genomic coordinate tracks and phylogenetic trees from imported Newick. Includes biological demonstration datasets.
- **Batch generator**: select chart families and themes, export up to 30 chart combinations as a ZIP with vector SVG figures, editable Plotly JSON configurations, source CSV and a manifest of skipped combinations. Unsupported input mappings are reported, not silently replaced.
- **Publication export**: journal widths (85mm/178mm), 300/600 DPI, TIFF with correct resolution tags, SVG, PNG, editable Plotly JSON, browser print-to-PDF, and a Python Plotly reproduction script.
- **Import**: CSV, TSV and Newick. Existing projects support JSON import/export. Core gallery can use up to 20,000 data rows (large selections are rendered with sampling for responsiveness).

## Quick start

1. Double-click `index.html`.
2. Choose a plot from **Plot gallery**, upload data in **Data workspace**, and configure column mappings in **Figure editor**.
3. Scroll to **Scientific workflows** (or select **Research workbench** in the left navigation).
4. In **Figure composer**, click **Add current chart**, choose another style and repeat, then export the combined figure.
5. In **Statistics**, choose the desired test, numeric column and group/second column. Click **Calculate** then export results.
6. In **Bioinformatics**, load sample coordinates for UMAP / MA / genomic tracks or paste/import a Newick tree.
7. In **Batch studio**, select styles and click **Generate batch ZIP**.
8. In **Publication export**, select your publication width, DPI and image type.

## Data format examples

Volcano: `gene,log2FC,pvalue`; MA: `gene,log2FC,pvalue,expression`; UMAP: `UMAP1,UMAP2,cluster`; forest: `study,effect,uncertainty`; heatmap: `gene,sample,expression`; enrichment: `pathway,gene_ratio,count`; genomic track: `gene,position,chromosome`; statistical tests: `group,value`.

Use the column mapping controls for datasets with different column names. UMAP plotting displays existing coordinates; it does **not** calculate UMAP. GO plotting displays supplied pathway-level results; it does **not** run gene-set enrichment. The phylogeny viewer parses supplied Newick trees; it does **not** infer phylogenetic trees. Statistical tests rely on the user's assumptions, appropriate sampling and experimental design.

## Export details and limits

- SVG exports are vector and generated from actual Plotly charts. Combined SVG embeds panel SVGs as SVG image data URIs. A browser or editor that doesn't support embedded data URIs may require conversion.
- TIFF export uses browser canvas rasterization and emits an uncompressed, 8-bit RGB TIFF with X/Y DPI metadata. It is not CMYK. Export resolution is capped at 24 megapixels to limit browser memory use; 600-DPI double-column exports may exceed this cap.
- PDF uses your browser's print dialog. The browser determines final paper/page settings.
- Batch output is a standards-compliant ZIP32 (uncompressed, UTF-8 filenames). Export may be resource intensive for 30 figures; cancel is available between jobs.
- For reproducibility, exported Python scripts require `pip install plotly kaleido` (Kaleido needed only for static image export). Project files also contain source data and plotting configuration.
- This is a fully browser-run tool rather than a multi-user web service: no hosted login, sharing backend, job queue or model API. It is **not clinically validated**.
