import streamlit as st

from .shared_functions import page_header, documentation, breakline

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    
    # Title
    with st.beta_expander("Title"):
        # what4("To put a title on the page. Notice it will put an anchor (link) next to the title!!!")
        st.markdown("**What for?**: To put a title on the page. Notice it automatically gets a anchor (link)!")
        # examples()
        st.markdown("Examples:")
        with st.echo('below'):
            st.title('My Title')
        with st.echo('below'):
            st.title('Another Title', anchor="CustomTitleAnchor")
        documentation("title")

    # Header 
    with st.beta_expander("Header"):
        with st.echo('below'):
            st.header('My Header')
        with st.echo('below'):
            st.header('Another Header', anchor="CustomHeaderAnchor")
        documentation("header")

    # Subheader 
    with st.beta_expander("Subheader"):
        with st.echo('below'):
            st.subheader('My Subheader')
        with st.echo('below'):
            st.subheader('Another Subheader', anchor="CustomSubheaderAnchor")
        documentation("subheader")

    # (fixed width) Text
    with st.beta_expander("Text"):
        with st.echo('below'):
            st.text('My fixed width text')
        documentation("text")

    # Markdown
    with st.beta_expander("Markdown"):
        with st.echo('below'):
            st.markdown('This is **Markdown** in all its _glory_ :heart_eyes_cat:')
        breakline()
        with st.echo('below'):
            # Trick for markdown on several lines
            lines = [
                      "This is a **_multiline_** markdown comment.",
                      "* One :dog:",
                      "* Two :cat:",
                      ]
            st.markdown("\n".join(lines))
        documentation("markdown")
        st.markdown("[Github's markdown documentation](https://guides.github.com/features/mastering-markdown/)")
        st.markdown("[Supported emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)")

    # Latex
    with st.beta_expander("Latex"):
        with st.echo('below'):
            st.latex(r''' e^{i\pi} + 1 = 0 ''')    
        breakline()
        with st.echo('below'):
            st.latex(r'''\begin{pmatrix} a & b\\ c & d \end{pmatrix}''')
        breakline()
        documentation("latex")
        st.markdown("[Supported latex](https://katex.org/docs/supported.html)")
        st.markdown("Observation: This is intended to display latex formulas, not for mixing text and math.")

