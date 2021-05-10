import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
import time
import gpt_2_simple as gpt2

# Note: commented-out lines use an alternative approach using dynanic index


app = dash.Dash(__name__, suppress_callback_exceptions=True)

print('App is starting..')

app.layout = html.Div([
    html.H3("Rick And Morty Transcript Generator",
            style={
                'text-align': 'center', }
            ),

    dcc.Slider(
        id='length-slider',
        min=50,
        max=400,
        value=200,
        step=50,
    ),

    dcc.Slider(
        id='temp-slider',
        min=0.5,
        max=1.5,
        value=0.8,
        step=0.1,
        marks={
            0.5: {'label': 'Cold 0.5', 'style': {'color': '#77b0b1'}},
            1.0: {'label': '1.0'},
            1.5: {'label': 'Hot 1.5', 'style': {'color': '#f50'}}
        },
        included=False
    ),

    html.Div(
        [
            dcc.Textarea(id="loading-input-2",
                         draggable='false', rows="40",
                         value='Rick:',
                         style={'resize': 'none', 'width': '80%',
                                'display': 'block',
                                'margin-left': 'auto',
                                'margin-right': 'auto'}),
            dcc.Loading(
                id="loading-2",
                children=[html.Div([html.Div(id="loading-output-2", children='ok')])],
                type="circle",
            )
        ]),
    html.Div(id='dynamic-button-container',
             children=[
                 html.Button(
                     # id={'type': 'dynamic-button', 'index': 0 },
                     id='button0',
                     children='Submit'
                 )
             ]),

])


@app.callback(
    [Output('dynamic-button-container', 'children'),
     Output("loading-input-2", "value"),
     Output("loading-output-2", "children"),
     ],
    [  # Input({'type': 'dynamic-button', 'index': ALL}, 'n_clicks')
        Input('button0', 'n_clicks')
    ],
    [State('dynamic-button-container', 'children'),
     State("loading-input-2", 'value'),
     State('temp-slider', 'value'),
     State('length-slider', 'value')])
def display_newbutton(n_clicks, children, input, temp, length):
    # if n_clicks[0] is None: return children
    # out = generate_out(input)
    # print(out)
    if n_clicks is None:
        return children, input, ''
    else:
        print('Doing some calculation..')
        # time.sleep(3)

        out = generate_out(input, temp, length)
        # print(out)

        new_element = html.Button(
            # id={'type': 'dynamic-button','index': 0 }, #n_clicks[0] },
            id='button0',
            children='Submit'
        )

        children.pop()
        children.append(new_element)
        print('Generating a new button')

        return children, out, ''


# @app.callback(
#     Output({'type': 'dynamic-button', 'index': 0}, 'disabled'),
#     [Input({'type': 'dynamic-button', 'index': 0}, 'n_clicks')]
# )
@app.callback(
    Output('button0', 'disabled'),
    [Input('button0', 'n_clicks')]
)
def hide_newbutton(n_clicks):
    if n_clicks is None:
        return False
    else:
        print('Disabling the button')
        return True


def generate_out(pre, temp, length):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    My_gen = gpt2.generate(sess,
                           length=length,
                           temperature=temp,
                           prefix=pre,
                           nsamples=1,
                           batch_size=1,
                           return_as_list=True,
                           )

    return My_gen[0]


# @app.callback(Output("loading-output-2", "children"), Input("loading-input-2", "value"))
# def input_triggers_nested(value):
#     time.sleep(1)
#     print('value:',value)
#     return value


if __name__ == '__main__':
    app.run_server(debug=True, host='10.0.0.19')
