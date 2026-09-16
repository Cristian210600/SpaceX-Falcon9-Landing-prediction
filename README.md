# SpaceX Falcon 9 Landing Prediction

An IBM Applied Data Science Capstone project exploring Falcon 9 launch records, first-stage landing outcomes, geographic context and classification models.

**Author:** Cristian  
**Repository:** [Cristian210600/SpaceX-Falcon9-Landing-prediction](https://github.com/Cristian210600/SpaceX-Falcon9-Landing-prediction)

## Project question

Can launch and booster information help predict the first-stage landing outcome recorded in the course dataset?

The project covers API data collection, web scraping, cleaning, exploratory analysis with Python and SQL, Folium geographic analysis, a Plotly Dash dashboard and model comparison. The binary laboratory label is not identical to mission success, recovered hardware or economic reuse.

## Main findings

| Analysis | Result | Scope |
|---|---|---|
| Landing outcome distribution | 60 Class 1 / 90 launches (66.67%) | EDA / ML snapshot |
| Largest Class 1 count | CCAFS SLC 40: 33 / 55 | EDA / ML snapshot |
| Highest observed site rate | KSC LC 39A: 17 / 22 (77.27%) | EDA / ML snapshot |
| Largest dashboard success count and rate | KSC LC-39A: 10 / 13 (76.92%) | Separate 56-record snapshot |
| NASA (CRS) payload sum | 45,596 kg | 101-record SQL snapshot |
| Best saved test accuracy | 83.33%, tied across LR, SVM and KNN | 18-record test set |

The dashboard pie’s **41.7% KSC share** means 10 out of 24 positive outcomes across all sites. It is not KSC’s within-site rate of 10 out of 13 launches (76.9%).

## Saved classification results

| Model | Best 10-fold CV accuracy | Test accuracy |
|---|---:|---:|
| Logistic regression | 84.64% | 83.33% |
| Support vector machine | 84.82% | 83.33% |
| Decision tree | 87.50% | 77.78% |
| K-nearest neighbors | 84.82% | 83.33% |

These values come from the saved outputs of the supplied ML notebook; they are not newly reproduced training results. The test set contains 18 records, so one prediction changes accuracy by 5.56 percentage points. An always-Class-1 baseline achieves 66.67% on this test set.

## Files

| Folder / file | Contents |
|---|---|
| [notebooks/](notebooks/) | Seven original course notebooks, ordered and renamed for navigation |
| [app/spacex_dash_app.py](app/spacex_dash_app.py) | Runnable implementation of all four dashboard tasks |
| [data/](data/) | The six course CSV snapshots used for the report and dashboard |
| [data/sources.json](data/sources.json) | Original download URLs, row counts and SHA-256 checksums |
| [sql/](sql/) | The ten SQLite exercise queries and a Python runner |
| [reports/SpaceX_Capstone_Report.pdf](reports/SpaceX_Capstone_Report.pdf) | Revised 41-slide presentation with explicit methodology links, SQL rankings and model selection |
| [reports/SpaceX_Capstone_Report.pptx](reports/SpaceX_Capstone_Report.pptx) | Editable presentation |
| [reports/SpaceX_Folium_Interactive.html](reports/SpaceX_Folium_Interactive.html) | Interactive map with outcome clusters and proximity lines |
| [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) | Environment differences, limitations and source provenance |
| [docs/PUBLISH_RO.md](docs/PUBLISH_RO.md) | Upload instructions in Romanian |

## Run the dashboard locally

Use Python 3.11 or 3.12. From the repository root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies and start the application:

```bash
python -m pip install -r requirements.txt
python app/spacex_dash_app.py
```

Open **http://127.0.0.1:8050**. The dashboard reads the bundled CSV, so no API credentials are needed. Use `Ctrl+C` to stop the server. GitHub displays source files; it does not run a Python Dash server.

### Dashboard functionality

- **All Sites:** compare the positive-outcome counts across sites.
- **One site:** compare Class 0 and Class 1 counts within that site.
- **Payload slider:** filter the scatter plot by an inclusive payload interval.
- **Booster colors:** compare the booster version categories present in the selected subset.

The Dash script was reconstructed for this repository from the lab requirements and supplied screenshots. It is not presented as the original script used to create those screenshots.

## Explore the notebooks

1. [API data collection](notebooks/01_data_collection_api.ipynb)
2. [Web scraping](notebooks/02_web_scraping.ipynb)
3. [Data wrangling](notebooks/03_data_wrangling.ipynb)
4. [Exploratory SQL](notebooks/04_eda_sql.ipynb)
5. [Exploratory visualization](notebooks/05_eda_visualization.ipynb)
6. [Folium geographic analysis](notebooks/06_folium_launch_sites.ipynb)
7. [Classification](notebooks/07_machine_learning.ipynb)

The notebooks are preserved from the supplied course files, including existing outputs. **Some use the Skills Network / JupyterLite environment** (`piplite`, JavaScript `fetch` or SQL magics). They are not all directly runnable in a standard Python kernel without adapting setup cells. See [reproducibility notes](docs/REPRODUCIBILITY.md) before rerunning. The package does not claim that every notebook was executed end to end during repository preparation.

Run the extracted SQL exercises without notebook extensions:

```bash
python sql/run_queries.py
```

Open the Folium HTML file in a browser with internet access for map tiles and JavaScript libraries.

## Data scope and limitations

| Snapshot | Records | Use |
|---|---:|---|
| `dataset_part_1.csv`, `dataset_part_2.csv`, `dataset_part_3.csv` | 90 each | Wrangling, EDA and ML; different processing stages |
| `Spacex.csv` | 101 | SQL exercises |
| `spacex_launch_dash.csv`, `spacex_launch_geo.csv` | 56 each | Dashboard and geographic analysis |

These historical laboratory snapshots must not be treated as current SpaceX performance. Site names and denominators differ across datasets.

Important methodological limits:

- The ML notebook scales all features before the train/test split. Fit preprocessing inside a cross-validated `Pipeline` in a future experiment to prevent leakage.
- The tree grid contains an obsolete `max_features='auto'` candidate and the tree is not seeded. Some fits fail and rerun scores may differ.
- Class 1 includes five successful ocean landings, so it is broader than actual booster recovery.
- Small groups are unstable: the dashboard’s B5 category has one positive outcome in one record.
- Geographic distances use manually selected reference points; they are neither verified nearest-feature distances nor driving distances.

## Next steps

Use chronological and booster-grouped validation, verify that every input was available before launch, align the outcome with the intended recovery decision, and evaluate the cost of optimistic false-positive predictions.

## Attribution

Course templates and educational data are from IBM / Skills Network’s Applied Data Science Capstone. Original notebook author and copyright notices are retained. Upstream data includes SpaceX API records and a historical Wikipedia launch-list revision. This repository is an educational project and is not affiliated with SpaceX. See [NOTICE.md](NOTICE.md) for asset and source credits.


## Presentation revision

The PDF and PowerPoint now contain 41 slides. Repository links appear throughout the methodology and results sections. Additional SQL queries and calculated results are included. Actual Folium basemap screenshots remain to be inserted on the geographic slides; the interactive HTML maps are included under `reports/`. See `docs/PUBLISH_RO.md` before submission.
