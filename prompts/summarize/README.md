# Summarize
This is a type of chain to distill large amounts of information into a small amount.

There are three types of summarize chains:
1. Stuff: This is a simple chain to stuff all the text from each document into one propmt. This is limited by token window so this approach only works for smaller amounts of data.
2. Map Reduce: This maps a summarize prompt onto each data chunk and then combines all the outputs to finally reduce using a summarization prompt.
3. Refine: This iteratively passes in each chunk of data and update a continously update an evolving summary to be more accurate based on the new chunk of data given.

## Usage