
import datetime
from streamlit.testing.v1 import AppTest

at=AppTest.from_file('app.py',default_timeout=10).run()

def test_title():    
    assert at.title[0].value=="Car Sales In the USA"

def test_selectbox():
    assert at.selectbox[0].options[1] == "year"  

def test_multiselect_make():
    assert at.multiselect[0].options[0]=="kia"

def test_multiselect_model():
    assert at.multiselect[1].options[0]=="Sorento"

def test_slider_year():
    assert at.slider[0].value[0] == 1984
    assert at.slider[0].value[1] == 2015

def test_slider_condition():
    assert at.slider[1].value[0] == 1
    assert at.slider[1].value[1] == 49

def test_slider_price():
    assert at.slider[4].value[0] == 1
    assert at.slider[4].value[1] == 230000

def test_input_date():
    assert at.date_input[0].value[0] == datetime.date(2014,1,1)
    assert at.date_input[0].value[1] == datetime.date(2015,7,21)

def test_types():
    assert at.dataframe[0].value.dtypes.iloc[0]=="int64"
    assert at.dataframe[0].value.dtypes.iloc[2]=="category"
    assert at.dataframe[0].value.dtypes.iloc[8]=="float64"
    assert at.dataframe[0].value.dtypes.iloc[14]=="datetime64[ns]"

def test_filter_make_model():
    at.multiselect[0].select('ferrari').run()
    assert at.multiselect[1].options==['California','F430','360','458 Italia']