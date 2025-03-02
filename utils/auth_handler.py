import streamlit as st
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
import pandas as pd

class AuthHandler:
    def __init__(self):
        # Initialize user data storage
        if 'users' not in st.session_state:
            st.session_state.users = pd.DataFrame(columns=[
                'username', 'password_hash', 'email', 'zip_code'
            ])
        if 'current_user' not in st.session_state:
            st.session_state.current_user = None

    def hash_password(self, password):
        """Hash a password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password, password_hash):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), password_hash)

    def register_user(self, username, password, email, zip_code):
        """Register a new user"""
        if username in st.session_state.users['username'].values:
            return False, "Username already exists"

        password_hash = self.hash_password(password)
        new_user = pd.DataFrame([{
            'username': username,
            'password_hash': password_hash,
            'email': email,
            'zip_code': zip_code
        }])
        st.session_state.users = pd.concat([st.session_state.users, new_user], ignore_index=True)
        return True, "Registration successful"

    def login_user(self, username, password):
        """Login a user"""
        if not username or not password:
            return False, "Please enter both username and password"

        user_data = st.session_state.users[st.session_state.users['username'] == username]
        if user_data.empty:
            return False, "Invalid username or password"

        stored_hash = user_data.iloc[0]['password_hash']
        if self.verify_password(password, stored_hash):
            st.session_state.current_user = username
            return True, "Login successful"
        return False, "Invalid username or password"

    def logout_user(self):
        """Logout current user"""
        st.session_state.current_user = None

    def get_current_user(self):
        """Get current logged in user"""
        return st.session_state.current_user

    def get_user_data(self, username):
        """Get user data"""
        user_data = st.session_state.users[st.session_state.users['username'] == username]
        if user_data.empty:
            return None
        return user_data.iloc[0]