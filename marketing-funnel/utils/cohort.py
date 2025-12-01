import pandas as pd

def create_cohort_retention(df):
    df['event_date'] = df['event_time'].dt.date
    df['event_month'] = df['event_time'].dt.to_period('M')

    df = df.sort_values(by=['user_id', 'event_date'])
    first_event = df.groupby('user_id')['event_date'].min().reset_index().rename(columns={'event_date': 'cohort_date'})
    df = df.merge(first_event, on='user_id')

    df['cohort_period'] = (df['event_date'] - df['cohort_date']).apply(lambda x: x.days // 30)  # monthly cohorts

    cohort_data = df.groupby(['cohort_date', 'cohort_period'])['user_id'].nunique().reset_index()
    retention = cohort_data.pivot(index='cohort_date', columns='cohort_period', values='user_id')

    cohort_sizes = retention.iloc[:, 0]
    retention_rate = retention.divide(cohort_sizes, axis=0)

    return retention_rate

def funnel_by_cohort(df):
    df['event_month'] = df['event_time'].dt.to_period('M')
    df['cohort_month'] = df.groupby('user_id')['event_month'].transform('min')

    rows = []

    for cohort, group in df.groupby("cohort_month"):
        v = group[group.event_type == "view"]['user_id'].nunique()
        c = group[group.event_type == "cart"]['user_id'].nunique()
        p = group[group.event_type == "purchase"]['user_id'].nunique()

        rows.append({
            "cohort_month": cohort.strftime("%Y-%m"),
            "view_users": v,
            "cart_users": c,
            "purchase_users": p,
            "view_to_cart": c / v if v else 0,
            "cart_to_purchase": p / c if c else 0,
            "view_to_purchase": p / v if v else 0
        })

    return pd.DataFrame(rows).sort_values("cohort_month")

def category_funnel(df):
    rows = []

    for category, group in df.groupby("category_id"):
        v = group[group.event_type == "view"]['user_id'].nunique()
        c = group[group.event_type == "cart"]['user_id'].nunique()
        p = group[group.event_type == "purchase"]['user_id'].nunique()

        rows.append({
            "category_id": category,
            "view_users": v,
            "cart_users": c,
            "purchase_users": p,
            "view_to_cart": c / v if v else 0,
            "cart_to_purchase": p / c if c else 0,
            "view_to_purchase": p / v if v else 0
        })

    df_out = pd.DataFrame(rows)
    return df_out.sort_values("view_users", ascending=False)