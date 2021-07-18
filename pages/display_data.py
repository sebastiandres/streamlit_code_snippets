import streamlit as st
import pandas as pd
import numpy as np

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """

    page_header(my_title)
    
    # Write
    with st.beta_expander("Write numbers"):
        with st.echo('below'):
            st.write(42) # Integers
        breakline()
        with st.echo('below'):
            st.write(3.141592) # Floats
        breakline()
        with st.echo('below'):
            st.write(3 + 4j) # Complex numbers
        documentation("write")
    with st.beta_expander("Write lists, sets and dictionaries"):
        with st.echo('below'):
            st.write({1,1,2,3,3}) # Sets
        breakline()
        with st.echo('below'):
            st.write([1,1,2,3,3]) # Lists
        breakline()
        with st.echo('below'):
            st.write({"one":3, "two":2, "three":5}) # Dicts
        breakline()
        with st.echo('below'):
            my_variable = [42, 3.14, {2, 3}, [1,2,3,4,5], {1:"1", 2:"2", 3:"3"}]
            st.write(my_variable) # General variables
        documentation("write")
    with st.beta_expander("Write text"):
        st.write("You can write general markdown")
        with st.echo('below'):
            st.write("This _is_ a **string**") # Strings
        breakline()
        with st.echo('below'):
            st.write(42, 3.14, {2, 3}, [1,2,3,4,5], {1:"1", 2:"2", 3:"3"}) # Several arguments 
        documentation("write")
    with st.beta_expander("Dataframes"):
        with st.echo('below'):
            st.dataframe(pd.DataFrame(data={'col1': [1, 2, 3], 'col2': [3.5, 4.5, 5.5]}))
        documentation("dataframe")
    # Table
    with st.beta_expander("Tables"):
        with st.echo('below'):
            st.table([[1,2,3],[2,3,4]])
        with st.echo('below'):
            X = np.random.randn(5, 5)
            st.table(X)
        documentation("table")
    # Json
    with st.beta_expander("JSON"):
        with st.echo('below'):
            st.json({'foo':'bar','fu':'ba'})
        documentation("json")
