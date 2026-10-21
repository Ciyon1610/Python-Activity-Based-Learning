# Case Study 47: Sports Tournament Ranking System

## Problem statement
Rank teams by points and tie-break rules.

## Objectives
Use tuples and nested-loop sorting.

## Assumptions
Win=3, draw=1; tie-break by goal difference, goals scored, then name.

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
| Normal sample | Wolves ranks before Falcons on goals scored. |
| Boundary case | Falcons rank before Tigers on goal difference. |
| Invalid or exceptional case | Eagles rank below teams with 7 points. |

## Output screenshot
See output_screenshot.png; captured text is in sample_output.txt.

## Conclusion
The program applies the assumptions to its sample data and reports results. Compare the assumptions with the faculty's exact rules before submission.
