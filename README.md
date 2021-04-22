# Atlas Full Text Search Assets & Patterns

For specific instructions on how to run each pattern, click on the relevant label in the table(s) below.

All links are focused on the use of __Atlas Full Text Search__, which showcase the full text search offering.

Be sure to review the [common search gotchyas](context/gotchyas).

## Search Foundations (Review First)

| #  | Label                              | Description                                                                                                                                                                                                                                                                 
|----|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Engine](foundations/engine)            | Review the basic components of a full-text search engine (including tokenization), and build one.
| 2  | [Basic](foundations/basic)            | Run a simple text search.
| 3  | [Fuzzy](foundations/fuzzy)            | Handle common typos
| 4  | [Highlighting](foundations/highlighting)            | Add a relevance score and hit highlights to the results
| 5  | [Autocomplete](foundations/autocomplete)            | Search as you type
| 6  | [Phrase](foundations/phrase)            | Ordered sequence of words
| 7  | [Diacritics](foundations/diacritics)            | Include multiple languages
| 8  | [Compound](foundations/compound)            | Combine two or more operators into a single query (or clause)
| 9  | [Explain](foundations/explain)            | See how the mongot (lucene) returns results to clients.


## Search Patterns & Use Cases

| #  | Label                              | Description                                                                                                                                                                                                                                                                 
|----|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Multi Tenant](patterns/multi-tenant)            | Ability to build search applications that limit what an end user can search for based on their tenancy.                                       
| 2  | [Weighted Fields](patterns/weighted-fields)            | Implement relevance weights where some fields more important than  other fields.   
| 3  | [Advanced Scoring](patterns/advanced-scoring)            |  Ensure the boosted variable doesn’t overwhelm the relevance of our search results.  
| 4  | [Sorting](patterns/sorting)            |  Using the Atlas Search near operator to sort documents based on a numeric, date, or geo field.
| 5  | [Custom Analyzer](patterns/sorting)            | Implement a synonym-based search functionality by leveraging the Custom Analyzers with the mapping character filter.
