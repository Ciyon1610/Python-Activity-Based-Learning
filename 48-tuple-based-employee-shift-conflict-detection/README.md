# Case Study 48: Tuple-Based Employee Shift Conflict Detection

## Problem statement
Detect overlapping shifts for the same employee.

## Objectives
Compare tuple pairs using interval inequalities.

## Assumptions
Times are minutes after midnight; endpoint-touching shifts do not overlap.

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
| Normal sample | Asha 540-720 overlaps 690-810. |
| Boundary case | 690-810 and 810-900 only touch, so no conflict. |
| Invalid or exceptional case | Different employees are not compared as conflicts. |

## Output screenshot
See output_screenshot.png; captured text is in sample_output.txt.

## Conclusion
The program applies the assumptions to its sample data and reports results. Compare the assumptions with the faculty's exact rules before submission.
