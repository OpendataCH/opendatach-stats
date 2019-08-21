Statistics about the [Opendata.ch association](https://opendata.ch), compiled into [Data Packages](https://frictionlessdata.io/data-packages/) using simple data formats such as [CSV](https://frictionlessdata.io/guides/csv/), [JSON](http://json-schema.org/specification.html) and [GeoJSON](http://geojson.org/). Relevant files are added to the `data` folder. If you are looking for open datasets in general, visit our [website](https://opendata.ch), [opendata.swiss](https://opendata.swiss), [datahub.io](https://datahub.io) or [github/datasets](https://github.com/datasets).

A description of the currently published packages follows below. 

## #opendatach19

[![goodtables.io](https://goodtables.io/badge/github/loleg/opendatach-stats.svg)](https://goodtables.io/github/loleg/opendatach-stats) [<img alt="DataHub" src="https://datahub.io/static/img/logo-cube.png" width="50">](https://datahub.io/loleg/opendatach19)

The data collected here was initially prepared by the [Opendata.ch/2019](https://opendata.ch/2019) unconference organisers. The image below is excerpted from the initial analysis of community needs, as described in the [blog post](https://opendata.ch/2019/08/opendata-ch-2019-forum-rueck-und-ausblick/). You can also explore [this data at DataHub](https://datahub.io/loleg/opendatach19).

![](https://docs.google.com/spreadsheets/u/2/d/e/2PACX-1vTtoCwqVV9EBhHMcmmCI5FxIELLTT5IdEVrKIMImWmfcq4iE1xOW-_90Rs-dt3JCkb-1DxjNJRCjy40/pubchart?oid=394312313&format=image)

Some of the data here was compiled and published as an [online spreadsheet](https://docs.google.com/spreadsheets/u/2/d/e/2PACX-1vTtoCwqVV9EBhHMcmmCI5FxIELLTT5IdEVrKIMImWmfcq4iE1xOW-_90Rs-dt3JCkb-1DxjNJRCjy40/pubhtml#) (Google Sheets), others come from APIs and other Data Packages. In the `update.py` you will find a [DataFlows](https://github.com/datahq/dataflows) script that copies the latest statistics into the `data`, tests for consistency and prepares a `datapackage.json` schema.

# Usage

To run the scripts locally and update the Data Packages, use these commands:

```
pip install dataflows
python update.py
```

For additional background see the documentation at [frictionlessdata.io](https://frictionlessdata.io/guides/data-package/) and [datahub.io](https://datahub.io/docs/data-packages/publish-faq).

# License

This repository is made available by its maintainers under the Open Data Commons [Public Domain Dedication and License v1.0](http://www.opendatacommons.org/licenses/pddl/1.0/), a copy of the full text of which is in [LICENSE.md](LICENSE.md).
