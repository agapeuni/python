import altair as alt
from vega_datasets import data

alt.renderers.enable('notebook')

iris = data.iris()

chart = alt.Chart(iris).mark_point().encode(
    x='petalLength',
    y='petalWidth',
    color='species'
)

# 크롬 브라우저에서 표시
chart.show()

# pip install altair vega_datasets vega

# pip install altair_viewer
# alt.renderers.enable('altair_viewer')
# 렌더링

# https://altair-viz.github.io/user_guide/display_frontends.html#display-general
