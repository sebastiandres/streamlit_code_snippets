import streamlit as st

from .shared_functions import page_header, documentation, breakline, what4, examples

def display_page(my_title):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    page_header(my_title)
    st.markdown("These are methods used to display different types of text.")

    # Title
    with st.beta_expander("Title"):
        what4("To put a title on the page. Notice it will put an anchor (link) next to the title!!!")
        examples()
        with st.echo('below'):
            st.title('My Title')
        breakline()
        with st.echo('below'):
            st.title('Another Title', anchor="CustomTitleAnchor")
        documentation("title")

    # Header 
    with st.beta_expander("Header"):
        what4("To put a header on the page. Notice it will put an anchor (link) next to the header!!!")
        examples()
        with st.echo('below'):
            st.header('My Header')
        breakline()
        with st.echo('below'):
            st.header('Another Header', anchor="CustomHeaderAnchor")
        documentation("header")

    # Subheader 
    with st.beta_expander("Subheader"):
        what4("To put a subheader on the page. Notice it will put an anchor (link) next to the subheader!!!")
        examples()
        with st.echo('below'):
            st.subheader('My Subheader')
        breakline()
        with st.echo('below'):
            st.subheader('Another Subheader', anchor="CustomSubheaderAnchor")
        documentation("subheader")

    # Markdown
    with st.beta_expander("Markdown"):
        what4("To display a text created with markdown.")
        examples()
        with st.echo('below'):
            st.markdown('This is **Markdown** in all its _glory_ :heart_eyes_cat:')
        breakline()
        with st.echo('below'):
            # Trick for markdown on several lines
            lines = [
                      "This is a **_multiline_** markdown comment.",
                      "* One :dog:",
                      "* Two :cat:",
                      "* And latex, from $\\alpha$ to $\\omega$",
                      ]
            st.markdown("\n".join(lines))
        documentation("markdown")
        st.markdown("[Github's markdown documentation](https://guides.github.com/features/mastering-markdown/)")
        st.markdown("[Supported emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)")

    # Latex
    with st.beta_expander("Latex"):
        what4("To display a text created with markdown.")
        examples()
        with st.echo('below'):
            st.latex(r''' e^{i\pi} + 1 = 0 ''')    
        breakline()
        with st.echo('below'):
            st.latex(r'''\begin{pmatrix} a & b\\ c & d \end{pmatrix}''')
        breakline()
        documentation("latex")
        st.markdown("[Supported latex](https://katex.org/docs/supported.html)")
        st.markdown("Observation: This is intended to display latex formulas, not for mixing text and math.")

    # (fixed width) Text
    with st.beta_expander("Text"):
        what4("To display a fixed width text.")
        examples()
        with st.echo('below'):
            st.text('My fixed width text')
        breakline()
        with st.echo('below'):
            st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        documentation("text")
