# Case Study 1: University Scholarship Allocation

## Problem statement
Screen and rank applicants using marks, attendance, and income.

## Objectives
Use tuples, multiple eligibility conditions, failed-reason lists, and ranking.

## Assumptions
Assume aggregate>=75, subject minimum>=60, attendance>=75, income<=300000; ties use attendance then lower income.

## Algorithm
1. Read or load the case data
2. Apply the stated rules and calculations
3. Process records with loops and conditions
4. Display results and summary

## Flowchart
See flowchart.svg.

## Pseudocode
START
  READ or LOAD the required data
  FOR each relevant record
    APPLY the stated conditions and calculations
    STORE or DISPLAY results
  END FOR
  DISPLAY summary
END

## Python source code
See source.py. The implementation uses the listed introductory syllabus topics.

## Test cases
| Input or condition | Expected result |
|---|---|
| Normal sample | Asha is eligible and ranks first. |
| Boundary case | Charan is rejected for income. |
| Invalid or exceptional case | Applicants below any threshold are rejected with reasons. |

## Output screenshot
See output_screenshot.png; captured text is in sample_output.txt.

## Conclusion
The program applies the assumptions to its sample data and reports results. Compare the assumptions with the faculty's exact rules before submission.
