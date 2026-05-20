# Assignment-Tracking-System-

### Introduction

The Assignment Tracking System is a web-based application designed to help students manage their academic workload efficiently. The system provides a simple and focused platform for tracking assignments, setting deadlines, and receiving timely reminders.
Unlike complex Learning Management Systems (LMS) such as Blackboard, this system focuses specifically on personal task management to improve productivity and reduce missed deadlines.

### Objective 

* To provide a simple interface for managing assignments.
* To reduce missed deadlines through automated reminders.
* To improve student time management and productivity.

## Assignment 4 Documentation

- [Stakeholder Analysis](STAKEHOLDER_ANALYSIS.md)
- [System Requirements](SYSTEM_REQUIREMENTS.md)
- [Reflection](REFLECTION.md)

## Assignment 5 Documentation

- [Use Case Diagram](USE_CASE_DIAGRAM.md)
- [Use Case Specifications](USE_CASE_SPECIFICATIONS.md)
- [Test Cases](TEST_CASES.md)
- [Reflection](REFLECTION_A5.md)

- ## Assignment 7 Documentation

- [Template Analysis](TAMPLATE_ANALYSIS.md)
- [Kanban Explanation](KANBAN_EXPLANATION.md)
- [Reflection](REFLECTION.md)

-  ## Assignment 8 Documentation

- [State Diagrams](STATE_DIAGRAMS.md)
- [Activity Diagrams](ACTIVITY_DIAGRAMS.md)
- [Reflection](a8_REFLECTION.md)

- ## Assignment 9 Documentation

- [Sequence Diagrams](SEQUENCE_DIAGRAMS.md)
- [Class Diagram](CLASS_DIAGRAM.md)
- [Reflection](A9_REFLECTION.md)

## Assignment 10

## Overview

This assignment focused on implementing the Assignment Tracking System using Python and applying creational design patterns.

## Source Code Structure

| Folder               | Purpose                    |
|--------------------- |--------------------------- |
| /src                 | Core system classes        |
| /creational_patterns | Creational design patterns |
| /tests               | Unit testing               |



## Design Choices

Python was selected because it is simple, readable, and suitable for object-oriented programming.

The system was structured into separate folders to improve maintainability and organization.

## Creational Pattern Rationales

| Pattern                   | Purpose                         |
|---------------------------|---------------------------------|
| Simple Factory            | Creates assignment types        |
| Factory Method            | Handles notification creation   |
| Abstract Factory          | Creates dashboard interfaces    |
| Builder                   | Builds assignments step-by-step |
| Prototype                 | Clones assignment templates     |
| Singleton                 | Ensures one database connection |


## Testing

Unit tests were implemented to validate:
- Assignment creation
- Singleton behavior
- Prototype cloning

## GitHub Management

GitHub Issues and milestones were used to track implementation progress and manage tasks throughout development.


## Assignment 11 – Repository Layer

## Overview

This assignment focused on implementing a repository layer for the Assignment Tracking System.
The repository layer separates storage logic from business logic, making the system easier to maintain, test, and extend.

## Repository Design

A generic repository interface was implemented to standardize CRUD operations across repositories.

### CRUD Operations
- Save
- Find By ID
- Find All
- Delete

Generics/interfaces were used to reduce duplication and improve scalability.

## In-Memory Storage

The first implementation uses in-memory dictionary storage.

Benefits:
- Fast testing
- No database dependency
- Simple implementation

## Storage Abstraction

The Factory Pattern was used to abstract storage creation.

This allows future switching between:
- In-memory storage
- Database storage
- File storage
- External APIs

without changing business logic.

## Future-Proofing

A stub DatabaseAssignmentRepository was added to demonstrate future database integration support.

## Testing

Unit tests were implemented for:
- Save operations
- Find operations
- Delete operations


# Assignment 12 – Service Layer and REST API

## Overview
This assignment implemented a service layer and REST API using FastAPI.

## Services
- UserService
- AssignmentService
- ReminderService

## API
Endpoints:
- GET /api/users
- POST /api/users
- GET /api/assignments
- GET /api/reminders

## Documentation
OpenAPI documentation added under /docs.
