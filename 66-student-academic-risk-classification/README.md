# Case Study 66: Student Academic Risk Classification

## Problem statement
Combine marks, attendance, and lab scores to classify risk with reasons.

## Objectives
Use parallel lists and nested marks lists.

## Assumptions
Flags: average <50, attendance <75, lab <40; zero=Low, one=Moderate, two or more=High.

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
| Normal sample | Asha is Low risk with no flags. |
| Boundary case | Bala is High risk with all three flags. |
| Invalid or exceptional case | Summary counts are displayed. |

## Output screenshot
See output_screenshot.png; captured text is in sample_output.txt.

## Conclusion
The program applies the assumptions to its sample data and reports results. Compare the assumptions with the faculty's exact rules before submission.
