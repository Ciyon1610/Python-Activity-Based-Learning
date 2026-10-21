# Case Study 37: Nested Loop Calendar Generator

## Problem statement
Print a month from its first weekday and length.

## Objectives
Use nested loops for week rows and weekday columns.

## Assumptions
Weekday 0=Sunday..6=Saturday; days 28..31; leap year is out of scope.

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
| Normal sample | 3,30 places day 1 under Wednesday and ends at day 30. |
| Boundary case | 0,28 starts Sunday. |
| Invalid or exceptional case | Weekday 7 is rejected. |

## Output screenshot
See output_screenshot.png; captured text is in sample_output.txt.

## Conclusion
The program applies the assumptions to its sample data and reports results. Compare the assumptions with the faculty's exact rules before submission.
