import pandas as pd
from datetime import datetime
import streamlit as st

class InsurancePlanHandler:
    def __init__(self):
        # Initialize insurance plans DataFrame
        if 'insurance_plans' not in st.session_state:
            st.session_state.insurance_plans = pd.DataFrame(columns=[
                'plan_type', 'provider', 'plan_name', 'member_id',
                'coverage_start', 'coverage_end', 'deductible',
                'out_of_pocket_max', 'benefits_used', 'total_benefits'
            ])
        # Initialize dependents DataFrame
        if 'dependents' not in st.session_state:
            st.session_state.dependents = pd.DataFrame(columns=[
                'name', 'relationship', 'date_of_birth', 'plan_ids'
            ])
        # Initialize providers DataFrame
        if 'providers' not in st.session_state:
            st.session_state.providers = pd.DataFrame(columns=[
                'name', 'specialty', 'address', 'phone', 'accepting_new_patients',
                'insurance_accepted', 'plan_types'
            ])

    def add_plan(self, plan_data):
        """Add a new insurance plan to the session state."""
        new_plan = pd.DataFrame([plan_data])
        st.session_state.insurance_plans = pd.concat([st.session_state.insurance_plans, new_plan], 
                                                  ignore_index=True)

    def add_dependent(self, dependent_data):
        """Add a new dependent to the session state."""
        # Convert plan_ids list to string for storage
        dependent_data['plan_ids'] = ','.join(dependent_data['plan_ids']) if dependent_data['plan_ids'] else ''
        new_dependent = pd.DataFrame([dependent_data])
        st.session_state.dependents = pd.concat([st.session_state.dependents, new_dependent],
                                             ignore_index=True)

    def add_provider(self, provider_data):
        """Add a healthcare provider to the session state."""
        # Convert lists to strings for storage
        provider_data['insurance_accepted'] = ','.join(provider_data['insurance_accepted']) if provider_data['insurance_accepted'] else ''
        provider_data['plan_types'] = ','.join(provider_data['plan_types']) if provider_data['plan_types'] else ''
        new_provider = pd.DataFrame([provider_data])
        st.session_state.providers = pd.concat([st.session_state.providers, new_provider],
                                           ignore_index=True)

    def update_benefits_used(self, plan_index, amount):
        """Update the benefits used for a specific plan."""
        st.session_state.insurance_plans.at[plan_index, 'benefits_used'] += amount

    def get_filtered_plans(self, plan_type=None, provider=None):
        """Get filtered insurance plans based on criteria."""
        df = st.session_state.insurance_plans
        if plan_type:
            df = df[df['plan_type'] == plan_type]
        if provider:
            df = df[df['provider'] == provider]
        return df

    def get_dependents(self):
        """Get all dependents with their plans."""
        df = st.session_state.dependents.copy()
        if not df.empty:
            # Convert stored string back to list
            df['plan_ids'] = df['plan_ids'].apply(lambda x: x.split(',') if x else [])
        return df

    def get_providers(self, specialty=None, accepting_new=None):
        """Get filtered healthcare providers."""
        df = st.session_state.providers.copy()
        if not df.empty:
            # Convert stored strings back to lists
            df['insurance_accepted'] = df['insurance_accepted'].apply(lambda x: x.split(',') if x else [])
            df['plan_types'] = df['plan_types'].apply(lambda x: x.split(',') if x else [])

        if specialty and specialty != "All":
            df = df[df['specialty'] == specialty]
        if accepting_new is not None:
            df = df[df['accepting_new_patients'] == accepting_new]
        return df

    def export_plans(self):
        """Export insurance plans to CSV."""
        return st.session_state.insurance_plans.to_csv(index=False)

    def calculate_remaining_benefits(self, plan_index):
        """Calculate remaining benefits for a plan."""
        plan = st.session_state.insurance_plans.iloc[plan_index]
        return plan['total_benefits'] - plan['benefits_used']