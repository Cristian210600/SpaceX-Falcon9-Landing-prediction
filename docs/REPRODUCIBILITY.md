# Reproducibility and provenance

## What is preserved

The seven notebooks are byte-for-byte copies of the latest uploaded course files, with descriptive filenames. A mapping and checksums are recorded in `notebooks/source_manifest.json`. Existing numerical outputs remain historical notebook outputs. They are not evidence that a new run occurred while this package was assembled.

The data folder contains the actual course CSV snapshots used to verify the presentation. `sources.json` records upstream URLs and hashes. These are different cohorts, not interchangeable versions of a single table.

## Notebook environment

The API and scraping notebooks require remote endpoints. The wrangling notebook reads a remote CSV. The EDA and ML notebooks use JupyterLite-specific `piplite` and `from js import fetch` setup. In a local kernel, install dependencies once using `requirements.txt`, skip the `piplite` cells, and replace JavaScript download cells with `pd.read_csv` of the corresponding bundled CSV.

When Jupyter is started from the repository root and the notebook is opened under `notebooks/`, a typical local path is `../data/dataset_part_2.csv`. Confirm the working directory using `Path.cwd()` rather than assuming it.

The original SQL notebook installs old SQLAlchemy / ipython-sql versions. Prefer the extracted `sql/run_queries.py` for a standard Python environment; it uses built-in sqlite3 and preserves the ten exercise queries.

The original EDA notebook contains repeated year-extraction code where a trend visualization was requested. The presentation’s year chart was rebuilt from `dataset_part_2.csv`. The repository preserves the submitted notebook and does not label it as a newly corrected, fully executed version.

The ML notebook's preprocessing, unseeded tree and obsolete grid option are retained to preserve the saved results’ context. Use a new experiment notebook for leakage-free, seeded comparisons; do not relabel fresh scores as the historical run.

## Additional code

`app/spacex_dash_app.py` was authored for this handoff based on the user-provided lab specification. It implements the site dropdown, pie callback, payload slider and scatter callback using the provided dashboard CSV. SQL query files are extracted from the supplied SQL notebook.

## Presentation status

The revised presentation contains 41 slides. It has the actual repository URL throughout methodology/results slides, expanded EDA scatter plots, SQL rates/rankings/time analysis, model comparison, confusion matrices and an explicit model-selection explanation. Remote GitHub contents were not verified or uploaded by this revision.

The PDF Folium slides contain coordinate diagrams and verified distance/results tables. The authoring browser blocked local HTML capture, so actual basemap screenshots remain to be added before claiming full map-slide compliance. Both interactive HTML maps are included. No generated coordinate graphic is described as a real Folium screenshot.

Additional SQL report queries in `sql/11_report_rates_and_ranking.sql` were executed on the included 101-row `Spacex.csv`. Their results are stored in `reports/additional_sql_results.json`. SQL landing success means a trimmed outcome beginning with `Success`; this definition differs from the ML Class target.

## Validation scope

Repository preparation checks file integrity, CSV dimensions, query execution, notebook JSON structure and Python syntax. It does not represent a fresh end-to-end execution of all seven original notebooks or a retraining of the classification models. Runtime dependency ranges describe the local application setup, not a lockfile for the historical ML execution.
