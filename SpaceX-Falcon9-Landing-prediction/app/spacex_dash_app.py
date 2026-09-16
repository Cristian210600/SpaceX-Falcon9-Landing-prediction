"""SpaceX capstone dashboard, reconstructed from the supplied lab requirements."""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

ROOT = Path(__file__).resolve().parents[1]
spacex_df = pd.read_csv(ROOT / "data" / "spacex_launch_dash.csv")
sites = sorted(spacex_df["Launch Site"].dropna().unique())
app = Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"
server = app.server

app.layout = html.Div(
    [
        html.H1("SpaceX Launch Records Dashboard"),
        html.P("IBM course snapshot: 56 records. Class is the laboratory outcome label."),
        dcc.Dropdown(
            id="site-dropdown",
            options=[{"label": "All Sites", "value": "ALL"}]
            + [{"label": site, "value": site} for site in sites],
            value="ALL",
            placeholder="Select a Launch Site here",
            searchable=True,
            clearable=False,
        ),
        dcc.Graph(id="success-pie-chart"),
        html.P("Payload range (kg):"),
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            marks={value: f"{value:,}" for value in range(0, 10001, 1000)},
            value=[float(spacex_df["Payload Mass (kg)"].min()),
                   float(spacex_df["Payload Mass (kg)"].max())],
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        dcc.Graph(id="success-payload-scatter-chart"),
    ],
    style={"maxWidth": "1150px", "margin": "30px auto", "fontFamily": "Arial"},
)


@app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
def get_pie_chart(entered_site):
    if entered_site == "ALL" or entered_site is None:
        counts = spacex_df.groupby("Launch Site", as_index=False)["class"].sum()
        fig = px.pie(counts, names="Launch Site", values="class",
                     title="Total Class 1 outcomes by site (share of all Class 1 records)")
    else:
        subset = spacex_df[spacex_df["Launch Site"] == entered_site]
        counts = subset["class"].value_counts().reindex([0, 1], fill_value=0)
        values = pd.DataFrame({"Outcome": ["Class 0", "Class 1"],
                               "Count": counts.to_numpy()})
        fig = px.pie(values, names="Outcome", values="Count", color="Outcome",
                     color_discrete_map={"Class 0": "#D16635", "Class 1": "#16817A"},
                     title=f"Outcome proportions at {entered_site} (n={len(subset)})")
    fig.update_traces(textinfo="percent+label")
    return fig


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value"),
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range or [0, 10000]
    subset = spacex_df[spacex_df["Payload Mass (kg)"].between(low, high)].copy()
    if entered_site and entered_site != "ALL":
        subset = subset[subset["Launch Site"] == entered_site]
    fig = px.scatter(
        subset, x="Payload Mass (kg)", y="class", color="Booster Version Category",
        hover_data=["Launch Site"],
        title=f"Payload and outcome: {entered_site or 'ALL'} (n={len(subset)})",
        labels={"class": "Outcome class"},
    )
    fig.update_yaxes(tickvals=[0, 1], range=[-0.15, 1.15])
    if subset.empty:
        fig.add_annotation(text="No records match the selected filters", showarrow=False,
                           xref="paper", yref="paper", x=0.5, y=0.5)
    return fig


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=False)
