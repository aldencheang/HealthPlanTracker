import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_handler import InsurancePlanHandler
from utils.auth_handler import AuthHandler
from utils.visualizations import (
    create_benefits_usage_chart,
    create_plan_type_distribution,
    create_benefits_progress
)

# Page configuration
st.set_page_config(
    page_title="Nest - Healthcare Benefits Dashboard",
    page_icon="🪹",
    layout="wide"
)

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize handlers
auth_handler = AuthHandler()
plan_handler = InsurancePlanHandler()

def show_menu():
    menu_items = ["Blog", "Roadmap", "Features"]
    menu = st.selectbox("☰", ["Menu"] + menu_items, key="menu_dropdown")
    return menu

def features_page():
    st.title("Nest Features")

    features = [
        {
            "icon": "📊",
            "title": "Smart Plan Comparison",
            "description": "Compare different healthcare plans side by side with our intelligent comparison tool."
        },
        {
            "icon": "🤖",
            "title": "AI Plan Recommendations",
            "description": "Get personalized plan recommendations based on your lifestyle and needs."
        },
        {
            "icon": "👨‍👩‍👧‍👦",
            "title": "Family Benefits Management",
            "description": "Manage the entire family's healthcare benefits in one place."
        },
        {
            "icon": "📱",
            "title": "Mobile Access",
            "description": "Access your benefits information anywhere, anytime."
        },
        {
            "icon": "🏥",
            "title": "Provider Network",
            "description": "Find and manage in-network healthcare providers easily."
        },
        {
            "icon": "⏰",
            "title": "Smart Reminders",
            "description": "Never miss important deadlines with automated reminders."
        }
    ]

    st.markdown('<div class="features-grid">', unsafe_allow_html=True)
    for feature in features:
        st.markdown(f"""
        <div class="feature-item">
            <div style="font-size: 3rem">{feature['icon']}</div>
            <h3>{feature['title']}</h3>
            <p>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def landing_page():
    menu = show_menu()

    if menu == "Blog":
        st.title("Healthcare Insights")
        # Blog Article 1
        st.markdown("""
        <div class="blog-card">
            <div class="blog-image" style="background-color: #f0f2f6;">
                📊 Healthcare Statistics Visualization
            </div>
            <div class="blog-content">
                <h2 class="blog-title">The Hidden Cost of Unused Healthcare Benefits</h2>
                <p class="blog-excerpt">Studies show that Americans leave billions in healthcare benefits unused each year. Learn how Nest helps you maximize your benefits and avoid leaving money on the table.</p>
                <p>Recent studies indicate that the average American family loses over $750 annually in unused healthcare benefits. This represents a significant portion of their healthcare investment that could be better utilized for preventive care and necessary medical procedures.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Blog Article 2
        st.markdown("""
        <div class="blog-card">
            <div class="blog-image" style="background-color: #f0f2f6;">
                🏥 Healthcare Provider Network
            </div>
            <div class="blog-content">
                <h2 class="blog-title">Maximizing Your Healthcare Network</h2>
                <p class="blog-excerpt">Understanding your provider network can save you thousands. Discover how Nest simplifies finding and managing in-network healthcare providers.</p>
                <p>Out-of-network charges can be up to 5 times higher than in-network rates. Nest helps you stay within your network and manage your healthcare costs effectively.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "Roadmap":
        st.title("Product Roadmap")
        # Stage 1: MVP
        st.markdown("""
        <div class="roadmap-stage">
            <h3 class="roadmap-title">Stage 1: MVP (Current)</h3>
            <ul class="roadmap-features">
                <li>Basic benefits tracking and management</li>
                <li>Family member and dependent profiles</li>
                <li>Healthcare provider directory</li>
                <li>Benefits usage analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Stage 2: Enhanced Features
        st.markdown("""
        <div class="roadmap-stage">
            <h3 class="roadmap-title">Stage 2: Enhanced Features (Q2 2025)</h3>
            <ul class="roadmap-features">
                <li>Integration with major healthcare portals</li>
                <li>Automated benefits tracking</li>
                <li>Smart notifications for unused benefits</li>
                <li>Mobile app launch</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Stage 3: Provider Integration
        st.markdown("""
        <div class="roadmap-stage">
            <h3 class="roadmap-title">Stage 3: Provider Integration (Q3 2025)</h3>
            <ul class="roadmap-features">
                <li>Direct appointment scheduling</li>
                <li>Real-time provider availability</li>
                <li>Telehealth integration</li>
                <li>Digital health records management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Stage 4: AI and Automation
        st.markdown("""
        <div class="roadmap-stage">
            <h3 class="roadmap-title">Stage 4: AI and Automation (Q4 2025)</h3>
            <ul class="roadmap-features">
                <li>AI-powered benefits optimization</li>
                <li>Predictive healthcare spending analysis</li>
                <li>Automated claims tracking</li>
                <li>Personalized wellness recommendations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "Features":
        features_page()
    else:
        # Hero Section with modern styling
        st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Nest 🪹</h1>
            <p class="hero-subtitle">Simplify Your Healthcare Journey</p>
        </div>
        """, unsafe_allow_html=True)

        # Feature Highlights
        st.markdown("""
        <h2 class="section-title">Why Choose Nest? ✨</h2>
        <p class="section-subtitle">Streamline your healthcare benefits management with our intelligent platform</p>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Smart Analytics</h3>
                <p>Track and optimize your benefits with AI-powered insights and recommendations.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3 class="feature-title">Personalized Plans</h3>
                <p>Get tailored healthcare plan recommendations based on your unique needs.</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">👨‍👩‍👧‍👦</div>
                <h3 class="feature-title">Family First</h3>
                <p>Manage your entire family's healthcare journey in one secure platform.</p>
            </div>
            """, unsafe_allow_html=True)

        # Testimonials Section
        st.markdown("""
        <div class="testimonial-section">
            <h2 class="section-title">What Our Users Say 💬</h2>
            """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="testimonial-card">
                <p class="testimonial-text">"Nest transformed how I manage healthcare for my family. The AI recommendations helped me save over $2,000 in unused benefits last year!"</p>
                <div class="testimonial-author">
                    <div class="testimonial-avatar">👩‍💼</div>
                    <div>
                        <p>Sarah Martinez</p>
                        <small>Healthcare Professional & Mother of Two</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="testimonial-card">
                <p class="testimonial-text">"As an HR manager, Nest has made it incredibly easy to help our employees make informed decisions about their healthcare plans."</p>
                <div class="testimonial-author">
                    <div class="testimonial-avatar">👨‍💼</div>
                    <div>
                        <p>Michael Chen</p>
                        <small>HR Director at TechCorp</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Perfect For Section
        st.markdown("""
        <h2 class="section-title">Perfect For You 🎯</h2>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="user-persona">
                <div class="user-persona-icon">👨‍👩‍👧‍👦</div>
                <div class="user-persona-title">Families</div>
                <p>Simplify healthcare for your entire family with smart benefit tracking and provider management.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="user-persona">
                <div class="user-persona-icon">👩‍💼</div>
                <div class="user-persona-title">Professionals</div>
                <p>Maximize your employer benefits and make informed healthcare decisions.</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="user-persona">
                <div class="user-persona-icon">👥</div>
                <div class="user-persona-title">HR Teams</div>
                <p>Empower your employees with a powerful healthcare benefits management platform.</p>
            </div>
            """, unsafe_allow_html=True)

        # Join Beta Button
        st.markdown("""
        <a href="#" class="join-beta-button" onclick="handleBetaClick()">
            Join Beta 🚀
        </a>
        """, unsafe_allow_html=True)

        if st.button("Already have access? Sign in →"):
            st.session_state.show_login = True
            st.rerun()


def login_page():
    st.title("Beta Access - Login")

    if st.button("← Back to Home"):
        st.session_state.show_login = False
        st.rerun()

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.form_submit_button("Login"):
                success, message = auth_handler.login_user(username, password)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

    with tab2:
        with st.form("signup_form"):
            new_username = st.text_input("Choose Username")
            new_password = st.text_input("Choose Password", type="password")
            email = st.text_input("Email")
            zip_code = st.text_input("ZIP Code (for finding local providers)")

            if st.form_submit_button("Sign Up"):
                success, message = auth_handler.register_user(
                    new_username, new_password, email, zip_code
                )
                if success:
                    st.success(message)
                    auth_handler.login_user(new_username, new_password)
                    st.rerun()
                else:
                    st.error(message)

def manage_dependents_page():
    st.title("Manage Dependents")

    # Add new dependent
    with st.form("add_dependent_form"):
        st.subheader("Add New Dependent")
        name = st.text_input("Dependent's Full Name")
        relationship = st.selectbox("Relationship", [
            "Spouse", "Child", "Parent", "Other"
        ])
        dob = st.date_input("Date of Birth")

        # Select applicable plans
        available_plans = plan_handler.get_filtered_plans()
        if not available_plans.empty:
            plan_options = available_plans['plan_name'].tolist()
            selected_plans = st.multiselect(
                "Select Applicable Insurance Plans",
                options=plan_options
            )
        else:
            st.warning("Please add insurance plans before adding dependents.")
            selected_plans = []

        submit_button = st.form_submit_button("Add Dependent")
        if submit_button and name and relationship and selected_plans:
            plan_handler.add_dependent({
                'name': name,
                'relationship': relationship,
                'date_of_birth': dob.strftime('%Y-%m-%d'),
                'plan_ids': selected_plans
            })
            st.success(f"Dependent {name} added successfully!")
            st.rerun()
        elif submit_button:
            st.error("Please fill in all required fields.")

    # Display existing dependents
    st.subheader("Your Dependents")
    dependents = plan_handler.get_dependents()
    if not dependents.empty:
        for _, dependent in dependents.iterrows():
            with st.expander(f"{dependent['name']} - {dependent['relationship']}"):
                st.write(f"Date of Birth: {dependent['date_of_birth']}")
                st.write("Covered under plans:", ", ".join(dependent['plan_ids']))
    else:
        st.info("No dependents added yet.")

def provider_search_page():
    st.title("Find and Save Healthcare Providers")
    user_data = auth_handler.get_user_data(auth_handler.get_current_user())

    # Add new provider
    with st.form("add_provider_form"):
        st.subheader("Add Healthcare Provider")
        provider_name = st.text_input("Provider Name")
        specialty = st.selectbox("Specialty", [
            "Primary Care", "Pediatrics", "Dental", "Vision", 
            "Cardiology", "Dermatology", "Other"
        ])
        address = st.text_input("Address")
        phone = st.text_input("Phone Number")
        accepting_new = st.checkbox("Accepting New Patients")

        available_providers = plan_handler.get_filtered_plans()['provider'].unique()
        insurance_accepted = st.multiselect(
            "Insurance Plans Accepted",
            options=available_providers if len(available_providers) > 0 else ["No plans available"]
        )

        plan_types = st.multiselect(
            "Types of Plans Accepted",
            options=["HMO", "PPO", "EPO", "POS"]
        )

        submit_button = st.form_submit_button("Add Provider")
        if submit_button and provider_name and specialty and address and phone:
            plan_handler.add_provider({
                'name': provider_name,
                'specialty': specialty,
                'address': address,
                'phone': phone,
                'accepting_new_patients': accepting_new,
                'insurance_accepted': insurance_accepted,
                'plan_types': plan_types
            })
            st.success(f"Provider {provider_name} added successfully!")
            st.rerun()
        elif submit_button:
            st.error("Please fill in all required fields.")

    # Search providers
    st.subheader("Search Providers")
    providers_df = plan_handler.get_providers()

    if not providers_df.empty:
        col1, col2 = st.columns(2)
        with col1:
            specialties = ["All"] + list(providers_df['specialty'].unique())
            search_specialty = st.selectbox(
                "Filter by Specialty",
                options=specialties
            )
        with col2:
            accepting_new_only = st.checkbox("Show Only Providers Accepting New Patients")

        # Display filtered providers
        filtered_providers = plan_handler.get_providers(
            specialty=search_specialty,
            accepting_new=accepting_new_only if accepting_new_only else None
        )

        if not filtered_providers.empty:
            for _, provider in filtered_providers.iterrows():
                with st.expander(f"{provider['name']} - {provider['specialty']}"):
                    st.write(f"Address: {provider['address']}")
                    st.write(f"Phone: {provider['phone']}")
                    st.write("Insurance Accepted:", ", ".join(provider['insurance_accepted']))
                    st.write("Plan Types:", ", ".join(provider['plan_types']))
                    if provider['accepting_new_patients']:
                        st.success("✔️ Accepting New Patients")
                    else:
                        st.warning("❌ Not Accepting New Patients")
        else:
            st.info("No providers found matching your criteria.")
    else:
        st.info("No providers have been added yet.")

def main_app():
    # Sidebar navigation
    st.sidebar.title(f"Welcome, {auth_handler.get_current_user()}")

    if st.sidebar.button("Logout"):
        auth_handler.logout_user()
        st.rerun()

    page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Add Plan", "Plan Details", "Manage Dependents", "Healthcare Providers"]
    )

    if page == "Dashboard":
        st.title("Healthcare Benefits Dashboard")

        # Filtering options
        col1, col2 = st.columns(2)
        with col1:
            plan_type_filter = st.selectbox(
                "Filter by Plan Type",
                ["All"] + list(plan_handler.get_filtered_plans()['plan_type'].unique())
            )
        with col2:
            provider_filter = st.selectbox(
                "Filter by Provider",
                ["All"] + list(plan_handler.get_filtered_plans()['provider'].unique())
            )

        # Apply filters
        filtered_plans = plan_handler.get_filtered_plans(
            plan_type=None if plan_type_filter == "All" else plan_type_filter,
            provider=None if provider_filter == "All" else provider_filter
        )

        # Display summary visualizations
        if not filtered_plans.empty:
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(create_benefits_usage_chart(filtered_plans), use_container_width=True)
            with col2:
                st.plotly_chart(create_plan_type_distribution(filtered_plans), use_container_width=True)

            # Display plan cards
            st.subheader("Your Insurance Plans")
            for idx, plan in filtered_plans.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([2, 2, 1])
                    with col1:
                        st.markdown(f"""
                        <div class="plan-card">
                            <div class="plan-header">{plan['plan_type']} - {plan['plan_name']}</div>
                            <p>Provider: {plan['provider']}<br>
                            Member ID: {plan['member_id']}<br>
                            Coverage: {plan['coverage_start']} to {plan['coverage_end']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    with col2:
                        st.plotly_chart(create_benefits_progress(
                            plan['benefits_used'],
                            plan['total_benefits'],
                            plan['plan_name']
                        ), use_container_width=True)
                    with col3:
                        st.markdown(f"""
                        <div class="benefit-tracker">
                            <p>Deductible: ${plan['deductible']}<br>
                            Out of Pocket Max: ${plan['out_of_pocket_max']}</p>
                        </div>
                        """, unsafe_allow_html=True)

    elif page == "Find Providers":
        st.title("Find In-Network Providers")
        user_data = auth_handler.get_user_data(auth_handler.get_current_user())

        st.info(f"Showing providers near ZIP code: {user_data['zip_code']}")
        st.warning("This feature is coming soon! We'll help you find local in-network providers based on your insurance plans and location.")

        # Placeholder for provider search functionality
        with st.expander("Provider Search Options"):
            st.selectbox("Specialty", ["Primary Care", "Dental", "Vision", "Specialist"])
            st.number_input("Distance (miles)", min_value=5, max_value=50, value=10)
            st.button("Search Providers")

    elif page == "Add Plan":
        st.title("Add New Insurance Plan")

        with st.form("new_plan_form"):
            plan_type = st.selectbox("Plan Type", ["Health", "Dental", "Vision", "Other"])
            provider = st.text_input("Insurance Provider")
            plan_name = st.text_input("Plan Name")
            member_id = st.text_input("Member ID")

            col1, col2 = st.columns(2)
            with col1:
                coverage_start = st.date_input("Coverage Start Date")
            with col2:
                coverage_end = st.date_input("Coverage End Date")

            col1, col2 = st.columns(2)
            with col1:
                deductible = st.number_input("Deductible ($)", min_value=0.0)
            with col2:
                out_of_pocket_max = st.number_input("Out of Pocket Maximum ($)", min_value=0.0)

            total_benefits = st.number_input("Total Benefits ($)", min_value=0.0)

            if st.form_submit_button("Add Plan"):
                new_plan = {
                    'plan_type': plan_type,
                    'provider': provider,
                    'plan_name': plan_name,
                    'member_id': member_id,
                    'coverage_start': coverage_start,
                    'coverage_end': coverage_end,
                    'deductible': deductible,
                    'out_of_pocket_max': out_of_pocket_max,
                    'benefits_used': 0.0,
                    'total_benefits': total_benefits
                }
                plan_handler.add_plan(new_plan)
                st.success("Plan added successfully!")

    elif page == "Plan Details":
        st.title("Plan Details and Benefits Tracking")

        plans = plan_handler.get_filtered_plans()
        if not plans.empty:
            selected_plan = st.selectbox(
                "Select Plan",
                plans['plan_name'].unique(),
                format_func=lambda x: f"{x} ({plans[plans['plan_name']==x]['plan_type'].iloc[0]})"
            )

            plan_data = plans[plans['plan_name'] == selected_plan].iloc[0]

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="plan-card">
                    <h3>Plan Information</h3>
                    <p>Type: {plan_data['plan_type']}<br>
                    Provider: {plan_data['provider']}<br>
                    Member ID: {plan_data['member_id']}<br>
                    Coverage Period: {plan_data['coverage_start']} to {plan_data['coverage_end']}</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="plan-card">
                    <h3>Benefits Summary</h3>
                    <p>Total Benefits: ${plan_data['total_benefits']}<br>
                    Benefits Used: ${plan_data['benefits_used']}<br>
                    Remaining Benefits: ${plan_data['total_benefits'] - plan_data['benefits_used']}</p>
                </div>
                """, unsafe_allow_html=True)

            # Update benefits used
            with st.form("update_benefits"):
                benefit_amount = st.number_input("Enter benefit usage amount ($)", min_value=0.0)
                if st.form_submit_button("Update Benefits"):
                    plan_index = plans[plans['plan_name'] == selected_plan].index[0]
                    plan_handler.update_benefits_used(plan_index, benefit_amount)
                    st.success("Benefits updated successfully!")
                    st.rerun()

            # Export functionality
            if st.button("Export Plan Details"):
                csv = plan_handler.export_plans()
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="insurance_plans.csv",
                    mime="text/csv"
                )
        else:
            st.info("No plans added yet. Please add a plan first.")
    elif page == "Manage Dependents":
        manage_dependents_page()
    elif page == "Healthcare Providers":
        provider_search_page()

# Main app flow
if 'show_login' not in st.session_state:
    st.session_state.show_login = False

if auth_handler.get_current_user() is None:
    if st.session_state.show_login:
        login_page()
    else:
        landing_page()
else:
    main_app()