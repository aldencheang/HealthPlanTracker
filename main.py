import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_handler import InsurancePlanHandler
from utils.visualizations import (
    create_benefits_usage_chart,
    create_plan_type_distribution,
    create_benefits_progress
)

# Page configuration
st.set_page_config(
    page_title="Healthcare Benefits Dashboard",
    page_icon="🏥",
    layout="wide"
)

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize the insurance plan handler
plan_handler = InsurancePlanHandler()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Add Plan", "Plan Details"])

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
                st.experimental_rerun()
        
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
