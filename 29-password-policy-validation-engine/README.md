# Case Study 29: Password Policy Validation Engine

## Problem statement
Check a sample password and explain every failed rule.

## Objectives
Use strings, loops, membership, and flags.

## Assumptions
At least 8 chars; uppercase, lowercase, digit, allowed symbol !@#$%&; no spaces or adjacent repeated chars.

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
| Normal sample | Study#2026 passes all rules. |
| Boundary case | short fails several rules. |
| Invalid or exceptional case | Study##2026 fails adjacent-repeat rule. |

## Output screenshot
See output_screenshot.png; captured text is in sample_output.txt.

## Conclusion
The program applies the assumptions to its sample data and reports results. Compare the assumptions with the faculty's exact rules before submission.
