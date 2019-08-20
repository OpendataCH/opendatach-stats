[![goodtables.io](https://goodtables.io/badge/github/loleg/opendatach-stats.svg)](https://goodtables.io/github/loleg/opendatach-stats)

Statistics about the [Opendata.ch association](https://opendata.ch), compiled into a [Data Package](https://frictionlessdata.io/data-packages/) format. The data collected here was initially prepared by the [Opendata.ch/2019](https://opendata.ch/2019) unconference organisers.

[Explore on ![DataHub](https://datahub.io/static/img/logo-cube.png)](https://datahub.io/loleg/opendatach19/v/1)

The image below is excerpted from the [analysis of community needs](https://docs.google.com/spreadsheets/d/e/2PACX-1vTtoCwqVV9EBhHMcmmCI5FxIELLTT5IdEVrKIMImWmfcq4iE1xOW-_90Rs-dt3JCkb-1DxjNJRCjy40/pubhtml?gid=218970622&single=true) (Google Sheets).

![](https://docs.google.com/spreadsheets/u/2/d/e/2PACX-1vTtoCwqVV9EBhHMcmmCI5FxIELLTT5IdEVrKIMImWmfcq4iE1xOW-_90Rs-dt3JCkb-1DxjNJRCjy40/pubchart?oid=394312313&format=image)

# Data

In this repository, we are collecting stats about our association in simple data formats such as [CSV](https://frictionlessdata.io/guides/csv/), [JSON](http://json-schema.org/specification.html) and [GeoJSON](http://geojson.org/) about the association. Relevant files are added to the `data` folder.

If you are looking for open datasets, visit [opendata.swiss](https://opendata.swiss), [datahub.io](https://datahub.io) or [github/datasets](https://github.com/datasets).

# Preparation

Some of the data here was compiled and published as an online spreadsheet, others come from APIs and other Data Packages. In the `update.py` you will find a [DataFlows](https://github.com/datahq/dataflows) script that copies the latest statistics into the `data`, tests for consistency and prepares a `datapackage.json` schema.

To run the scripts locally, use these commands:

```
pip install dataflows
python update.py
```

To work with this Data Package, see the documentation at [frictionlessdata.io](https://frictionlessdata.io/guides/data-package/) and [datahub.io](https://datahub.io/docs/data-packages/publish-faq).

# License

This Data Package is made available by its maintainers under the [Public Domain Dedication and License v1.0](http://www.opendatacommons.org/licenses/pddl/1.0/), a copy of the full text of which is in [LICENSE.md](LICENSE.md).
