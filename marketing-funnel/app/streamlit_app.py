import streamlit as st
import os
import sys
import zipfile
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import charts, cohort, funnel, load_data

st.set_page_config(page_title="Marketing Funnel Dashboard", layout="wide")

st.title("📊 Marketing Funnel Analytics Dashboard")

uploaded = st.file_uploader("Upload the e-commerce dataset", type="zip")

if uploaded:
    df = load_data.read_data(uploaded)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # ---------------------------------
    # GLOBAL FUNNEL
    # ---------------------------------
    st.subheader("🪜 Overall Funnel Analysis")
    funnel = funnel.funnel_conversion(df)
    st.json(funnel)
    st.pyplot(charts.plot_funnel(funnel))

    st.subheader("🔄 Funnel Sankey Plot")
    st.plotly_chart(charts.plot_sankey_funnel(funnel))  # type: ignore

    # ---------------------------------
    # COHORT RETENTION
    # ---------------------------------
    st.subheader("📅 Cohort Retention")
    retention = cohort.create_cohort_retention(df)
    st.dataframe(retention.style.format("{:.1%}"))
    # st.pyplot(charts.plot_retention_heatmap(retention))
    st.pyplot(charts.plot_cohort_retention_line(retention)) # type: ignore

    # ---------------------------------
    # FUNNEL BY COHORT
    # ---------------------------------
    st.subheader("🪜 Funnel Progression per Cohort")
    funnel_cohorts = cohort.funnel_by_cohort(df)

    styled_fc = funnel_cohorts.copy()
    for col in ["view_to_cart", "cart_to_purchase", "view_to_purchase"]:
        styled_fc[col] = styled_fc[col].apply(lambda x: f"{x:.1%}")

    st.dataframe(styled_fc)
    st.pyplot(charts.plot_funnel_cohort_heatmap(funnel_cohorts)) # type: ignore

    # ---------------------------------
    # CATEGORY-LEVEL FUNNELS
    # ---------------------------------
    st.subheader("📦 Category-Level Funnel Analysis")
    cat_df = cohort.category_funnel(df)

    styled_cf = cat_df.copy()
    for col in ["view_to_cart", "cart_to_purchase", "view_to_purchase"]:
        styled_cf[col] = styled_cf[col].apply(lambda x: f"{x:.1%}")

    st.dataframe(styled_cf)
    st.subheader("Top 10 Categories by View → Purchase Conversion Rate")
    st.pyplot(charts.plot_category_funnel_bar(cat_df)) # type: ignore

else:
    st.info("Upload a CSV file to start the analysis.")