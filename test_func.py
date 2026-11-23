from reader import read_csv
from validator import valid
from transformer import convert_prices

def test_read_csv(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("id,name\n1,Ana\n", encoding="utf-8")
    assert read_csv(csv_file) == [{"id": "1", "name": "Ana"}]

def test_valid():
    assert valid("olist_mini/orders.csv") is True

def test_convert_prices():
    rows = convert_prices("olist_mini/order_items.csv")
    assert isinstance(rows[0]["price"], float)