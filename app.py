from random import randrange
from flask import Flask, render_template
from flask.json import jsonify
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Gauge
from pyecharts.charts import Page
import threading
from main import Main

m = Main()
m.main()


app = Flask(__name__, static_folder="templates")

x = [">-30", '-39~-48', '-48~-57', '-57~-66', '-66~-75', '-75~-84', '-84~-93', '-93~-102', '-102~-111', '-111~-120', '<-120']
y = [randrange(0, 100) for _ in range(11)]
ttl = ''
def bar_base() -> Bar:
    global x, y, ttl
    # try:
    x, y, ttl = m.solveData(m.wLs1)
    # except:
        # print('EROdate')
    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("数量", y)
        .set_global_opts(title_opts=opts.TitleOpts(title="五分钟客流量", subtitle="顾堪予的项目"), 
                         xaxis_opts=opts.AxisOpts(name="强度", axislabel_opts=opts.LabelOpts(font_size=16, rotate=-15), name_textstyle_opts=opts.TextStyleOpts(font_size = 24)), 
                         yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 20))
                         )
        .set_series_opts(label_opts=opts.LabelOpts(position='top', font_size = 20))
    )
    # d = (
    #     Gauge()
    #     .add(series_name="业务指标", data_pair=[["完成率", 55.5]], radius="50%")
    #     .set_series_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"))
    #     # .set_global_opts(legend_opts=opts.LegendOpts(type_="scroll", pos_left="right", orient="vertical"),
    # )
    # e = (
    #     Page(layout=Page.DraggablePageLayout)
    #     .add(c, d)
    # )
    return c

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route("/ttl")
def totl():
    return str(ttl)

# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def main():
    app.after_request(after_request)
    app.run(host='0.0.0.0',
      port= 5000,
      # debug=True
      )

if __name__ == "__main__":
    main()