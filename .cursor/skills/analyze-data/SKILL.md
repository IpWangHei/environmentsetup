---
name: analyze-data
description: Inspect and analyze a small tabular dataset carefully and reproducibly. Use this skill when working with CSV or other simple tabular data and the goal is to understand the dataset, check data quality, compute descriptive statistics, or extend an existing analysis.
disable-model-invocation: true
---

Analyze Data

Use this workflow when analyzing a tabular dataset.

The goal is not simply to produce numbers. First understand the data, then check its quality, then perform the analysis in a way that can be reproduced and verified.

1. Inspect Before Analyzing

Before making any changes:

1. Locate the relevant data file.
2. Inspect the column names.
3. Identify what each column appears to represent.
4. Determine the number of observations.
5. Inspect a small sample of rows.
6. Identify the apparent data types of the columns.

Do not modify any files at this stage.

2. Check Data Quality

Check for obvious data-quality problems, including:

* missing values;
* duplicate observations;
* values with unexpected types;
* clearly unusual or suspicious values;
* inconsistent formatting.

Do not silently fix these problems.

If you find a potential problem, report it before deciding whether any correction is appropriate.

3. Produce Descriptive Statistics

For relevant numerical variables, consider reporting:

* count;
* mean;
* median;
* minimum;
* maximum.

Only report statistics that are meaningful for the variable.

Do not calculate statistics merely because they are available.

For non-numerical variables, briefly describe the categories or other useful characteristics when relevant.

4. Understand the Existing Project

If the repository already contains analysis code:

1. Inspect the existing code before editing it.
2. Understand what the current program does.
3. Follow the existing project structure and coding style.
4. Prefer modifying the existing analysis rather than creating unnecessary new files.
5. Avoid introducing new dependencies unless they are genuinely needed.

Before changing any code, briefly explain:

* what you intend to change;
* which file or files you expect to modify;
* why the change is useful.

5. Make Small, Reproducible Changes

If the user asks you to modify the analysis:

* make the smallest reasonable change;
* keep the analysis reproducible;
* do not modify the original raw data;
* do not hard-code results that should be calculated from the data;
* preserve existing useful behavior unless the task requires otherwise;
* avoid unnecessary refactoring.

Prefer simple, readable code over clever or unnecessarily complex code.

6. Verify the Analysis

After changing code:

1. Run the relevant program.
2. Check that it completes without errors.
3. Inspect the output.
4. Confirm that the new results are actually calculated from the data.
5. Check that existing functionality still works.

If something cannot be verified, clearly say so.

Do not claim that the analysis works unless you have actually checked it.

7. Report What You Found

When reporting the analysis, use the following structure where appropriate:

Dataset

Briefly state:

* number of observations;
* important columns;
* any important data-quality issues.

Results

Report the main descriptive results clearly.

Interpretation

Explain in plain language what the results show.

Do not overstate what can be concluded from simple descriptive statistics.

Changes Made

If files were modified, state:

* which files changed;
* what was changed;
* how the change was verified.

Important Rules

Always follow these rules:

1. Never modify the original raw dataset unless the user explicitly asks for it.
2. Never invent missing values or results.
3. Inspect the data before analyzing it.
4. Inspect existing code before changing it.
5. Explain the plan before editing code.
6. Prefer the smallest reasonable code change.
7. Run and verify code after editing it.
8. Clearly distinguish observed results from interpretation.
9. Do not claim verification that you did not perform.