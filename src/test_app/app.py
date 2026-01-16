"""
Docstring for myapp.App
"""

import streamlit as st
from test_app.pages.test_pages import test
# from myapp.common.container import Container
# from myapp.common.database.test_db import Test_Database
# from myapp.common.state_manager import StateManager


def main():
    """
    Docstring for main
    """

    # if "Container" not in st.session_state:
    #     db: Test_Database = Test_Database()
    #     container: Container = Container(db)
    #     st.session_state.Container = container

    # auth_pages = [st.Page("test_app/pages/home.py", title="Talksy")]

    # pages = [
    #     st.Page("test_app/pages/login.py", title="Login"),
        
    #     # st.Page("myapp/pages/new_account.py", title="New Account"),
    # ]

    # if StateManager.get_user() is not None and StateManager.get_authenticated():
    # else:
    #     pg = st.navigation(pages, position="top")
    print(test())
    # pg = st.navigation([st.Page("test_app/pages/login.py", title="Login")], position="top")
    # pg.run()


if __name__ == "__main__":
    main()
