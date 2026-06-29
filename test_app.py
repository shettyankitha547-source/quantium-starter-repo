from app import app


def test_header_exists():
    assert "Pink Morsel" in str(app.layout)


def test_graph_exists():
    assert "sales-chart" in str(app.layout)


def test_region_picker_exists():
    assert "region-filter" in str(app.layout)