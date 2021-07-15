import streamlit as st

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    st.title(my_title)
    
    with st.beta_expander("Line chart"):
        with st.echo():
            data = [1,2,3,2,1,2,3,2,1]
            st.line_chart(data)
    
    with st.beta_expander("Area chart"):
        with st.echo():
            data = [1,2,3,2,1,2,3,2,1]
            st.area_chart(data)
    
    with st.beta_expander("Bar chart"):
        with st.echo():
            st.code("FIX ME")
            #st.bar_chart(data)
    
    with st.beta_expander("Pyplot chart"):
        with st.echo():
            st.code("FIX ME")
            #st.pyplot(fig)
    
    with st.beta_expander("Altair chart"):
        with st.echo():
            st.code("FIX ME")
            #st.altair_chart(data)
    
    with st.beta_expander("Vega Lite chart"):
        with st.echo():
            st.code("FIX ME")
            #st.vega_lite_chart(data)
    
    with st.beta_expander("Plotly chart"):
        with st.echo():
            st.code("FIX ME")
            #st.plotly_chart(data)
    
    with st.beta_expander("Bokeh chart"):
        with st.echo():
            st.code("FIX ME")
            #st.bokeh_chart(data)
    
    with st.beta_expander("Pydeck chart"):
        with st.echo():
            st.code("FIX ME")
            #st.pydeck_chart(data)
    
    with st.beta_expander("Deck GL chart"):
        with st.echo():
            st.code("FIX ME")
            #st.deck_gl_chart(data)
    
    with st.beta_expander("Graphviz chart"):
        with st.echo():
            st.code("FIX ME")
        #st.graphviz_chart(data)
    
    with st.beta_expander("Maps"):
        with st.echo():
            st.code("FIX ME")
            #st.map(data)