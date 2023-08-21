import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd

# marker_color='rgb(55, 83, 109)'
# marker_color='rgb(26, 118, 255)'

# template: ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]


def AddQpsLatencyTrace(fig, df, barName, lineName):
    XAxis = df['Threads']

    # Draw Bar
    fig.add_trace(go.Bar(
        x=XAxis,
        y=df['QPS'],
        name=barName,
    ),
        secondary_y=False,
    )

    # Draw Line
    fig.add_trace(go.Scatter(
        x=XAxis,
        y=df['AvgLatency'],
        mode='lines+markers',
        name=lineName,
        marker=dict(size=10),
    ),
        secondary_y=True,
    )

    # fig.add_trace(go.Scatter(
    #     x=XAxis,
    #     y=df['PctLatency'],
    #     mode='lines+markers',
    #     name='PctLatency',
    # ),
    #     secondary_y=True,
    # )


def Draw(figureTitle, configs):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Threads</b>")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>QPS</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Latency</b>", secondary_y=True)

    # Set figure title
    fig.update_layout(
        template="plotly_white",
        title={
            'text': figureTitle,
            'x': 0.5,
            'font': dict(
                family="Arial",  # figure title font
                size=24,  # figure title size
                color="#000000"  # figure title color
            )
        })

    # Read data into DataFrame from csv files
    for conf in configs:
        fileName = conf['fileName']
        barName = conf['barName']
        lineName = conf['lineName']

        print("read data from:", fileName)
        df = pd.read_csv(fileName, sep="\t")
        df['Threads'] = df['Threads'].astype(str)
        print(df)

        AddQpsLatencyTrace(fig, df, barName, lineName)

    # display
    fig.show()
