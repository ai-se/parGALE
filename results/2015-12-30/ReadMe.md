## Feature Space Division
- Randomly select **n** * 25 points and construct a decision tree with **n** leaves. **n** represents the number of processor.
- For each leaf identify the range of inputs(decisions).
- For each processor: randomly assign input range of one leaf.
- Decisions will now be generated within only this input range.
- Experiment was conducted 20 times

# Results.
## ERS Feature Model
- 35 Features
- 7 Objectives
- 5184 Solutions

### Runtimes
| Processors |    GALE    | GALE FS | ParGIA |
|:----------:|:-----------:|:-------------:|:----------:|
|1| 250.605 | 250.673.05 |62.12|
|2| 105.10 | 100.86 43 |32.60|
|3| 65.23 | 63.73  |46.70|
|4| 47.88 | 47.53  |29.89|
|5| 37.9 | 37.82 |25.08|
|6| 29.69 | 30.80  |31.36|
|7| 25.03 | 26.33  |29.27|
|8| 22.82 | 24.14  |16.90|
|9| 22.43 | 21.04  |25.53|
|10| 21.95 | 20.265 |19.46|
|11| 21.11 | 17.233 |26.76|
|12| 21.46 | 17.233 |18.45|
|13| 21.12 | 18.318 |17.12|
|14| 20.87| 18.05 |24.06|
|15| 20.45| 18.29 |17.29|
|16| 21.69| 20.02 |14.60|

### Speedups
![speedups](ers_speedups.png)

### BaseLine
![baseline](ERS_baseline.png)

## WPT Feature Model
- 44 Features
- 2,120,800 Solutions
- 4 Objectives

### Runtimes
| Processors |    GALE    | GALE FS | ParGIA |
|:----------:|:-----------:|:-------------:|:----------:|
|1| 269.37 +/- 2.17 | 269.37 +/- 2.17 | 10151.69|
|2| 100.81 +/- 1.72 | 113.03 +/- 1.07 |4299.47|
|3| 65.28 +/- 1.11 | 71.86 +/- 0.91 |11118.42|
|4| 47.61 +/- 1.26 | 53.11 +/- 2.91 |4308.46|
|5| 37.63 +/- 0.47 | 42.17 +/- 1.59 |10606.78|
|6| 30.57 +/- 0.23 | 34.23 +/- 1.76 |4034.11|
|7| 25.96 +/- 0.08 | 29.50 +/- 1.14 |7612.78|
|8| 23.58 +/- 0.32 | 27.22 +/- 2.03 |4077.85|
|9| 23.96 +/- 0.49 | 23.57 +/- 2.03 |6811.58|
|10| 23.99 +/- 0.22 | 22.98 +/- 2.64 |4028.05|
|11| 23.53 +/- 0.34 | 20.66 +/- 0.96 |6566.03|
|12| 23.85 +/- 0.29 | 19.38 +/- 1.93 |3729.90|
|13| 23.91 +/- 0.16 | 20.54 +/- 1.59 |4949.09|
|14| 23.56 +/- 0.28 | 20.49 +/- 2.53 |3497.46|
|15| 23.39 +/- 0.08 | 20.59 +/- 0.95 |4536.61|
|16| 24.94 +/- 0.26 | 22.64 +/- 3.44 |3191.49|

### Speedups
![speedups](wpt_speedups.png)

### BaseLine
![baseline](WPT_baseline.png)
