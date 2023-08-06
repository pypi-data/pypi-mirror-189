import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/home/willie/projects/dbz/test-data/2023-02-nsrl/power-supply/2023-02-03T11-47-47.706817.csv"
)
df["Datestamp"] = pd.to_datetime(df["Datestamp"], format="%Y-%m-%dT%H-%M-%S.%f")
print(df)
dfs = {
    i: df.filter(like=i) for i in df.columns.str.split(" ").str[-1] if i != "Datestamp"
}

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
axes[-1].set_xlabel("Time (s)")
cnt = 0
for title, d in dfs.items():
    d.rename(
        columns=lambda x: x[8:-8] if x != "Datestamp" and len(x) > 16 else x,
        inplace=True,
    )
    d["Datestamp"] = df["Datestamp"]
    ax = d.plot(x="Datestamp", ax=axes[cnt])
    ax.set_ylabel(title)
    cnt += 1

plt.tight_layout()
plt.show()
