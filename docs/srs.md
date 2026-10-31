# Software Requirements Specification · Tutoring Platform

> Structure: ISO/IEC/IEEE 29148 (SRS, based on IEEE 830-1998).
> Status: draft · Version 0.1 · Author: J.C. Alonso

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements of Grulla, version 1 (MVP). It is
written for the developer, future contributors and reviewers of the project.
It is the reference for design, implementation and testing.

### 1.2 Scope
**Grulla** is a mobile-first platform that simplifies how private tutors manage
their lessons. Tutors stop acting as administrators: scheduling, cancellations
and payment tracking happen in the app instead of in endless WhatsApp messages.
Students (or their guardians) see the schedule, book free slots and cancel on
their own, which gives tutors more time to prepare better lessons.

Objectives:
- Remove the manual messaging a tutor does today to schedule, cancel and ask for payments.
- Let students and guardians manage lessons without depending on the tutor.
- Give the tutor a clear view of lessons given and payments pending.

#### MVP: in scope
- Tutor account with an invite code to share with students.
- Student registration with the tutor's invite code, including guardian data
  and consent for minors (see §2.4).
- Tutor weekly availability.
- Recurring lessons scheduled by the tutor (same day and time every week).
- One-off lessons booked by the student in a free slot, choosing one of the
  durations allowed by the tutor (1 h to 2 h, in 30-minute steps).
- Moving an occurrence of a recurring lesson to a free slot, without approval.
- Student cancellation up to 2 hours before the lesson; later cancellations are charged.
- Tutor cancellation or rescheduling up to 3 hours before the lesson.
- In-person (with address) or online (with meeting link) modality per lesson.
- Email notifications of bookings, changes and cancellations (D-05).
- Lesson notes written by the tutor.
- Blocked periods (holidays) that cancel recurring lessons without charge.
- Spanish and English user interface.
- Payment tracking: hourly price per student, monthly summary for recurring
  lessons and per-lesson charge for one-off lessons; the tutor marks payments
  as received.

#### MVP: out of scope
- In-app payments with Stripe.
- Google Calendar sync and WhatsApp notifications (WhatsApp Business API).
- Video calls (online lessons use the tutor's own tool; only the link is stored).
- Per-student calendar view for the tutor.
- AI-generated worksheets.
- Students with more than one tutor.
- Public directory or marketplace of tutors.

### 1.3 Definitions, acronyms and abbreviations
| Term | Definition |
| --- | --- |
| Tutor | Teacher who gives private lessons and owns a Grulla account |
| Student | Person who receives lessons; belongs to exactly one tutor |
| Guardian | Parent or legal guardian of a minor student; pays for the lessons |
| Invite code | Code that identifies a tutor and is required to register as a student |
| Availability | Weekly time windows in which a tutor accepts lessons |
| Free slot | Part of the availability not taken by any lesson |
| Recurring lesson | Lesson repeated every week at the same day and time, set by the tutor |
| One-off lesson | Single lesson booked by the student in a free slot |
| Occurrence | A single date of a recurring lesson |
| Late cancellation | Cancellation less than 2 hours before the lesson; it is charged |
| MVP | Minimum Viable Product: first version that already gives real value |

### 1.4 References
- ISO/IEC/IEEE 29148:2018 — Requirements engineering
- IEEE Std 830-1998 — Recommended practice for SRS
- Regulation (EU) 2016/679 (GDPR) and Spanish Organic Law 3/2018 (LOPDGDD)

### 1.5 Overview
Section 2 describes the product context. Section 3 lists the specific
requirements. Section 4 describes how they will be verified.

## 2. Overall description

### 2.1 Product perspective
Grulla is a standalone system: a backend API plus a native mobile app
(decision D-01). It replaces the tutor's current workflow (WhatsApp, calendar
and manual payment tracking). Its only external dependency in the MVP is an
email delivery service for notifications. It requires an internet connection.

### 2.2 Product functions
| Epic | Functions |
| --- | --- |
| Accounts | Tutor sign-up, student sign-up with invite code, guardian data, login |
| Availability | Tutor defines weekly availability |
| Scheduling | Recurring lessons, one-off bookings, moving occurrences, cancellations |
| Notifications | Email notifications of bookings, changes and cancellations |
| Lessons | Lesson notes, blocked periods |
| Payments | Monthly and per-lesson payment tracking, late-cancellation charges |

### 2.3 User characteristics
**Tutor.** Teaches one-to-one, from primary school to adult learners. Uses the
phone constantly, but has little time for administration. Wants to stop
messaging parents about schedules and payments.

**Student.** Any age from primary school to adulthood. Students aged 16 or over
use the app on their own. For younger students the guardian operates the
account and signs in with the guardian's email (D-02, D-03).

**Guardian.** Parent of a student under 16. Pays for the lessons and may
manage the schedule. Has no account of their own in the MVP: the student's
account is operated by the student or by the guardian (decision D-02).

### 2.4 Constraints
- **Legal:** GDPR and LOPDGDD. In Spain a minor under 14 cannot consent to the
  processing of their personal data. By product policy, Grulla requires
  guardian data and consent for every student under 16 (decision D-03).
- **Organizational:** one developer, about 10 hours per week, budget close to 0 €.
- **Technical:** backend in Java with Spring Boot; native mobile client.
- **Privacy:** only the data in §3.6.1 is collected (data minimisation).

### 2.5 Assumptions and dependencies
- Users have a smartphone with internet access.
- Expected load in the first year: about 10 tutors and their students.
- The tutor shares the invite code outside the app (in person or by message).
- The tutor and students agree on the video call tool for online lessons.

### 2.6 Apportioning of requirements (future requirements)
- In-app payments with Stripe, paid by the guardian.
- Google Calendar sync and WhatsApp notifications.
- Guardian accounts managing several children.
- Per-student calendar view for the tutor.
- AI-generated worksheets.

### Decisions
| ID | Decision | Rationale |
| --- | --- | --- |
| D-01 | Native mobile app | Owner's choice. Risk: higher effort than a responsive web app |
| D-02 | One account per student, operated by the student or the guardian | Keeps 1 student : 1 tutor and avoids a guardian account in the MVP |
| D-03 | Guardian data and consent required under 16; the guardian's email is the login | Product policy, stricter than the legal minimum of 14 |
| D-04 | Late cancellations of recurring lessons are not deducted from the monthly charge | Same rule as one-off lessons: a late cancellation is paid |
| D-05 | Email notifications in the MVP; WhatsApp later | WhatsApp Business API needs business verification, approved templates and per-conversation fees |
| D-06 | One-off lessons are booked at least 24 h in advance | Gives the tutor time to prepare |
| D-07 | The tutor can cancel or move a lesson up to 3 h before it starts | E.g. a 19:00 lesson can be changed until 16:00 |
| D-08 | A 30-minute buffer applies between all lessons | Travel and preparation time |

### Open issues
| ID | Question | Status |
| --- | --- | --- |
| OI-09 | Legal retention period for payment records after a student leaves | Open: confirm with an official source |
| OI-10 | Native platforms: Android, iOS or both? | Open |

## 3. Specific requirements

### 3.1 External interfaces
#### 3.1.1 User interfaces
- Native mobile app (platforms: OI-10), in Spanish and English.
- Two roles with different home screens: tutor and student.

#### 3.1.2 Software interfaces
- REST API over HTTPS between the app and the backend (JSON).
- Email delivery service (SMTP or a transactional email provider) for notifications.

### 3.2 Functional requirements

Priority uses MoSCoW: **M** must, **S** should, **C** could, **W** won't (this version).
"Student" means the student or the guardian operating the student's account (D-02).

#### Epic E1 · Accounts
| ID | User story | Acceptance criteria | Pri. |
| --- | --- | --- | --- |
| US-01 | As a tutor I want to sign up so that I can manage my lessons | Account created with email and password; an invite code is generated | M |
| US-02 | As a student I want to sign up with my tutor's invite code so that I can book lessons | Invalid code rejects the sign-up; under 16, guardian name, contact and consent are required | M |
| US-03 | As a user I want to log in so that I can access my data | Wrong credentials are rejected; each user only sees their own tutor's data | M |
| US-04 | As a tutor I want to set an hourly price per student so that charges are calculated | Price greater than 0 €; used for every charge of that student | M |
| US-05 | As a tutor I want to regenerate my invite code or stop accepting students so that I control who joins | Old code stops working; closed sign-ups reject valid codes | S |
| US-06 | As a tutor I want to remove a student so that they lose access | Removed student cannot log in; past lessons and payments are kept | S |

#### Epic E2 · Availability
| ID | User story | Acceptance criteria | Pri. |
| --- | --- | --- | --- |
| US-07 | As a tutor I want to define my weekly availability so that students only book when I can teach | Time windows per weekday; changes do not affect already booked lessons | M |
| US-08 | As a tutor I want to choose the lesson durations I offer so that students pick one of them | Options between 1 h and 2 h in 30-minute steps | M |

#### Epic E3 · Scheduling
| ID | User story | Acceptance criteria | Pri. |
| --- | --- | --- | --- |
| US-09 | As a tutor I want to create a recurring lesson for a student so that we keep a weekly schedule | Weekday, start time, duration, modality; occurrences generated every week | M |
| US-10 | As a student I want to see my tutor's free slots so that I know when I can book | Slots respect availability, existing lessons and the 30-minute buffer | M |
| US-11 | As a student I want to book a one-off lesson so that I get extra classes when I need them | Allowed duration only; at least 24 h in advance (D-06); slot no longer free afterwards | M |
| US-12 | As a student I want to move one occurrence of my recurring lesson so that I can adapt to my week | Moved directly if the target slot is free; other occurrences unchanged | M |
| US-13 | As a student I want to cancel a lesson so that I don't waste my tutor's time | Up to 2 h before: not charged; later: marked as charged | M |
| US-14 | As a tutor I want to cancel or move a lesson so that I can handle my own changes | Allowed up to 3 h before (D-07); never charged to the student | M |
| US-15 | As a user I want to see my upcoming lessons so that I know what's next | Ordered by date; shows time, duration, modality and place or link | M |
| US-16 | As a tutor I want to add an address or meeting link to a lesson so that the student knows where to go | Address for in-person, link for online | S |
| US-24 | As a tutor I want to write notes for each lesson so that I remember what we covered | Free text per lesson; only the tutor can see it | S |
| US-25 | As a tutor I want to block periods (holidays) so that no lessons happen then | Recurring occurrences in the period are cancelled and not charged; no bookings allowed | M |

#### Epic E4 · Notifications
| ID | User story | Acceptance criteria | Pri. |
| --- | --- | --- | --- |
| US-17 | As a user I want to be notified when a lesson is booked, moved or cancelled so that nobody has to send messages | The other party receives an email within 1 minute | M |
| US-18 | As a student I want a reminder before each lesson so that I don't forget it | Sent 24 h before | S |
| US-19 | As a tutor I want automatic payment reminders so that I don't have to ask for money | Sent when a charge is pending at the end of the billing period | C |

#### Epic E5 · Payments
| ID | User story | Acceptance criteria | Pri. |
| --- | --- | --- | --- |
| US-20 | As a tutor I want a monthly summary per student so that I know what each one owes | Hours given, amount and status (pending / paid) per student and month | M |
| US-21 | As a tutor I want to mark a charge as paid so that the summary stays up to date | Status changes to paid with the date | M |
| US-22 | As a student I want to see what I owe so that I can pay on time | Same data as US-20, only for my account | S |
| US-23 | As a guardian I want to pay in the app with Stripe so that payments are automatic | — | W |

#### Billing rules
- BR-01: charge = hours × the student's hourly price.
- BR-02: recurring lessons are charged monthly; one-off lessons are charged per lesson.
- BR-03: lessons cancelled by the student up to 2 h before, lessons cancelled by the tutor and occurrences in blocked periods are not charged.
- BR-04: late cancellations by the student are charged in full (D-04).

#### Scenarios of core stories
**US-02 · Sign-up with invite code**
- *Given* a valid invite code, *when* a 15-year-old signs up without guardian data, *then* the sign-up is rejected and guardian data is requested.
- *Given* an invalid or regenerated code, *when* someone signs up, *then* the sign-up is rejected.

**US-11 · Book a one-off lesson**
- *Given* a free slot from 17:00 to 19:00, *when* the student books 1.5 h at 17:00, *then* the lesson is created and the slot is no longer free.
- *Given* a lesson ending at 17:00, *when* the student tries to book at 17:15, *then* the booking is rejected because of the 30-minute buffer.

**US-12 · Move a recurring occurrence**
- *Given* a recurring lesson on Mondays at 18:00, *when* the student moves next Monday's occurrence to a free slot on Tuesday, *then* only that occurrence changes.

**US-13 · Cancel a lesson**
- *Given* a lesson at 18:00, *when* the student cancels at 15:00, *then* it is not charged.
- *Given* a lesson at 18:00, *when* the student cancels at 16:30, *then* it is marked as charged.

**US-20 · Monthly summary**
- *Given* 4 recurring lessons of 1 h at 15 €/h, one cancelled late, *when* the tutor opens the month, *then* it shows 4 h, 60 € and status pending.

#### 3.2.1 Use cases
<!-- TBD: diagram (docs/use-cases.png) + event flows of core use cases (UC-xx) -->

### 3.3 Performance requirements
| ID | Requirement | Verification |
| --- | --- | --- |
| NFR-01 | 95 % of API requests answer in under 500 ms with 10 tutors and their students | Load test |
| NFR-02 | Notification emails are sent within 1 minute of the event | Integration test |

### 3.4 Domain model
Conceptual model (no technical types or ids). Diagram: `docs/domain-model.png` (to be drawn in RSAD).

| Concept | Main attributes |
| --- | --- |
| Tutor | name, email, invite code, accepting students, lesson durations offered |
| Student | name, school year, hourly price |
| Guardian | first name, last name, email, phone, consent date |
| Availability window | weekday, start time, end time |
| Blocked period | start date, end date |
| Recurring lesson | weekday, start time, duration, modality, place or link |
| Lesson | date, start time, duration, modality, place or link, status, notes |
| Charge | billing period, hours, amount, status, paid date |

| Association | Multiplicity |
| --- | --- |
| Tutor teaches Student | 1 — 0..* |
| Student has Guardian | 1 — 0..1 (exactly 1 if under 16) |
| Tutor defines Availability window | 1 — 0..* |
| Tutor defines Blocked period | 1 — 0..* |
| Student attends Recurring lesson | 1 — 0..* |
| Recurring lesson generates Lesson (occurrence) | 0..1 — 0..* |
| Student attends Lesson | 1 — 0..* |
| Charge covers Lesson | 0..1 — 1..* |

**Invariants**
- INV-01: a student belongs to exactly one tutor.
- INV-02: two lessons of the same tutor never overlap, including the 30-minute buffer (D-08).
- INV-03: every lesson lies inside the tutor's availability and outside blocked periods.
- INV-04: every lesson duration is one of the durations offered by the tutor (1 h to 2 h, 30-minute steps).
- INV-05: a one-off lesson is created at least 24 h before it starts (D-06).
- INV-06: a student under 16 has a guardian with recorded consent (D-03).
- INV-07: a student's hourly price is greater than 0 €.
- INV-08: a charge is marked as paid only together with its paid date.
- INV-09: a lesson is counted in at most one charge.

### 3.5 Design constraints
- Backend: Java 25, Spring Boot 4.1, Gradle (Kotlin DSL), Spring Data JPA (Hibernate 7), Flyway, PostgreSQL in production.
- Client: native mobile app (technology to be decided in M7).
- Budget close to 0 €: free tiers of hosting and email services.

### 3.6 Software system attributes
#### 3.6.1 Security and privacy
| ID | Requirement |
| --- | --- |
| NFR-03 | Passwords are stored as a salted hash, never in plain text |
| NFR-04 | All traffic uses HTTPS |
| NFR-05 | A user can never read or change data of another tutor (tenant isolation) |
| NFR-06 | Only this personal data is stored: student name and school year; guardian first name, last name, email and phone; tutor name and email |
| NFR-07 | When a student leaves or asks for deletion, their personal data is deleted or anonymised; payment records are kept only for the legal retention period (OI-09) |
| NFR-08 | Guardian consent is recorded with its date |

#### 3.6.2 Reliability and availability
| ID | Requirement |
| --- | --- |
| NFR-09 | The app requires an internet connection; without it, it shows a clear error and loses no data |
| NFR-10 | The database is backed up at least once a day |

#### 3.6.3 Maintainability
| ID | Requirement |
| --- | --- |
| NFR-11 | Backend test coverage of at least 80 % |
| NFR-12 | Code passes the formatter check (Spotless) and the CI pipeline on every push |

#### 3.6.4 Portability and localisation
| ID | Requirement |
| --- | --- |
| NFR-13 | The interface is available in Spanish and English; all texts are externalised, none hard-coded |

#### Definition of Done
A user story is done when: its acceptance criteria and scenarios pass as automated tests, the formatter check passes, CI is green, related NFRs are respected and the change has been reviewed.

## 4. Verification
<!-- TBD: verification method per requirement, quality checklist, traceability matrix -->

## Annex A. Feasibility study
Market check done on 2026-10-30. Prices as published at that date.

| Alternative | Type | Price | Strengths | Gaps for a solo Spanish tutor |
| --- | --- | --- | --- | --- |
| WhatsApp + calendar + spreadsheet | Status quo | Free | Everyone already uses it | All manual: the problem Grulla solves |
| TutorBird | Tutor management SaaS | From 16.95 US$/month | Scheduling, invoicing, payments, lesson notes, reminders | English-first; paid; generic rules |
| Teachworks | Tutoring business SaaS | From 16.49 US$/month | Complete business management | Aimed at tutoring companies more than solo tutors |
| EasyWeek | Booking SaaS | Free plan available | Booking page, reminders incl. WhatsApp | Generic booking tool, not tutoring-specific |
| 7DaysTutor | Mobile app for tutors | Free with in-app purchases | Lesson diary, attendance, payments; Spanish | Tutor-only: students and guardians do not book |
| Tusclases, GoStudent | Marketplaces | Commission / packs | Find students | Different product: discovery, not management |

**Conclusion.** The problem is real and already solved by mature, cheap tools,
so Grulla cannot compete on features alone. Its differentiation must be:
(1) built for solo tutors in Spain, in Spanish, with guardians and LOPDGDD
handled from day one; (2) the tutor's rules (2 h cancellation, late
cancellations charged, monthly billing) applied automatically; (3) simpler
and cheaper than general tutoring suites. As a portfolio project it is fully
feasible; as a SaaS the commercial risk is high and must be validated with
real tutors before investing in payments or marketing.

Sources: [TutorBird pricing (Capterra)](https://www.capterra.com/p/181623/TutorBird/pricing/) ·
[Teachworks (Software Advice)](https://www.softwareadvice.com/music-school/teachworks-profile/) ·
[Free tutoring software (Capterra ES)](https://www.capterra.es/directory/30849/tutoring/pricing/free/software) ·
[7DaysTutor (App Store)](https://apps.apple.com/mx/app/7daystutor/id6745792093)

## Annex B. Elicitation notes
<!-- TBD -->
