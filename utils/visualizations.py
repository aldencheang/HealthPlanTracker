import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_benefits_usage_chart(plan_data):
    """Create a bar chart showing benefits usage per plan."""
    fig = px.bar(
        plan_data,
        x='plan_name',
        y=['benefits_used', 'total_benefits'],
        title='Benefits Usage by Plan',
        labels={'value': 'Amount ($)', 'plan_name': 'Plan Name'},
        barmode='group',
        color_discrete_sequence=['#0066cc', '#28a745']
    )
    return fig

def create_plan_type_distribution(plan_data):
    """Create a pie chart showing distribution of plan types."""
    plan_distribution = plan_data['plan_type'].value_counts()
    fig = px.pie(
        values=plan_distribution.values,
        names=plan_distribution.index,
        title='Distribution of Insurance Plans',
        color_discrete_sequence=['#0066cc', '#28a745', '#dc3545', '#ffc107']
    )
    return fig

def create_benefits_progress(used, total, plan_name):
    """Create a progress gauge for benefits usage."""
    percentage = (used / total) * 100 if total > 0 else 0
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        title={'text': f"{plan_name} Benefits Usage"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#0066cc"},
            'steps': [
                {'range': [0, 50], 'color': "#e6f3ff"},
                {'range': [50, 75], 'color': "#b3d9ff"},
                {'range': [75, 100], 'color': "#80bfff"}
            ]
        }
    ))
    return fig
