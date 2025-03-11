import streamlit as st #type: ignore

# Library Manager App

# Title
st.title("📚 Personal Library Manager")

# Ek dictionary banayein jisme books store honge
if "library" not in st.session_state:
    st.session_state.library = {}

# Functions define karein
def add_book():
    """
    Ye function book add karega library mein.
    """
    book_name = st.text_input("Book ka naam likhein:")
    author_name = st.text_input("Author ka naam likhein:")
    if st.button("Add Book"):
        if book_name and author_name:
            st.session_state.library[book_name] = author_name
            st.success(f"'{book_name}' library mein add ho gayi hai! 🎉")
        else:
            st.error("Book aur author ka naam zaroori hai.")

def delete_book():
    """
    Ye function book delete karega library se.
    """
    book_name = st.text_input("Delete karne ke liye book ka naam likhein:")
    if st.button("Delete Book"):
        if book_name in st.session_state.library:
            del st.session_state.library[book_name]
            st.success(f"'{book_name}' library se delete ho gayi hai! 🗑️")
        else:
            st.error(f"'{book_name}' library mein nahi mili.")

def view_books():
    """
    Ye function library ki books ki list show karega.
    """
    if st.session_state.library:
        st.write("Library ki books:")
        for book, author in st.session_state.library.items():
            st.write(f"- {book} by {author}")
    else:
        st.write("Library khali hai.")

def search_book():
    """
    Ye function book search karega library mein.
    """
    book_name = st.text_input("Search karne ke liye book ka naam likhein:")
    if st.button("Search Book"):
        if book_name in st.session_state.library:
            st.success(f"'{book_name}' library mein mili hai. Author: {st.session_state.library[book_name]} 🎉")
        else:
            st.error(f"'{book_name}' library mein nahi mili.")

# Sidebar mein options
st.sidebar.header("Options")
option = st.sidebar.radio(
    "Choose an option:",
    ("📖 Books Ki List Dekhein", "➕ Book Add Karein", "🗑️ Book Delete Karein", "🔍 Book Search Karein")
)

# Option ke hisab se function call karein
if option == "📖 Books Ki List Dekhein":
    view_books()
elif option == "➕ Book Add Karein":
    add_book()
elif option == "🗑️ Book Delete Karein":
    delete_book()
elif option == "🔍 Book Search Karein":
    search_book()