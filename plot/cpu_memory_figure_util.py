import os.path

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio


# marker_color='rgb(55, 83, 109)'
# marker_color='rgb(26, 118, 255)'
# template: ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]


def AddQpsLatencyTrace(fig, df, barName, lineName):
    XAxis = df['Thread']

    # Draw Bar
    fig.add_trace(go.Bar(
        x=XAxis,
        y=df['cpu'],
        name=barName,
    ),
        secondary_y=False,
    )

    # Draw Line
    fig.add_trace(go.Scatter(
        x=XAxis,
        y=df['memory'],
        mode='lines+markers',
        name=lineName,
        marker=dict(size=10),
    ),
        secondary_y=True,
    )


def Draw(figureTitle, configs, path):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Threads</b>")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>CPU USAGE</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>MEM USAGE</b>", secondary_y=True)

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
        df = pd.read_csv(fileName, sep=",")
        df['Thread'] = df['Thread'].astype(str)
        print(df)

        AddQpsLatencyTrace(fig, df, barName, lineName)

    minMemory = min(df['memory'])
    maxMemory = max(df['memory'])
    # 设置y轴的范围
    fig.update_layout(
        yaxis2=dict(
            range=[minMemory-2000, maxMemory+2000],  # 假设您希望y轴的范围是从0到100
            dtick=1000  # 设置y轴的刻度间隔为10
        )
    )

    # display
    fig.show()
    pio.write_image(fig, os.path.join(path, 'cpu_memory.png'), scale=2)

