import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def plot_funnel(funnel):
    stages = ["Viewed", "Cart", "Remove_from_cart", "Purchase"]
    values = [funnel['view'], funnel['cart'], funnel['remove_from_cart'], funnel['purchase']]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(stages, values, color=['skyblue', 'orange', 'lightgreen', 'salmon'])
    ax.set_title("Funnel Counts")

    # Annotate bars with values
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, str(yval), ha='center', va='bottom')
    return fig

def plot_retention_heatmap(retention):
    plt.figure(figsize=(12, 6))
    sns.heatmap(retention, annot=True, fmt=".0%", cmap="Blues")
    plt.title("Cohort Retention Heatmap")
    return plt

def plot_cohort_retention_line(retention):
    plt.figure(figsize=(10, 5))
    for cohort in retention.index:
        plt.plot(retention.columns, retention.loc[cohort], marker='o', label=f'Cohort {cohort}')
    plt.title("Cohort Retention Over Time")
    plt.xlabel("Periods Since Cohort Start (Months)")
    plt.ylabel("Retention Rate")
    plt.grid()
    return plt

def plot_funnel_cohort_heatmap(df):
    plt.figure(figsize=(10, 5))
    sns.heatmap(df.set_index("cohort_month")[["view_to_purchase"]],
                annot=True, fmt=".0%", cmap="Greens")
    plt.title("View → Purchase Conversion by Cohort")
    return plt

def plot_category_funnel_bar(df):
    df = df.sort_values(by="view_to_purchase", ascending=False).head(10)
    df['view_to_purchase'] = round(df['view_to_purchase'] * 100,2)  # Convert to percentage
    df['category_id'] = df['category_id'].astype(str)  # Ensure category_id is string for better display
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, y="view_to_purchase", x="category_id", palette="Purples_r")
    plt.xticks(rotation=90)
    plt.title("Category Conversion Rate (View → Purchase)")
    return plt 

def plot_sankey_funnel(funnel):
    labels = ["Viewed", "Cart", "Remove_from_cart", "Purchase"]
    sources = [0, 1, 1, 2, 0]
    targets = [1, 2, 3, 3, 3]
    values = [
        funnel['view_to_cart'],
        funnel['cart_to_remove_from_cart'],
        funnel['cart_to_purchase'],
        funnel['remove_from_cart_to_purchase'],
        funnel['view_to_purchase']
    ]

    fig = go.Figure(data=[go.Sankey(
        node=dict(pad=20, 
                  thickness=20, 
                  line=dict(color="black", width=0.5), 
                  label=labels,
                  color=["#4C72B0", "#55A868", "#C44E52", "#8172B3"],),
        link=dict(source=sources, 
                  target=targets, 
                  value=values)
    )])

    fig.update_layout(title_text="Funnel Sankey Diagram", font_size=10)
    return fig