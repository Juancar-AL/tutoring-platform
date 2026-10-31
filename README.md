# Tutoring Platform

A scheduling and management platform for private tutors and their students.
Tutors publish their availability, students book lessons, and both keep track
of sessions and payments in one place.

> **Status:** early development. Backend in progress — not usable yet.

## Why

I've been tutoring one-to-one for 3+ years and manage everything with chats,
calendars and spreadsheets. This project is the tool I wish I had: built for
my own classes first, designed to become a multi-tenant SaaS later.

## Features

MVP scope (planned):

- [ ] Accounts for tutors and students (role-based access)
- [ ] Open student sign-up with a tutor invite code
- [ ] Tutor availability slots
- [ ] Student lesson booking
- [ ] Per-student pricing and payment tracking
- [ ] Monthly summary per student

Later:

- [ ] AI-generated worksheets tailored to each student's level

## Tech stack

| Layer          | Tools                                              |
|----------------|----------------------------------------------------|
| Language       | Java 25                                            |
| Framework      | Spring Boot 4.1 (Spring Framework 7)               |
| Build          | Gradle 9 (Kotlin DSL)                              |
| Persistence    | Spring Data JPA, Hibernate 7, PostgreSQL, Flyway   |
| Security       | Spring Security 7, JWT                             |
| Testing        | JUnit 5, Testcontainers                            |
| Infrastructure | Docker, GitHub Actions                             |

## Domain model

```
User (role: teacher | student)
 ├── TeacherProfile (invite_code, accepting_students)
 │     └── Availability ──┐
 └── StudentProfile (teacher_id, school_level, default_price)
                          └── Booking
```

Each student belongs to exactly one tutor; every query is scoped by tutor
(multi-tenant by design).

## Getting started

> Setup instructions will be added once the Spring Boot project is created.

## Documentation

- [Software Requirements Specification](docs/srs.md)

## Roadmap

1. Core models, database and migrations
2. Authentication and tutor-scoped access
3. Availability and booking
4. Payments, Docker and deployment
5. Minimal frontend
6. AI worksheets and beta with real tutors

## License

[MIT](LICENSE) © 2026 J.C. Alonso
