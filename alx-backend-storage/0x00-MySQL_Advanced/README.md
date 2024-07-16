# 0x00. MySQL advanced

| `Back-end` | `SQL` | `MySQL` |

## Resources

**Read or watch:**

-   [MySQL cheatsheet](https://intranet.alxswe.com/rltoken/8w9di_hk19DIMSBEV3EayQ)
-   [MySQL Performance: How To Leverage MySQL Database Indexing](https://intranet.alxswe.com/rltoken/2GJbZ48zRPA70o2YhTdH7g)
-   [Stored Procedure](https://intranet.alxswe.com/rltoken/K180X2OCzb6gzPngjn-EIg)
-   [Triggers](https://intranet.alxswe.com/rltoken/cJ1qA4o-rRm4rWIsqYKSZg)
-   [Views](https://intranet.alxswe.com/rltoken/vHg1z3UAOcWMvOt8xZHeiA)
-   [Functions and Operators](https://intranet.alxswe.com/rltoken/g-c1m6iljScpi4LeqxBRqQ)
-   [Trigger Syntax and Examples](https://intranet.alxswe.com/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ)
-   [CREATE TABLE Statement](https://intranet.alxswe.com/rltoken/X789nJ22H6HVh1uCQPl0lg)
-   [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.alxswe.com/rltoken/mfrWMt1KL3NHXblJykMgZg)
-   [CREATE INDEX Statement](https://intranet.alxswe.com/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ)
-   [CREATE VIEW Statement](https://intranet.alxswe.com/rltoken/FEZNlZFKZmD1ISnLINkCwQ)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

-   How to create tables with constraints
-   How to optimize queries by adding indexes
-   What is and how to implement stored procedures and functions in MySQL
-   What is and how to implement views in MySQL
-   What is and how to implement triggers in MySQL

## Tasks

### 0. We are all unique!

Write a SQL script that creates a table `users` following these requirements:

-   With these attributes:

    -   `id`, integer, never null, auto increment and primary key
    -   `email`, string (255 characters), never null and unique
    -   `name`, string (255 characters)

-   If the table already exists, your script should not fail
-   Your script can be executed on any database

**Context:** _Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application_
