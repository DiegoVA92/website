### Data
import datetime
import pandas as pd
import json
### Graphing
import plotly.graph_objects as go
import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
from footer import Footer

with open('assets/risk_calculators/risk_calc_features.json','r') as f:
    features = json.load(f)

def gender_map(x,name):
    if name == "Gender":
        if x == 0:
            return "Male"
        else:
            return "Female"
    return x

def build_dropdown_card(id, content_dict):
    insert_data = \
            [
                dbc.Col(
                    html.Div(
                        dcc.Dropdown(
                            id = 'calc-categorical-{}'.format(id),
                            options = [{'label': gender_map(x,content_dict["name"]), 'value': x} for x in content_dict['vals']],
                            value = "{}".format(content_dict['default']),
                            style={"width":150}
                        ),
                        id = 'calc-categorical-{}-wrapper'.format(id),
                    ),
                ),
            ]
    card = [
        dbc.Row(
            insert_data,
        ),
        dbc.Tooltip(
            content_dict['explanation'],
            target='calc-categorical-{}-wrapper'.format(id),
        ),
    ]
    return card

def build_input_card(id, content_dict):
    insert_data = \
            [
                dbc.Col(
                    html.Div(
                        dcc.Input(
                            id="calc-numeric-{}".format(id),
                            type="number",
                            placeholder="{}".format(content_dict['default']),
                            style={"width":100}
                        ),
                        id = "calc-numeric-{}-wrapper".format(id),
                    ),
                ),
            ]
    card = [
        dbc.Row(
            insert_data,
        ),
        dbc.Tooltip(
            content_dict['explanation'],
            target="calc-numeric-{}-wrapper".format(id),
        ),
    ]
    return card

def build_checkbox_card(id, content_dict):
    insert_data = \
            [
                dbc.Col(
                    html.Div(
                        dbc.Checklist(
                            options=[{'label': x, 'value': x} for x in content_dict['vals']],
                            value=[],
                            id="calc-checkboxes-{}".format(id),
                        ),
                        id = "calc-checkboxes-{}-wrapper".format(id),
                    ),
                ),
                dbc.Col(
                    html.Div(
                        dbc.Checklist(
                            options=[{'label': x, 'value': x} for x in content_dict['vals']],
                            value=[],
                            id="calc-checkboxes-{}".format(id),
                        ),
                        id = "calc-checkboxes-{}-wrapper".format(id),
                    ),
                ),
            ]
    card = [
        dbc.Row(
            insert_data
        ),
        dbc.Tooltip(
            content_dict['explanation'],
            target="calc-checkboxes-{}-wrapper".format(id),
        ),
    ]
    return card

def build_feature_cards():
    card_content = []
    cards = []
    inputs = features["numeric"]
    dropdowns = features["categorical"]
    checkboxes = features["checkboxes"]
    for id, content_dict in enumerate(dropdowns):
        card_content.append((content_dict['name'],build_dropdown_card(id, content_dict)))
    for id, content_dict in enumerate(inputs):
        card_content.append((content_dict['name'],build_input_card(id, content_dict)))
    for id, content_dict in enumerate(checkboxes):
        card_content.append((content_dict['name'],build_checkbox_card(id, content_dict)))

    for name,c in card_content:
        card = \
            dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(name,style={"fontWeight": "bold"}),
                        dbc.CardBody(c,className="feat-options-body")
                    ],
                    className="feat-options"
                ),
            ],
            style={
                'paddingBottom':20,
                'borderColor':'red'
                },
            xs=5,
            sm=4,
            md=4,
            lg=12,
            )
        cards.append(card)
    return cards
