from flask import Blueprint, render_template
from alpaca_trade_api.rest import REST, TimeFrame

index_page = Blueprint("index", __name__, static_folder="static", template_folder="templates")

api = REST()


def get_bars():
    bars_list = []

    def process_bar(bar):
        # process bar
        bars_list.append(bar)

    bar_iter = api.get_bars_iter("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw')
    for bar in bar_iter:
        process_bar(bar)
        
    return bars_list


@index_page.route('/', methods=["GET", "POST"])
def index():
    """
    This method returns the index page.
    :return: render_template('index.html')
    """
    # Wait and get all bars at once
    # bars = api.get_bars("AAPL", TimeFrame.Hour, "2022-05-10", "2022-05-10", adjustment='raw').df

    # Wait for individual bars to come in
    bars = get_bars()
    return render_template('index.html', bars=bars)
