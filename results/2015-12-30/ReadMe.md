## Feature Space Division
- Randomly select **n** * 25 points and construct a decision tree with **n** leaves. **n** represents the number of processor.
- For each leaf identify the range inputs within the range.
- For each processor: randomly assign input range of one leaf.
- Decisions will now be generated within only this input range.

# Results.
## ERS Feature Model

## Runtimes

| Processors |    Naive    | Feature Split |
|------------|-------------|---------------|
|1| 250.67 +/- 23.05 | 250.67 +/- 23.05 | 
|2| 105.15 +/- 4.60 | 100.86 +/- 1.43 |
|3| 65.23 +/- 3.17 | 63.73 +/- 1.24 |
|4| 47.88 +/- 0.67 | 47.53 +/- 0.68 |
|5| 37.9 +/- 0.43 | 37.82 +/- 0.94 |
|6| 29.69 +/- 0.07 | 30.80 +/- 1.41 |
|7| 25.03 +/- 0.15 | 26.33 +/- 1.29 |
|8| 22.82 +/- 0.38 | 24.14 +/- 1.52 |
|9| 22.43 +/- 0.59 | 21.04 +/- 1.29 |
|10| 21.92 +/- 0.65 | 20.26 +/- 1.15 | 
|11| 21.12 +/- 0.61 | 17.23 +/- 0.73 |
|12| 21.47 +/- 0.26 | 17.23 +/- 0.73 |
|13| 21.15 +/- 0.42 | 18.31 +/- 1.18 |
|14| 20.87 +/- 0.51 | 18.05 +/- 1.72 |
|15| 20.45 +/- 0.74 | 18.29 +/- 1.65 |
|16| 21.69 +/- 0.63 | 20.02 +/- 2.75 |
