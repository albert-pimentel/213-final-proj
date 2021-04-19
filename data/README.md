<h1> Description of data </h1>

<h2> raw-data-with-profileIDs-no-essays: </h2>
This is the data that should be input into Mechanical Turk -- it is the original dataset with essays removed and profile IDs added.

<h2> QC_Sample_Input: </h2>
This should be approximately what our MTurk data looks like, and therefore what the input to our QC module looks like. Note that the Qualified_worker column is empty.

<h2> QC_Sample_Output_(AggregationInput): </h2>
This should be approximately what the output of our QC module looks like, and therefore what the input to our Aggregation module looks like. Note that the Qualified_worker column is filled, indicating that we have used quality control to classify workers as qualified or unqualified.

<h2> Aggregation_Output: </h2>
This is what the output of our Aggregation module looks like. It is essentially the QC_Sample_Output with quality control columns removed and only rows by qualified workers kept.
