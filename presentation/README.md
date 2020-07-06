# Presentation
Code snips and graphics for presentation

## Project Ideas
- Use the AST to compute and dynamically create the CFG and compute the various graph metrics.
- Understand the correspondence between paths in the CFG with sets of rays.  I believe there is a paper of Drumm which classifies these rays.
- The existing tests provide 100% branch coverage, but only 33% path coverage.  Can we use the correspondence with classification of rays to generate tests cases sufficient to obtain 100% path coverage?
- Even with 100% path coverage, there may be other "interesting" tests, corresponding to rays on boundaries between regions.  Testers often have an intution for these corner cases and create so called _boundary values tests_ for these.  How could we formally define the boundary value tests?  Could we quantify how many boundary value tests would be needed?
