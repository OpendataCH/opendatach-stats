from dataflows import Flow, load, dump_to_path, dump_to_zip, printer, add_metadata
from dataflows import sort_rows, filter_rows, find_replace, delete_fields, set_type, validate, unpivot


od19_base = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTtoCwqVV9EBhHMcmmCI5FxIELLTT5IdEVrKIMImWmfcq4iE1xOW-_90Rs-dt3JCkb-1DxjNJRCjy40/pub?single=true&output=csv&gid='
od19_feedback = '587615265'
od19_analysis = '218970622'

def not_empty_groupcol(rows):
    deduplicate = []
    for row in rows:
        if 'Alle "Bedürfnisse"' not in row:
            yield row
        elif row['Alle "Bedürfnisse"'].strip() and \
             row['Anzahl Auflistung (Zahl)'] is not None:
                v = row['Alle "Bedürfnisse"'].strip()
                if not v in deduplicate:
                    deduplicate.append(v)
                    yield row

def conference_csv():
    flow = Flow(
        # Load inputs
        load(
            od19_base + od19_feedback,
            name='feedback',
            format='csv',
        ),
        load(
            od19_base + od19_analysis,
            name='analysis',
            format='csv',
        ),
        # Process them
        set_type("Anzahl.*", type='integer', resources='analysis'),
        delete_fields([
            "Anzahl Auflistung",
            ".*\\(Formel\\)",
            ".*Duplikate",
            ], resources='analysis'
        ),
        not_empty_groupcol,
        # Save the results
        add_metadata(
            name='opendatach19',
            title='''Opendata.ch/2019 Forum''',
            licenses=[{
                "name": "ODC-PDDL-1.0",
                "path": "http://opendatacommons.org/licenses/pddl/",
                "title": "Open Data Commons Public Domain Dedication and License v1.0"
            }],
            maintainers=[{
                "name": "Oleg Lavrovsky",
                "web": "https://datalets.ch/"
            }],
            views=[{
                "name": "Groups",
                "resources": [ "analysis" ],
                "spec": {
                    "group": "Alle ""Bedürfnisse""",
                    "series": [
                        "Anzahl Auflistung (Zahl)"
                    ],
                    "type": "bar"
                },
                "specType": "simple",
                "title": "Topic counts"
            }]
        ),
        printer(),
        validate(),
        dump_to_path('data/opendatach19'),
    )
    flow.process()


if __name__ == '__main__':
    conference_csv()
