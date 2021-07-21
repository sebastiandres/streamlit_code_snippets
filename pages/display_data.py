import streamlit as st
import pandas as pd
import numpy as np

from .shared_functions import page_header, documentation, breakline, what4, examples

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """

    page_header(my_title)
    st.write("Methods used to display different types of data.")
    st.write("TLDR; You can safely assume that you can always use method `write`.")
    
    # Numbers
    with st.beta_expander("Write numbers"):
        what4("To write different numbers.")
        examples()
        with st.echo('below'):
            st.write(42) # Integers
        breakline()
        with st.echo('below'):
            st.write(3.141592) # Floats
        breakline()
        with st.echo('below'):
            st.write(3 + 4j) # Complex numbers
        documentation("write")

    # Collections
    with st.beta_expander("Write lists, sets and dictionaries"):
        what4("To write different numbers.")
        examples()
        with st.echo('below'):
            st.write({"cat", "gato", "chat", "cat", "chat", "cat"}) # Sets
        breakline()
        with st.echo('below'):
            st.write([1, 1, 2, 3, 5, 8, 13]) # Lists
        breakline()
        with st.echo('below'):
            st.write({"one":3, "two":2, "three":5}) # Dicts
        documentation("write")

    # Arbitrary expressions
    with st.beta_expander("Write arbitrary expressions"):
        what4("You can use it similar to `print` method, with variable number of arguments.")
        examples()
        with st.echo('below'):
            x, cat = 42, 0+1j
            st.write("The value of x =", x, "and :cat: = ", cat) # Several arguments 
        breakline()
        with st.echo('below'):
            st.write(42, 3.14, {2, 3}, [1,2,3,4,5], {1:"1", 2:"2", 3:"3"}) # Several arguments 
        breakline()
        with st.echo('below'):
            my_variable = [42, 3.14, {2, 3}, [1,2,3,4,5], {1:"1", 2:"2", 3:"3"}]
            st.write(my_variable) # General variables
        documentation("write")

    # Text
    with st.beta_expander("Write text"):
        what4("You can write general markdown strings")
        examples()
        with st.echo('below'):
            st.write("This _is_ a **string**") # Strings
        documentation("write")

    # Dataframes
    with st.beta_expander("Dataframes"):
        what4("You can write dataframes")
        examples()
        with st.echo('below'):
            st.dataframe(pd.DataFrame(data={'col1': [1, 2, 3], 'col2': [3.5, 4.5, 5.5]}))
        breakline()
        with st.echo('below'):
            st.write(pd.DataFrame(data={'col1': [1, 2, 3], 'col2': [3.5, 4.5, 5.5]}))
        documentation("dataframe")

    # Table
    with st.beta_expander("Tables"):
        what4("You can write tables (but they are ugly)")
        examples()
        with st.echo('below'):
            st.table([[1,2,3],[2,3,4]])
        breakline()
        with st.echo('below'):
            X = np.random.randn(5, 5)
            st.table(X)
        breakline()
        with st.echo('below'):
            Y = np.random.randn(5, 5)
            st.write(Y)
        documentation("table")

    # JSON
    with st.beta_expander("JSON"):
        what4("You can write general JSON data")
        examples()
        with st.echo('below'):
            st.json({'foo':'bar','fu':[0, 1, 3, 5, 7, 9]})
        breakline()
        with st.echo('below'):
            st.write({'foo':'bar','fu':[0, 1, 3, 5, 7, 9]})
        documentation("json")
