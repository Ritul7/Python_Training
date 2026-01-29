# DAY-4 Learnings

## 1. SQL vs NoSQL Databases

## 4. Indexing 

- A technique to speed up the data retrieval from the db.
- Index is a seperate data structure(B-Tree), that stores the value of one or more columns and a pointer(reference) to the actual row in the table.'
- DB looks for the index first, if not found then T.C. might go upto 0(n).
- If index found then T.C. reduces to O(logn).

### Use Indexing when
- A column is frequently used in WHERE, GROUP BY, JOIN, ORDER BY
- Cardinality(Number of unique values in a column) is high as it gives better index selectivity, like search space decreases effectively.
- A Table has very large no. of rows

### Don't use Indexing when
- Table has frequent writes as INSERT, UPDATE, DELETE requires heavy operations, because DB must update table + index
- Column has low cardinality (Overhead Increases)
- Small no. of columns, as traversing will be more easy rather than indexing

## 5. Query optimization.
